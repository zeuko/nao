__author__ = 'Patrycja'

from MasterModule.Commands.Command import Command


class MoveBackwardsCommand(Command):
    def __init__(self, nao_proxy):
        self.movement = nao_proxy.movement

    def execute(self):
        self.movement.moveTo(-1.0, 0.0, 0.0)