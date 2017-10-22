#! /usr/bin/env python

import traceback
import struct
import time
import numpy as np
from collections import defaultdict

import rospy

import ros_vtd.msg as msg
from viRDBIcd import *

import scp_connection as scp_conn
import rdb_connection as rdb_conn

set_entity_template = """
<Set entity="player" name="{name}">
    <PosInertial hDeg="0" jumpToPos="true" x="{x}" y="{y}" z="0" />
    <Speed value="{speed}" />
    <Path id="-1" s="0.000" />
</Set>
"""

class VTDStepper:

    def __init__(self):
        # tells publishes the position the ego car should be in at each frame.
        # subscribes to the planner, but the position in each frame is the
        # interpolated positions
        rospy.init_node('vtd_stepper', anonymous=True)
        rospy.Subscriber("/planner_path", msg.planner_result,
                         self.planner_path_callback, queue_size=10)
        rospy.Subscriber("/scenario_setup", msg.scenario_start,
                         self.scenario_setup_callback, queue_size=10)

        self.waypoint_msgs = defaultdict(list)
        self.lastmsg = None
        self.prev_msg = None
        self.initalize_flag = False
        self.offset_time = 0.0
        self.players = {
            'PlayerA': {
                'id': 1,
                'name': 'PlayerA',
                'cfgModelId': 91
            },
            'PlayerB': {
                'id': 2,
                'name': 'PlayerB',
                'cfgModelId': 92
            }
        }
        self.scenario_start = {
            'xh': -136.0,
            'yh': -1.83,
            'vh': 30.0,
            'xr': -136.0,
            'yr': -6.09,
            'vr': 30.0
        }

        self.empty_plan = True

    def set_rdb_msg(self, pos, h=0.0, player='PlayerB'):
        # fill with default values, only update the position
        msg = RDB_OBJECT_STATE_t()
        msg.base.id = self.players[player]['id']
        msg.base.category = 1
        msg.base.type = 1
        msg.base.visMask = 1
        msg.base.name = self.players[player]['name']
        msg.base.cfgFlags = 3
        msg.base.cfgModelId = self.players[player]['cfgModelId']
        msg.base.geo.dimX = 4.22100019455
        msg.base.geo.dimY = 1.76199996471
        msg.base.geo.dimZ = 1.46500003338
        msg.base.geo.offX = 1.3654999733
        msg.base.geo.offY = 0.0
        msg.base.geo.offZ = 0.0
        msg.base.pos.x = pos[0]
        msg.base.pos.y = pos[1]
        msg.base.pos.h = h
        msg.base.pos.flags = 3

        return msg

    def planner_path_callback(self, planner_result, player='PlayerB'):
        self.waypoint_msgs.clear()
        self.empty_plan = False
        for t, x, y in zip(planner_result.t, planner_result.x, planner_result.y):
            # planner also sends 0.0 time to initialize the setup
            if t == 0.0:
                self.initalize_flag = True
                self.prev_msg = (0.0, self.set_rdb_msg((x, y), player=player))
            else:
                msg = self.set_rdb_msg((x, y), player=player)
                self.waypoint_msgs[msg.base.id].append((t, msg))

    def scenario_setup_callback(self, scenario_start):
        print("Setting scenario initial conditions to: ", scenario_start)
        self.scenario_start['xh'] = scenario_start.xh
        self.scenario_start['yh'] = scenario_start.yh
        self.scenario_start['vh'] = scenario_start.vh
        self.scenario_start['xr'] = scenario_start.xr
        self.scenario_start['yr'] = scenario_start.yr
        self.scenario_start['vr'] = scenario_start.vr

    def get_encoded(self, sim_time, sim_frame, rbd_frame_msgs, pkg_id, extended=True):
        """
        returns header for message
        """
        msg_header = RDB_MSG_HDR_t(
            frameNo=sim_frame, simTime=sim_time, magicNo=35712, version=285)
        msg_header.headerSize = msg_header.size
        header = RDB_MSG_ENTRY_HDR_t()
        msg_size = rbd_frame_msgs[0].size
        n_msgs = len(rbd_frame_msgs)
        header.pkgId = pkg_id
        header.headerSize = header.size
        header.dataSize = msg_size * n_msgs
        header.elementSize = msg_size
        header.flags = RDB_PKG_FLAG_EXTENDED if extended else 0x0
        msg_header.dataSize = header.size + (msg_size * n_msgs)
        encoded = msg_header.pack() + header.pack()
        for msg in rbd_frame_msgs:
            encoded += msg.pack()

        return encoded

    def interpolate_pos(self, plan_msg, curr_time, prev_msg):
        # print("PREV: %f, %f | %f, %f" % (prev_msg[1].base.pos.x,
        #                                  prev_msg[1].base.pos.y,
        #                                  plan_msg[1].base.pos.x,
        #                                  plan_msg[1].base.pos.y))
        # everything is in sim_(real)_time
        gamma = (curr_time - prev_msg[0]) / \
            (plan_msg[0] + self.offset_time - prev_msg[0])
        x, y = (prev_msg[1].base.pos.x + gamma * (plan_msg[1].base.pos.x - prev_msg[1].base.pos.x),
                prev_msg[1].base.pos.y + gamma * (plan_msg[1].base.pos.y - prev_msg[1].base.pos.y))
        # print("Interpolated: %f, %f" % (x, y))
        h = np.arctan2(plan_msg[1].base.pos.y - prev_msg[1].base.pos.y,
                       plan_msg[1].base.pos.x - prev_msg[1].base.pos.x)
        return self.set_rdb_msg((x, y), h)

    def step(self, n_steps=1):
        """
        Step simulator for n_steps
        """
        command = "<SimCtrl><Step size=\"{}\" /></SimCtrl>"
        command = command.format(n_steps)
        # print("Sending: %r" % command)
        scp_conn.send_message(command)

    def send_driver_ctrl(self, header, entry_header, _):
        # plan_msg is in local time (start from zero, so the sim_time offset must be done manually)
        # plan_msg = (t, (x,y))
        # prev and curr_sim_time is in sim time, no offset required
        # prev_msg = (t, (x,y))
        curr_sim_time, curr_sim_frame = header.simTime, header.frameNo
        if self.initalize_flag:
            self.offset_time = curr_sim_time
            # only time prev needs to be offsetted
            self.prev_msg = (self.offset_time, self.prev_msg[1])

            # OR DOES THIS GO ON THE PLANNER SIDE???
            # we need to initialize the human controlled car as well ... how? SCP?
            init_human_msg = set_entity_template.format(name='PlayerA', x=self.scenario_start['xh'],
                                                                        y=self.scenario_start['yh'],
                                                                        speed=self.scenario_start['vh'])
            print('Sending: %s' % init_human_msg)
            scp_conn.send_message(init_human_msg)

            self.initalize_flag = False

        # print("Frame: %r : %r" % (curr_sim_frame, curr_sim_time))
        n_msgs = 1
        rdb_msgs = []
        i = 0
        if not self.waypoint_msgs:
            self.empty_plan = True
        # print(len(planner_msgs))

        for key, planner_msgs in self.waypoint_msgs.items():
            # looks for the future position relative to current sim time
            while len(planner_msgs) > 0 and planner_msgs[0][0] <= curr_sim_time - self.offset_time:
                a = planner_msgs.pop(0)
                print("PAST PLANNER WAYPOINT: ", a[0])
            if len(planner_msgs) == 0:
                self.empty_plan = True
                print("NO MORE ITEMS")
                continue

            # get the point that is the nearest future
            plan_msg = planner_msgs[0]
            # interpolate to get the appropriate position for that frame
            if self.prev_msg:
                step_pos = self.interpolate_pos(
                    plan_msg, curr_sim_time, self.prev_msg)
            else:
                step_pos = plan_msg[1]  # ....maybe?
            # update prev_msg
            self.prev_msg = (curr_sim_time, step_pos)
            # print((curr_sim_time, step_pos))
            i += 1
            # print("Sending message")

            rdb_msgs.append(step_pos)

        if len(rdb_msgs):
            encoded = self.get_encoded(
                curr_sim_time, curr_sim_frame, rdb_msgs, RDB_PKG_ID_OBJECT_STATE)

        if i == n_msgs:
            self.lastmsg = encoded
            rdb_conn.send_messages(curr_sim_time, curr_sim_frame, [encoded])

        elif self.lastmsg:
            rdb_conn.send_messages(
                curr_sim_time, curr_sim_frame, [self.lastmsg])

    def run(self, vtd_rate=60):
        rate = rospy.Rate(vtd_rate)
        rdb_conn.register_callback(
            RDB_PKG_ID_START_OF_FRAME, self.send_driver_ctrl)

        while not rospy.is_shutdown():
            # print("Plan empty?", self.empty_plan)
            if not self.empty_plan:
                # print("STEPPING.")
                self.step()
                rdb_conn.run_once()


if __name__ == '__main__':
    vtd_stepper = VTDStepper()
    vtd_stepper.run()