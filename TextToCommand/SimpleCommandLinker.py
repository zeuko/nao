from TextToCommand.CommandLinker import CommandLinker
from TextToCommand.Errors import CommandNotFoundError

text2Command = {"go forward": "go forward",
                "turn left": "turn left",
                "turn right": "turn right"}


class SimpleCommandLinker(CommandLinker):
    def getCommand(self, text):
        if text in text2Command:
            return text2Command.get(text)
        else:
            raise CommandNotFoundError(text)