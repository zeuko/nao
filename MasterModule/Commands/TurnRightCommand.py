__author__ = 'Patrycja'

from math import pi
from MasterModule.Commands.Command import Command


class TurnRightCommand(Command):
    def __init__(self, nao_proxy):
        self.movement = nao_proxy.movement

    def execute(self):
        self.movement.moveTo(0.0, 0.0, -pi / 2.0)