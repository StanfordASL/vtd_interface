import rosbag
import subprocess
from subprocess import Popen
import sys
import signal
import time
import os
import sys

process = None



def start(topics, filename, folder='~/bags/'):
	global process
	folder = os.path.expanduser(folder)
	if not os.path.isdir(folder):
		os.mkdir(folder)
	os.chdir(os.path.expanduser(folder))

	command = ['rosbag', 'record', '-O', filename]
	command.extend(topics)
	process = Popen('exec ' + ' '.join(command), stdin=subprocess.PIPE, stdout=subprocess.PIPE, preexec_fn=os.setsid, shell=True)

def stop():
	global process
	if process is not None:
		print("KILLING PROCESS")
		os.killpg(os.getpgid(process.pid), signal.SIGINT)
		time.sleep(0.1)

def sigint_handler(*args):
	print("Stopping rosbag")
	stop()
	sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)
