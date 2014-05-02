from VoiceToText.SpeechRecognizer import SpeechRecognizer


class MockSpeechRecognizer(SpeechRecognizer):
    def registerCallback(self, onRecognizedText):
        self.callback = onRecognizedText

    def stopRecognizing(self):
        self.callback = None

    def startRecognizing(self):
        self.callback("turn left")