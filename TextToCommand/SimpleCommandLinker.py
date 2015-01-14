from TextToCommand.CommandLinker import CommandLinker
from TextToCommand.Errors import CommandNotFoundError
from MasterModule.Configuration import commands


class SimpleCommandLinker(CommandLinker):
    def getCommand(self, text):
        if text in commands:
            return text
        else:
            raise CommandNotFoundError(text)