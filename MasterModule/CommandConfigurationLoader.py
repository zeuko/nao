__author__ = 'Patrycja'

from MasterModule.NaoModulesProxy import NaoModules

configuration_proxy = NaoModules()


def initCommandInstance(string_command_name):
    """ Returns instance of Command object from MasterModule.Commands module.
        It requires providing NaoModulesProxy.NaoModules object,
        which contains initialized proxy objects to a few NAO Modules
    """
    module = __import__('MasterModule.Commands.' + string_command_name, fromlist=[string_command_name])
    command_class = getattr(module, string_command_name)
    return command_class(configuration_proxy)


def loadConfig(filename):
    """ Loads configuration from configuration file with name passed as argument.
        Returns map containing initialized Commands (ready for execute() call),
        each one is connected with key representing voice command recognized by NAO.
    """
    config_file = open(filename, 'r')
    command_map = {}
    for line in config_file:
        config = line.split('=')
        string_command = config[0].strip().strip("[]")
        command_class = config[1].strip()
        print string_command
        print command_class
        command_map[string_command] = initCommandInstance(command_class, proxy)
        command_map[string_command].execute()
    return command_map


