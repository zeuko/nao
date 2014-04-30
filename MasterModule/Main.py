from CommandExecution.MockCommandExecutor import MockCommandExecutor
from TextToCommand.MockCommandLinker import MockCommandLinker
from VoiceToText.MockSpeechRecognizer import MockSpeechRecognizer


speechRecognizer = MockSpeechRecognizer()
commandLinker = MockCommandLinker()
commandExecutor = MockCommandExecutor()

def textRecognized(text):
    speechRecognizer.stopRecognizing()
    command = commandLinker.getCommand(text)
    if not command:
        print "Command unrecognized"
    else:
        commandExecutor.executeCommand(command)


def main():
    speechRecognizer.registerCallback(textRecognized)
    speechRecognizer.startRecognizing()

main()

