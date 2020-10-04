import os

from configurator import Configurator


class TestConfigurator(object):
    def test_class_init_properties(self):
        config = Configurator(os.path.abspath(os.curdir + os.path.normpath('/files/config.json')))
        assert config.client_id == '01234'
        assert config.client_secret == '56789'
        assert config.command_prefix == '$'
        assert config.bot_token == 'abc'
        assert config.database_url == 'localhost'
        assert config.database_port == '27017'
