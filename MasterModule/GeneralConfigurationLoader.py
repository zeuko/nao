__author__ = 'Michal'

import ConfigParser
import socket


commands = ["go forward", "turn left", "turn right", "go back", "stand up", "hello nao", "sit down", "napshoot", "shut down", "fstech", "vlevvo", "vpravvo"]


def readConfiguration(filename):
    config = ConfigParser.ConfigParser()
    config.read(filename)

    threshold = 0.5
    try:
        inputThreshold = config.getfloat('Main', 'threshold')
        if 0.0 <= inputThreshold <= 1.0:
            threshold = inputThreshold
        else:
            raise ValueError
    except ValueError:
        print 'Invalid threshold value in configuration file. Setting to default:', threshold

    ip = '127.0.0.1'
    try:
        inputIP = config.get('Main', 'ip')
        socket.inet_aton(inputIP)
        ip = inputIP
    except socket.error:
        print 'Invalid ip value in configuration file. Setting to default:', ip

    port = '9559'
    try:
        inputPort = config.getint('Main', 'port')
        if 0 <= inputPort <= 65535:
            port = inputPort
        else:
            raise ValueError
    except ValueError:
        print 'Invalid port value in configuration file. Setting to default:', port

    config_file = 'command_config_eng.cfg'
    try:
        config_file = config.get('Main', 'command_config_filepath')
    except socket.error:
        print 'Invalid command config filepath in configuration file. Setting to default:', config_file

    return ip, port, threshold, config_file
