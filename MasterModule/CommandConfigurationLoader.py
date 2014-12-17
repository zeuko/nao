__author__ = 'Patrycja'

CONFIG_PATH = '../command_config.cfg'

dictionary = []

"""
Returns instance of specific command
"""
def initCommandInstance(stringName):
    module = __import__('MasterModule.Commands.' + stringName, fromlist=[stringName])
    command_class = getattr(module, stringName)
    return command_class()


config_file = open(CONFIG_PATH, 'r')

print config_file
command_map = {}
for line in config_file:
    config = line.split('=')
    string_command = config[0].strip().strip("[]")
    dictionary.append(string_command)
    command_class = config[1].strip()
    print string_command
    print command_class
    command_map[string_command] = initCommandInstance(command_class)
    command_map[string_command]().execute()

