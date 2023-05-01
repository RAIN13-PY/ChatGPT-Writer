import configparser
from makeDirectories import checkIfConfigFileIsCreated
wait_b_s = 5
interval_b_c_m = 0.1
interval_b_c_ma = 0.3
if checkIfConfigFileIsCreated == True:
    config = configparser.ConfigParser()
    config.read_file(open(r'config.txt'))
    wait_b_s = config.get('Main Config', 'wait_before_start')
    interval_b_c_m = config.get('Main Config', 'interval_between_character_min')
    interval_b_c_ma = config.get('Main Config', 'interval_between_character_max')
    #[Main Config]
    #wait_before_start = 5 # time in seconds
    #interval_between_character_min = 0.1
    #interval_between_character_max = 0.3
    #use_default_config = false