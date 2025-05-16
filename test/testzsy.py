from appdirs import AppDirs
import os


print()
config_file = os.path.join(AppDirs('trader').user_config_dir, 'config.ini')
print(config_file)