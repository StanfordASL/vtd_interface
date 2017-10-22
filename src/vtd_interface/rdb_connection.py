# Author: Wolf Vollprecht
# This file handles the RDB connection

import rospy
from ros_vtd.msg import *
from viRDBIcd import *
import traceback
import struct
import socket
import time
from collections import defaultdict

TCP_IP = '127.0.0.1'
RDB_PORT = 48190
SCP_PORT = 48179
BUFFER_SIZE = 204800

rdb_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rdb_conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
rdb_conn.connect((TCP_IP, RDB_PORT))

data = b''  # empty global data
callbacks = {}

def register_callback(key, cb):
    """
    Register a callback to a specific RDB message 
    The key is a RDB_MSG_ID. 

    To execute a callback everytime a RDB_PKG_ID_START_OF_FRAME
    is received register a callback like so:


    import rdb_connection as rdb_conn
    from viRDBlcd import RDB_PKG_ID_START_OF_FRAME

    def cb(header, entry_header, msgs):
        pass

    register_callback(RDB_PKG_ID_START_OF_FRAME, cb)

    """
    global callbacks
    callbacks[key] = cb


def run_once():
    """
    Run this function in your ROS main loop to receive data and call according callbacks.
    """
    receive()
    parse_data()

def send_messages(sim_time, sim_frame, messages):
    """
    Send a list of messages for sim_time and sim_frame
    This function also sends the start and end frame, so use only once per frame
    """

    msg_header = RDB_MSG_HDR_t(frameNo=sim_frame, simTime=sim_time, magicNo=35712, version=285)
    msg_header.headerSize = msg_header.size

    frame_control_msg = RDB_MSG_ENTRY_HDR_t()
    frame_control_msg.pkgId = RDB_PKG_ID_START_OF_FRAME
    frame_control_msg.headerSize = frame_control_msg.size
    frame_control_msg.dataSize = 0

    msg_header.dataSize = frame_control_msg.headerSize + frame_control_msg.dataSize

    rdb_conn.sendall(msg_header.pack() + frame_control_msg.pack())

    for msg in messages:
        rdb_conn.sendall(msg)

    frame_control_msg.pkgId = RDB_PKG_ID_END_OF_FRAME

    rdb_conn.sendall(msg_header.pack() + frame_control_msg.pack())

def receive():
    """
    Receive data from buffer and write append to global data variable

    Probably `run_once` is more appropriate for your use case
    """
    global data, rdb_conn
    recv = rdb_conn.recv(BUFFER_SIZE)

    if len(recv) == 0:
        print("Had to reconnect")
        rdb_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rdb_conn.connect((TCP_IP, RDB_PORT))
        data = rdb_conn.recv(BUFFER_SIZE)

    else:
        data += recv

    return data


def parse_data():
    """
    This function parses the global data stream

    Probably `run_once` is more appropriate for your use case
    """

    global data

    delete_up_to = 0
    need_more_data = False
    magic_no_idx = -1

    recorded_data = []

    total_data = len(data)
    i = 0

    while i <= len(data) - 2:
        header = RDB_MSG_HDR_t()
        header.unpack(data[i:i + header.size])

        if header.magicNo != RDB_MAGIC_NO:
            print("Messages out of sync.")
            i += 1
            continue

        delete_up_to = magic_no_idx = i

        if total_data - i < header.dataSize:
            need_more_data = True
            break

        i += header.headerSize

        entry_header = RDB_MSG_ENTRY_HDR_t()
        entry_header.unpack(data[i:i + entry_header.size])

        i += entry_header.headerSize

        if callbacks.get(entry_header.pkgId):
            msgs = []
            if entry_header.elementSize:
                try:
                    typ = type_dict[entry_header.pkgId]

                except KeyError:
                    print("This key doesn't exist: %r" % entry_header.pkgId)
                    delete_up_to = magic_no_idx + header.dataSize
                    break

                for j in range(int(round(entry_header.dataSize / entry_header.elementSize))):
                    t = typ()

                    if t.size > entry_header.elementSize:
                        if t.__fields_types__.get('base') is not None:

                            # don't unpack extended!
                            typ_base = t.__fields_types__['base'][0]
                            tb = typ_base()
                            tb.unpack(data[i:i + entry_header.elementSize])
                            t.base = tb
                            msgs.append(t)
                            i += entry_header.elementSize

                        else:
                            print("Something wrong with element size for message: %r, %r" % (t, entry_header))
                            break
                    else:
                        t.unpack(data[i:i + t.size])
                        msgs.append(t)
                        i += len(t)

            callbacks[entry_header.pkgId](header, entry_header, msgs)

        else:
            i += entry_header.dataSize
            delete_up_to = magic_no_idx + header.dataSize + header.headerSize

    if magic_no_idx == -1:
        print("No magic number found.")
        delete_up_to = len(data)

    if delete_up_to != 0:
        data = data[delete_up_to:]

    return recorded_data