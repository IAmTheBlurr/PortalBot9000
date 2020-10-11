""" ./connectors/configuration.py """
import json
import os


class Configuration(object):
    def __init__(self, file_path: str):
        self.__file_path = file_path
        self.client_id = ''
        self.client_secret = ''
        self.command_prefix = ''
        self.modules = []
        self.bot_token = ''

        self.database_url = ''
        self.database_port = ''

        self.read_file()

    @staticmethod
    def __check_path(file_path: str) -> str:
        if not os.path.isfile(file_path):
            raise IOError('Value provided as a path to the file does not appear to point to a file.  Please provide a full path to a .json file.')

        return file_path

    def read_file(self, file_path: str = '') -> None:
        if not file_path:
            file_path = self.__file_path

        with open(self.__check_path(file_path)) as config:
            data = config.read()

        content = json.loads(data)

        self.client_id = content['discord']['client_id'] if 'client_id' in content['discord'] else ''
        self.client_secret = content['discord']['client_secret'] if 'client_secret' in content['discord']else ''
        self.command_prefix = content['discord']['command_prefix'] if 'command_prefix' in content['discord'] else ''
        self.bot_token = content['discord']['bot_token'] if 'bot_token' in content['discord'] else ''
        self.database_url = content['database']['address'] if 'address' in content['database'] else ''
        self.database_port = content['database']['port'] if 'port' in content['database'] else ''
