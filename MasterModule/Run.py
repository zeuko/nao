# -*- encoding: UTF-8 -*-


import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from GeneralConfigurationLoader import readConfiguration
from ExecutorModule.NaoGeneralCommandExecutor import NaoGeneralCommandExecutor
from TextToCommand.GeneralCommandLinker import GeneralCommandLinker
import MasterModule.CommandConfigurationLoader

COMMAND_CONFIG_PATH = '../command_config_eng.cfg'
CONFIG_PATH = '../config.cfg'
NAO_IP = "10.20.106.251"
NAO_PORT = 9559
THRESHOLD = 0.5

# Global variable to store the SpeechRecognizer module instance - it is REQUIRED by NAOqi
SpeechRecognizer = None
memory = None
myBroker = None
asr = None
commandLinker = None
commandExecutor = None


class SpeechRecognizerModule(ALModule):
    """ A module able to react to word recognition events, used by main application.

    """

    def __init__(self, name):
        ALModule.__init__(self, name)
        # No need for IP and port here because
        # we have our Python broker connected to NAOqi broker


        # Subscribe to the WordRecognized event:
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("WordRecognized",
                                "SpeechRecognizer",
                                "onWordRecognized")

    def onWordRecognized(self, key, value, message):
        """ This will be called each time a face is
        detected.

        """
        # Unsubscribe to the event when executing
        memory.unsubscribeToEvent("WordRecognized",
                                  "SpeechRecognizer")

        print "Recognized: " + value[0] + ": " + str(value[1])
        com = commandLinker.getCommand(value[0])
        if com == "shutdown":
            myBroker.shutdown()
            return

        if value[1] > THRESHOLD:
            commandExecutor.executeCommand(com)

        # Subscribe again to the event
        memory.subscribeToEvent("WordRecognized",
                                "SpeechRecognizer",
                                "onWordRecognized")

    def shutdown(self):
        memory.unsubscribeToEvent("WordRecognized",
                                  "SpeechRecognizer")


def main():
    """ Main entry point.

    """

    global NAO_PORT, NAO_IP, THRESHOLD, COMMAND_CONFIG_PATH
    global commandExecutor, commandLinker, asr

    NAO_IP, NAO_PORT, THRESHOLD, COMMAND_CONFIG_PATH = readConfiguration(CONFIG_PATH)

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    global myBroker
    myBroker = ALBroker("myBroker",
                        "0.0.0.0",  # listen to anyone
                        0,  # find a free port and use it
                        NAO_IP,  # parent broker IP
                        NAO_PORT)  # parent broker port



    asr = ALProxy("ALSpeechRecognition")
    asr.setLanguage("English")

    commandMap = MasterModule.CommandConfigurationLoader.loadConfig(COMMAND_CONFIG_PATH)
    commands = commandMap.keys()
    try:
        asr.setVocabulary(commands, True)
    except RuntimeError:
        print "Vocabulary have already been set. Omitting."


    commandExecutor = NaoGeneralCommandExecutor()
    commandLinker = GeneralCommandLinker(commandMap)

    # Warning: SpeechRecognizer must be a global variable
    # The name given to the constructor must be the name of the variable
    # It is required by NAOqi
    global SpeechRecognizer
    SpeechRecognizer = SpeechRecognizerModule("SpeechRecognizer")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        SpeechRecognizer.shutdown()
        asr.stop()
        sys.exit(0)


if __name__ == "__main__":
    main()