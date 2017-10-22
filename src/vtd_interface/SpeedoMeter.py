#!/usr/bin/env python
import rospy
from ros_vtd.msg import *
from viRDBIcd import *
import traceback
import struct
import socket

from matplotlib import pyplot as plt
from matplotlib import patches as patches

import sys
import numpy as np

# ALL IN MPH (any m/s is converted in MPH)
plt.ion()

def speed_to_angle(speed, max_speed):
    ratio = speed/max_speed
    return (1 - ratio) * np.pi

def get_needle(speed, radius, max_speed):
    angle = speed_to_angle(speed, max_speed)
    x, y = radius*np.cos(angle), radius*np.sin(angle)
    x1, y1 = 0.95*radius*np.cos(angle), 0.95*radius*np.sin(angle)
    return np.array([0, x1, x]), np.array([0, y1, y])

def plot_speed_text(ax, radius, max_speed, units, increment, offset = 0.01):
    for speed in np.arange(0, max_speed + 1, increment):
        x, y = get_needle(speed, radius + offset, max_speed)
        if x[-1] < 0:
            ax.text(x[-1]-0.02, y[-1] + 0.005, str(int(speed)))
        else:
            ax.text(x[-1], y[-1] + 0.005, str(int(speed)))
        x, y = get_needle(speed, radius, max_speed)
        ax.plot(x[-2:], y[-2:], color = "black")


class CarSound:

    def __init__(self, player_id, x_offset, y_offset, mean_speed = 70, increment = 2, alert_speed = 85):
        rospy.init_node('speedo' + player_id, anonymous=True)
        rospy.Subscriber('/object_state/' + player_id, rdb_object_state, self.car_callback)
        self.v = 0
        self.mean_speed = mean_speed
        self.increment = 2
        self.ms_to_mph = 2.23694
        self.n_players = 1

        # plotting variables
        self.radius = 0.2
        self.max_speed = 100.0
        self.speed_limit = 80.0
        self.ratio = 1 - self.speed_limit / self.max_speed
        self.speedo_increment = 10
        self.units = "mph"
        self.speedo_base = patches.Wedge((0,0), 0.2, self.ratio*180, 180, color = 'lightcoral', alpha = 0.3)
        self.speedo_fast = patches.Wedge((0,0), 0.2, 0, self.ratio*180, color = 'indianred', alpha = 0.4)
        self.fig, self.ax = plt.subplots(figsize = (4, 2), facecolor='white')
        self.alert_speed = alert_speed

        self.ax.add_patch(self.speedo_base)
        self.ax.add_patch(self.speedo_fast)
        self.ax.axis([-0.25, 0.25, 0, 0.25])
        self.ax.axis('off')
        plot_speed_text(self.ax, self.radius, self.max_speed, self.units, self.speedo_increment)

        plt.get_current_fig_manager().window.wm_geometry("+%s+%s" % (x_offset, y_offset))

        plt.pause(0.001)

    def car_callback(self, data):
        self.v = np.linalg.norm([data.ext.speed.x, data.ext.speed.y]) * self.ms_to_mph

    def runall(self):
        rate = rospy.Rate(10) # 10 Hz
        print("RUNNING LIKE A CHAMP")

        while not rospy.is_shutdown():

            self.ax.cla()
            self.ax.add_patch(self.speedo_base)
            self.ax.add_patch(self.speedo_fast)
            self.ax.axis([-0.25, 0.25, 0, 0.25])
            plot_speed_text(self.ax, self.radius, self.max_speed, self.units, self.speedo_increment)
            needle_x, needle_y = get_needle(self.v, self.radius, self.max_speed)
            self.ax.arrow(0, 0, needle_x[-1], needle_y[-1], head_width=0.02, head_length=0.05, fc='k', ec='k', length_includes_head = True)
            if self.v < self.speed_limit: 
                 self.ax.text(-0.08, 0.05, str(round(self.v, 1)), fontsize = 40)
                 # self.ax.text(-0.23, 0.2, self.units, fontsize = 30)
            else:
                 self.ax.text(-0.08, 0.05, str(round(self.v, 1)), fontsize = 40, color = 'red')
                 # self.ax.text(-0.23, 0.2, self.units, fontsize = 30, color = 'red')
            self.ax.axis('off')

            plt.pause(0.001)
            rate.sleep()

if __name__ == '__main__':
  player, x_offset, y_offset = sys.argv[1], sys.argv[2], sys.argv[3]
  cs = CarSound(player, x_offset, y_offset)
  cs.runall()