#!/usr/bin/env python
# -*- coding: utf-8 -*-
import signal
from uuid import getnode as get_mac

__author__ = "Emin Mastizada"
__description__ = "Simulation of CDMA Network"

TIMEOUT = 10  # 10 second for each t for input, in real use less than second
FLOW = [(0, 0), (0, 0), (0, 0), (0, 0)]  # 4 chip sequence pairs


def interrupted(signum, frame):
    """
    called when read times out
    :param signum:
    :param frame:
    :return: boolean
    """
    return True
signal.signal(signal.SIGALRM, interrupted)


# noinspection PyBroadException
def get_transmits():
    """
    Gets data from all transmitters
    :return: array
    """
    signal.alarm(TIMEOUT)
    data = []
    data += [0, 0, 0, 0]
    try:
        t_1 = input("Transmit from t_1: ")
    except:
        t_1 = False
    if t_1:
        if len(t_1) > 0:
            data[0] = format(ord(t_1[0]), 'b')
    try:
        t_2 = input("Transmit from t_2: ")
    except:
        t_2 = False
    if t_2:
        if len(t_2) > 0:
            data[1] = format(ord(t_2[0]), 'b')
    try:
        t_3 = input("Transmit from t_3: ")
    except:
        t_3 = False
    if t_3:
        if len(t_3) > 0:
            data[2] = format(ord(t_3[0]), 'b')
    try:
        t_4 = input("Transmit from t_4: ")
    except:
        t_4 = False
    if t_4:
        if len(t_4) > 0:
            data[3] = format(ord(t_4[0]), 'b')
    signal.alarm(0)
    return data


def get_input():
    """
    Get standard input
    :return: array
    """
    receives = []
    receives += [0, 0, 0, 0]
    user_inputs = input("Standard input (max len: 4): ")
    for user_input in range(len(user_inputs)):
        receives[user_input] = format(ord(user_inputs[user_input][0]), 'b')
    return receives


""" Main Work """
while True:
    inputs = get_input()
    transmits = get_transmits()
    "\n\nWorker: Got data from all receivers and transmitters"
    for sequence in range(len(FLOW)):
        if transmits[sequence]:
            _t = transmits[sequence]
        else:
            _t = 0
        if inputs[sequence]:
            _r = inputs[sequence]
        else:
            _r = 0
        FLOW[sequence] = (_t, _r)
    print(FLOW)