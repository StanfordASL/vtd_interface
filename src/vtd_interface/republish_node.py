#! /usr/bin/env python

# Author: Wolf Vollprecht <w.vollprecht@gmail.com>
#
# This script parses VTD messages and republishes them as ROS messages under specific topics
#

import rospy
from ros_vtd.msg import *
from viRDBIcd import *
import traceback
import struct
import socket

import rdb_connection as rdb

type_map = {
    'RDB_GEOMETRY_t': rdb_geometry,
    'RDB_OBJECT_STATE_BASE_t': rdb_object_state_base,
    'RDB_OBJECT_STATE_EXT_t': rdb_object_state_ext,
    'RDB_COORD_t': rdb_coord,
}

ros_to_pkg_id = {
    RDB_PKG_ID_OBJECT_STATE: rdb_object_state,
    RDB_PKG_ID_ROAD_POS: rdb_road_pos,
    RDB_PKG_ID_DRIVER_CTRL: rdb_driver_ctrl
}

pub_map = {}


def rdb_to_ros(msg, typ=rdb_object_state_base, timestamp=None):
    r = typ()
    d = msg.__dict__
    keys = list(d.keys())
    for k in keys:
        if isinstance(d[k], (float, int, str)):
            setattr(r, k, d[k])
        elif isinstance(d[k], bytes):
            if k in ('name', 'modelName', 'fileName'):
                d[k] = d[k].split(b'\0',1)[0].decode('ascii')
            elif k == 'laneId':
                d[k] = ord(d[k][0])
        else:
            n = d[k].__class__.__name__
            if n in type_map:
                setattr(r, k, rdb_to_ros(d[k], typ=type_map[n]))
    if timestamp:
        r.simTime = timestamp
    return r


def pub_as_ros(header, entry_header, msgs):
    typ = ros_to_pkg_id[entry_header.pkgId]
    timestamp = header.simTime
    base_name = '/' + typ.__name__[4:] + '/'

    for msg_single in msgs:
        ros_msg = rdb_to_ros(msg_single, typ, timestamp)

        if entry_header.pkgId == RDB_PKG_ID_OBJECT_STATE:
            playerId = msg_single.base.id
        else:
            playerId = msg_single.playerId

        pub_name = base_name + str(playerId)
        publisher = pub_map.get(pub_name)
        if not publisher:
            pub_map[pub_name] = rospy.Publisher(pub_name, typ, queue_size=10)
            publisher = pub_map[pub_name]
        publisher.publish(ros_msg)


def run():
    rospy.init_node('ros_vtd')
    rospy.sleep(0.5)
    rospy.loginfo('Node started')
    rospy.loginfo('Running until shutdown (Ctrl-C).')

    # Register callbacks for different ROS/RDB messages here:

    rdb.register_callback(RDB_PKG_ID_OBJECT_STATE, pub_as_ros)
    rdb.register_callback(RDB_PKG_ID_ROAD_POS,     pub_as_ros)
    rdb.register_callback(RDB_PKG_ID_DRIVER_CTRL,  pub_as_ros)

    while not rospy.is_shutdown():
        rdb.run_once()

    rospy.loginfo('Node finished')


if __name__ == '__main__':
    # TODO add argument parsing.
    run()
