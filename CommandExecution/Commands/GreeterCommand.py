from CommandExecution.Commands.Command import Command

__author__ = 'Patrycja'


class GreeterCommand(Command):
    def __init__(self, nao_proxy):
        self.tts = nao_proxy.tts

    def execute(self):
        self.tts.say("Hello!")