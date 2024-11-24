from configparser import ConfigParser
import os
from pathlib import Path

class Config:

    #def __init__(self):
    # END __init__(self)

    def load_config(self, section='postgresql'):
        base_path = Path(__file__).parent
        config_filepath = '../../../config/database.ini'        
        file_path = (base_path / config_filepath).resolve()

        if not os.path.isfile(file_path):
            raise FileNotFoundError("File not found: " + file_path)

        parser = ConfigParser()
        parser.read(file_path)

        # get section, default to postgresql
        config = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                config[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, file_path))

        return config
    # END load_config()

# END class Config