__author__ = 'Patrycja'

from naoqi import ALProxy


class NaoModules:
    """ Simple class providing proxies for basic NAO modules. Instance of this class is passed to every
        specific Command to give commands easier access to basic NAO proxies.

    """
    def __init__(self):
        self.movement = ALProxy("ALMotion")
        self.posture = ALProxy("ALRobotPosture")
        self.tts = ALProxy("ALTextToSpeech")