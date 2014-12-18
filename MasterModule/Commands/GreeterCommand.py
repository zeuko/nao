__author__ = 'Patrycja'

from MasterModule.Commands.Command import Command


class GreeterCommand(Command):
    def __init__(self, nao_proxy):
        self.tts = nao_proxy.tts

    def execute(self):
        self.tts.say("Hello!")