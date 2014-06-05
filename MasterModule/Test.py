# -*- encoding: UTF-8 -*-
""" Say 'hello, you' each time a human face is detected

"""

import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser
from CommandExecution.NaoBasicCommandExecutor import NaoBasicCommandExecutor
from TextToCommand.SimpleCommandLinker import SimpleCommandLinker

NAO_IP = "127.0.0.1"


# Global variable to store the HumanGreeter module instance
VoiceRecognition = None
memory = None
asr = None
commandLinker = SimpleCommandLinker()
commandExecutor = None


class VoiceRecognitionModule(ALModule):
    """ A simple module able to react
    to facedetection events

    """

    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker


        # Subscribe to the FaceDetected event:
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("WordRecognized",
                                "VoiceRecognition",
                                "onWordDetected")

    def onWordDetected(self, key, value, message):
        """ This will be called each time a face is
        detected.

        """
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        memory.unsubscribeToEvent("WordRecognized",
                                  "VoiceRecognition")

        print "Rozpoznano: " + value[0] + ": " + str(value[1])
        com = commandLinker.getCommand(value[0])
        if value[1] > 0.5:
            commandExecutor.executeCommand(com)

        # Subscribe again to the event
        memory.subscribeToEvent("WordRecognized",
                                "VoiceRecognition",
                                "onWordDetected")
    def shutdown(self):
        memory.unsubscribeToEvent("WordRecognized",
                                  "VoiceRecognition")


def main():
    """ Main entry point

    """
    parser = OptionParser()
    parser.add_option("--pip",
                      help="Parent broker port. The IP address or your robot",
                      dest="pip")
    parser.add_option("--pport",
                      help="Parent broker port. The port NAOqi is listening to",
                      dest="pport",
                      type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=9559)

    (opts, args_) = parser.parse_args()
    pip = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
                        "0.0.0.0", # listen to anyone
                        0, # find a free port and use it
                        pip, # parent broker IP
                        pport)       # parent broker port


    # Warning: HumanGreeter must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global asr
    asr = ALProxy("ALSpeechRecognition")
    asr.setLanguage("English")
    wordList = ["go forward", "turn left", "turn right", "stop", "stand up", "hello nao", "sit down"]
    #asr.setVocabulary(wordList, True)

    global commandExecutor
    commandExecutor = NaoBasicCommandExecutor()

    global VoiceRecognition
    VoiceRecognition = VoiceRecognitionModule("VoiceRecognition")
    # HumanGreeter.shutdown()

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