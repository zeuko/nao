from ExecutorModule.CommandExecutor import CommandExecutor


class MockCommandExecutor(CommandExecutor):
    """ Mock executor for testing purpose.

    """
    def executeCommand(self, command):
        if command == "hello":
            print "Nao says hello"
        elif command == "go":
            print "Nao goes forward"
        else:
            print "Nao does nothing"