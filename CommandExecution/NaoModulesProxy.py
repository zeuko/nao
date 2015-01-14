__author__ = 'Patrycja'

from naoqi import ALProxy


class NaoModules:
    """ Simple class providing proxies for basic NAO modules."""
    def __init__(self):
        self.movement = ALProxy("ALMotion")
        self.posture = ALProxy("ALRobotPosture")
        self.tts = ALProxy('ALTextToSpeech')