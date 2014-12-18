from math import pi

from naoqi import ALProxy
from CommandExecution.CommandExecutor import CommandExecutor
from MasterModule.Errors import CommandNotFoundError


class NaoBasicCommandExecutor(CommandExecutor):
    def __init__(self):
        self.move = ALProxy("ALMotion")
        self.posture = ALProxy("ALRobotPosture")
        self.tts = ALProxy('ALTextToSpeech')

    def executeCommand(self, command):
        if command == "go forward":
            self.move.moveTo(1.0, 0.0, 0.0)
        elif command == "turn right" or command == "vpravvo":
            self.move.moveTo(0.0, 0.0, -pi / 2.0)
        elif command == "turn left" or command == "vlevvo":
            self.move.post.moveTo(0.0, 0.0, pi / 2.0)
        elif command == "stand up":
            self.posture.goToPosture("StandInit", 0.8)
        elif command == "hello nao":
            self.tts.say("Hello, Patricia!")
        elif command == "sit down":
            self.posture.goToPosture("Sit", 0.8)
        elif command == "go back":
            self.move.moveTo(-1.0, 0.0, 0.0)
        elif command == "napshoot":
            self.move.moveTo(1.0, 0.0, 0.0)
        elif command == "fstech":
            self.move.moveTo(-1.0, 0.0, 0.0)
        else:
            raise CommandNotFoundError(command)
