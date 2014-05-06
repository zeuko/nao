from TextToCommand.CommandLinker import CommandLinker
from TextToCommand.Errors import CommandNotFoundError

text2Command = ("go forward", "turn left", "turn right", "stop", "stand up", "hello nao", "sit down")


class SimpleCommandLinker(CommandLinker):
    def getCommand(self, text):
        if text in text2Command:
            return text
        else:
            raise CommandNotFoundError(text)