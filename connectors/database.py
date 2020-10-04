from pymongo import MongoClient

from configurator import Configurator


class Database(MongoClient):
    def __init__(self, config: Configurator):
        super().__init__(config.database_url, config.database_port)
