from CommandExecution.Commands.Command import Command

__author__ = 'Patrycja'


class StandUpCommand(Command):
    def __init__(self, nao_proxy):
        self.posture = nao_proxy.posture

    def execute(self):
        self.posture.goToPosture("StandInit", 0.8)

