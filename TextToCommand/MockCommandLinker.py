from TextToCommand.CommandLinker import CommandLinker


class MockCommandLinker(CommandLinker):
    """ Mock command linker created for testing purpose.

    """
    def __init__(self):
        super(MockCommandLinker, self).__init__()
        self.commandsMap = {"Something has been said": "hello", "go": "go"}

    def getCommand(self, text):
        if text in self.commandsMap:
            return self.commandsMap.get(text)
        else:
            return None