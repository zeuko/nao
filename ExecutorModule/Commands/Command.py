__author__ = 'Patrycja'


class Command:
    """ Base class for implementations of executable NAO commands.
        Each custom implemented class MUST extend this class. """
    def __init__(self):
        pass

    def execute(self):
        pass