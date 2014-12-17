__author__ = 'Patrycja'


from TextToCommand.CommandLinker import CommandLinker


class GeneralCommandLinker(CommandLinker):
    def __init__(self):
        super(MockCommandLinker, self).__init__()
        self.commandsMap = {"Something has been said": "hello", "go": "go"}

    def getCommand(self, text):
        if text in self.commandsMap:
            return self.commandsMap.get(text)
        else:
            return None