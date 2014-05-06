from naoqi import ALBroker
from CommandExecution.NaoBasicCommandExecutor import NaoBasicCommandExecutor
from TextToCommand.Errors import CommandNotFoundError
from TextToCommand.SimpleCommandLinker import SimpleCommandLinker
from VoiceToText.MockSpeechRecognizer import MockSpeechRecognizer
from VoiceToText.NaoVoiceRecognition import NaoRecognizer

import time
import sys

myBroker = ALBroker("myBroker",
                    "0.0.0.0", # listen to anyone
                    0, # find a free port and use it
                    "10.20.106.251", # parent broker IP
                    9559)       # parent broker port

speechRecognizer = NaoRecognizer()
commandLinker = SimpleCommandLinker()
commandExecutor = NaoBasicCommandExecutor()


def textRecognized(text):
    speechRecognizer.stopRecognizing()
    try:
        command = commandLinker.getCommand(text)
        commandExecutor.executeCommand(command)
    except CommandNotFoundError as err:
        print "Command " + err.message + " not found"


def main():
    speechRecognizer.registerCallback(textRecognized)
    speechRecognizer.startRecognizing()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)


if __name__ == "__main__":
    main()

