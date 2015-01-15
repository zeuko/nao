from naoqi import ALModule, ALProxy, ALBroker
from VoiceToText.SpeechRecognizer import SpeechRecognizer

Recognizer = None
memory = None
callback = None
asr = None
myBroker = None

class RecognizerModule(ALModule):
    """ Missing pydoc

    """
    def __init__(self, name):
        ALModule.__init__(self, name)

        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("WordRecognized", "Recognizer", "onWordRecognized")

    def onWordRecognized(self, key, value, message):
        """invokes callback with recognized word with highest probability"""
        callback(value[0])

    def stopWorking(self):
        global memory
        memory.unsubscribeToEvent("WordRecognized", "Recognizer")


class NaoRecognizer(SpeechRecognizer):
    def registerCallback(self, onRecognizedText):
        global callback
        callback = onRecognizedText

    def stopRecognizing(self):
        global Recognizer
        Recognizer.stopWorking()

    def startRecognizing(self):

        global asr
        asr = ALProxy("ALSpeechRecognition")
        asr.setLanguage("English")

        global Recognizer
        Recognizer = RecognizerModule("Recognizer")