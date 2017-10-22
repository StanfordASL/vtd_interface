import scp_connection as SCP
import os
import subprocess
import record
from bs4 import BeautifulSoup
from random import randint
import numpy as np
from time import gmtime, strftime, localtime

set_entity_template = """
<Set entity="player" name="{name}">
    <PosInertial hDeg="0" jumpToPos="true" x="{x}" y="{y}" z="0" />
    <Speed value="{speed}" />
    <Path id="-1" s="0.000" />
</Set>
"""

set_speed_template = """
<Set entity="player" name="{name}">
    <Speed value="{speed}" />
</Set>
"""

init_positions = {}

def load_scenario(scenario):
    with open(scenario, 'r') as fi:
        soup = BeautifulSoup(fi.read(), "html.parser")

    players = soup.find_all("player")

    for player in players:
        init_positions[player.description['name']] = {
            'x': float(player.init.posabsolute['x']),
            'y': float(player.init.posabsolute['y']),
        }

    return init_positions


def set_starting_condition(name, swap, vel, d_vel, co_t):
    use_name = name
    # swapping players
    if swap and name == 'PlayerA':
        use_name = 'PlayerB'
    elif swap and name == 'PlayerB':
        use_name = 'PlayerA'

    if use_name == 'PlayerA':
        start_speed_m_s = vel
    elif use_name == 'PlayerB':
        start_speed_m_s = vel + d_vel

    pos = init_positions[use_name]
    # play around with this
    x_start = -145.0
    y_start = pos['y']

    if use_name == 'PlayerB':
        x_start -= d_vel * co_t

    msg = set_entity_template.format(
            name=name,
            speed=start_speed_m_s,
            x=x_start,
            y=y_start
        )
    SCP.send_message(msg)

def main(name_a, name_b, scenario='/home/aslsim/Simulator/VTD.2.0/Data/Projects/Current/Scenarios/ScenarioDBOff.xml'):

    players = load_scenario(scenario)
    print(players)
    vel_list = [29]   # mean velocity is 65mph
    swap_list = [0, 1]
    d_vel_list = [-2, 0, 2]
    co_t_list = [1, 2, 3]
    configs = np.array([[v, s, dv, co] for v in vel_list for s in swap_list for dv in d_vel_list for co in co_t_list])

    n_configs = len(configs)
    # # vel = randint(27, 32)
    # vel = 29    # mean velocity is 65mph
    # d_vel = 2*randint(-1, 1)
    # co_t = randint(1, 3)
    is_recording = False
    round_idx = 0
    while True:
        # SCP.send_message('<Traffic><Reset /></Traffic>')

        # tetra shuffling
        round_idx += 1
        config_order = np.random.permutation(18)
        trial = 0
        while trial < n_configs:
        # for trial in range(n_configs):
            if is_recording:
                config = configs[config_order[trial]]
                vel = config[0]
                swap = config[1]
                d_vel = config[2]
                co_t = config[3]
                trial += 1
                print("Recording: Round: " + str(round_idx) + " -- " + str(trial) + "/" + str(n_configs) +\
                 " --> config: vel: %2i swap: %1i d_vel: %1i co_t: %1i"% tuple(config) )
            else:
                config = configs[config_order[randint(0, n_configs-1)]]
                vel = config[0]
                swap = config[1]
                d_vel = config[2]
                co_t = config[3]
                print("Not recording --> config: vel: %2i swap: %1i d_vel: %1i co_t: %1i"% tuple(config) )

            for player in players:
                # if player.description['control'] == 'external':
                    # print("Sending Message: %s" % msg)
                name = player
                set_starting_condition(name, swap, vel, d_vel, co_t)

            time_s = strftime("%H:%M:%S", localtime())
            fn = "{}_{}_{}_{}_{}_{}.bag".format(time_s, vel, swap, d_vel, co_t, round_idx)

            folder = '~/bags/' + strftime("%Y-%m-%d", localtime())  + '/' + name_a + '_and_' + name_b

            day_folder = '~/bags/' + strftime("%Y-%m-%d", localtime())

            full_day_folder = os.path.expanduser(day_folder)
            if not os.path.isdir(full_day_folder):
                os.mkdir(full_day_folder)
            os.chdir(os.path.expanduser(full_day_folder))

            if is_recording:
                record.start([
                    '/object_state/1',
                    '/object_state/2',
                    '/road_pos/1',
                    '/road_pos/2',
                    '/driver_ctrl/1',
                    '/driver_ctrl/2',
                ], filename=fn, folder=folder)

            s = raw_input("Press Enter to reset ...")
            if s == "":
                is_recording = True
            elif s == "nn":
                record.stop()
                return True
            elif s == "qq":
                record.stop()
                return False
            elif s == "rr":
                trial -= 1
                is_recording = True
            else:
                is_recording = False

            record.stop()

    return False

if __name__ == '__main__':
    switch_player = True
    while switch_player:

        player_a = raw_input("Name of Player 1: ")
        player_b = raw_input("Name of Player 2: ")

        switch_player = main(player_a, player_b)

    print("Finished data collection")






