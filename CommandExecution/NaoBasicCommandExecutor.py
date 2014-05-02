from math import pi
from naoqi import ALProxy
from CommandExecution.CommandExecutor import CommandExecutor
from TextToCommand.Errors import CommandNotFoundError


class NaoBasicCommandExecutor(CommandExecutor):
    def __init__(self):
        self.move = ALProxy("ALMotion")

    def executeCommand(self, command):
        if command == "go forward":
            self.move.moveTo(1.0, 0.0, 0.0)
        elif command == "turn right":
            self.move.moveTo(0.0, 0.0, pi / 2.0)
        elif command == "turn left":
            self.move.moveTo(0.0, 0.0, -pi / 2.0)
        else:
            raise CommandNotFoundError(command)
