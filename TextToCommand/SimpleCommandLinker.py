from TextToCommand.CommandLinker import CommandLinker
from MasterModule.Errors import CommandNotFoundError
from MasterModule.GeneralConfigurationLoader import commands


class SimpleCommandLinker(CommandLinker):
    def getCommand(self, text):
        if text in commands:
            return text
        else:
            raise CommandNotFoundError(text)