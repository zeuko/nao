__author__ = 'Patrycja'

from CommandExecution.CommandExecutor import CommandExecutor


class NaoGeneralCommandExecutor(CommandExecutor):
    def __init__(self):
        pass

    def executeCommand(self, command):
        command.execute()
