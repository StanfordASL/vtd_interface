#!/usr/bin/env python
import rospy
from ros_vtd.msg import *

import os
import wave
import threading
import sys
import pyaudio
import numpy as np


class WaveCarSoundLoop(threading.Thread):
    def __init__(self, filepath, loop=True):
        super(WaveCarSoundLoop, self).__init__()
        self.filepath = os.path.abspath(filepath)
        self.loop = loop
        self.d_shift_left = 0
        self.d_shift_right = 0
        self.ratio_left = 1.0
        self.ratio_right = 1.0
        self.player = pyaudio.PyAudio()

    def run(self):
        wf = wave.open(self.filepath, 'rb')
        duration = wf.getnframes()
        # duration = 40000
        stream = self.player.open(format = self.player.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True)
        data = wf.readframes(duration)
        da = np.fromstring(data, dtype=np.int16)
        left, right = da[0::2], da[1::2]  # left and right channel
        N = len(left) # == len(right)
        while self.loop:
            nl = np.interp(np.arange(N) * self.ratio_left, np.arange(N), left, period = N)
            nr = np.interp(np.arange(N) * self.ratio_right, np.arange(N), right, period = N)
            print("INTERPOLATING WITH %f %f" % (self.ratio_left, self.ratio_right))
            # lf, rf = np.fft.rfft(left), np.fft.rfft(right)
            # lf, rf = np.roll(lf, self.d_shift_left), np.roll(rf, self.d_shift_right)
            # if self.d_shift_left > 0: lf[:self.d_shift_left] = 0
            # if self.d_shift_right > 0: lf[:self.d_shift_right] = 0
            # if self.d_shift_left < 0: lf[self.d_shift_left:] = 0
            # if self.d_shift_right < 0: lf[self.d_shift_right:] = 0
            # nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)

            ns = np.column_stack((nl, nr)).ravel().astype(np.int16)
            shifted_data = ns.tostring()
            stream.write(shifted_data)

        stream.close()
        self.player.terminate()


    def play(self):
        self.start()

    def stop(self):
        self.loop = False


class CarSound:

    def __init__(self, mean_speed = 75, increment = 2, alert_speed = 85):
        rospy.init_node('sound_generator', anonymous=True)
        rospy.Subscriber('/object_state/1', rdb_object_state, self.car1_callback)
        rospy.Subscriber('/object_state/2', rdb_object_state, self.car2_callback)
        self.v1 = 0
        self.v2 = 0
        self.mean_speed = mean_speed
        self.increment = increment
        self.alert_speed = alert_speed
        self.ms_to_mph = 2.23694


    def car1_callback(self, data):
        self.v1 = data.ext.speed.x * self.ms_to_mph

    def car2_callback(self, data):
        self.v2 = data.ext.speed.x * self.ms_to_mph



    def run(self, wp):
        rate = rospy.Rate(10) # 10 Hz
        wp.play()
        while not rospy.is_shutdown():
            wp.ratio_right = self.v1 / self.mean_speed if self.v1 < self.alert_speed else 100.0
            wp.ratio_left = self.v2 / self.mean_speed if self.v2 < self.alert_speed else 100.0
            # print(wp.ratio_right, wp.ratio_left, self.v1, self.v2)
            rate.sleep()
        else:
            wp.stop()

if __name__ == '__main__':
    cs = CarSound()
    car_sound_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                      "assets/accel_sound_trim_variable.wav")
    print car_sound_filename
    wav_player = WaveCarSoundLoop(car_sound_filename)
    cs.run(wav_player)