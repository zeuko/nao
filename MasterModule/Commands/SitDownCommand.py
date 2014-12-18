__author__ = 'Patrycja'

from MasterModule.Commands.Command import Command


class SitDownCommand(Command):
    def __init__(self, nao_proxy):
        self.posture = nao_proxy.posture

    def execute(self):
        self.posture.goToPosture("Sit", 0.8)
