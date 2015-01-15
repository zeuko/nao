__author__ = 'Patrycja'

from MasterModule.Errors import CommandNotFoundError
from TextToCommand.CommandLinker import CommandLinker


class GeneralCommandLinker(CommandLinker):
    """ Receives string transcript of recognized command, and returns proper Command implementation.
        Command linker stores dictionary, mapping transcripts to Command implementations.

    """
    def __init__(self, commands):
        self.commands = commands

    def getCommand(self, text):
        try:
            command = self.commands[text]
        except KeyError:
            raise CommandNotFoundError
        return command

