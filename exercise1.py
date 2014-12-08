#!/usr/bin/env python
# -*- coding: utf-8 -*-
from uuid import getnode as get_mac

__author__ = "Emin Mastizada"
__description__ = "Implement 7 layer data flow"

from details import get_data


def application_layer(data):
    """
    Implementation of application layer
    Adds application type to data
    Example application layer used: telnet
    AH-data
    :param data: string
    :return: string
    """
    application = 'telnet'
    app_data = application + '|' + data
    " Test print: "
    print("\nApplication Layer:", app_data)
    return app_data


def presentation_layer(data):
    """
    Implementation of presentation layer
    Adds presentation type to data
    Example presentation type: ASCII
    PH-data
    :param data: string
    :return: string
    """
    presentation = 'ASCII'
    app_data = presentation + '|' + application_layer(data)
    " Test print: "
    print("\nApplication Layer:", app_data)
    return app_data


def session_layer(data):
    """
    Implementation of session protocol layer
    Adds session protocol name to data
    Example session protocol: SCP: Session Control Protocol
    SH-data
    :param data: string
    :return: string
    """
    session = 'SCP'
    app_data = session + '|' + presentation_layer(data)
    " Test print: "
    print("\nSession Layer:", app_data)
    return app_data


def transport_layer(data):
    """
    Implementation of transport layer
    Adds transport layer protocol to data
    Example transport layer protocol: UDP: User Datagram Protocol
    TH-data
    :param data: string
    :return: string
    """
    transport = 'UDP'
    app_data = transport + '|' + session_layer(data)
    " Test print: "
    print("\nTransport Layer:", app_data)
    return app_data


def network_layer(data):
    """
    Implementation of network layer
    Adds network protocol type to data
    Example network protocol: IPv4: Internet Protocol
    NH-data
    :param data:
    :return:
    """
    network = 'IPv4'
    app_data = network + '|' + transport_layer(data)
    " Test print: "
    print("\nNetwork Layer:", app_data)
    return app_data


def ll_sublayer():
    """
    Implementation of logical link sublayer
    Example logical link sublayer: 802.11n
    :return: string
    """
    return '802.11n'


def mac_sublayer():
    """
    Returns device's mac address
    :return: string
    """
    device_mac = get_mac()
    print("\nDevice's MAC:", ':'.join(("%012X" % device_mac)[i:i + 2] for i in range(0, 12, 2)))
    return str(device_mac)


def data_link_layer(data):
    """
    Implementation of data link layer
    Adds logical link data and mac data to main data
    DH-data-DH
    :param data: str
    :return: str
    """
    app_data = mac_sublayer() + '|' + ll_sublayer() + '|' + network_layer(
        data) + '|' + mac_sublayer() + '|' + ll_sublayer()
    " Test print: "
    print("\nData Link Layer:", app_data)
    return app_data


def physical_layer(data):
    """
    Implementation of physical layer
    Makes binary data from string data
    Example modulation: convert string to binary
    :param data: string
    :return: string
    """
    data = data_link_layer(data)
    app_data = ''
    for layer in data.split('|'):
        app_data += ''.join(format(ord(symbol), 'b') for symbol in layer) + '|'
    return app_data


""" Le Start """
if __name__ == '__main__':
    data = get_data()
    print("\n\nPhysical Data (separated by '|'):", physical_layer(data))
