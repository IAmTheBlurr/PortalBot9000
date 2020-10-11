""" ./connectors/database.py """
from pymongo import MongoClient

from connectors import Configuration
from entities import Event


class Database(MongoClient):
    def __init__(self, config: Configuration):
        super().__init__(config.database_url, config.database_port)

    def __enter__(self):
        return

    def __exit__(self, *_):
        return

    def connect(self):
        return

    def disconnect(self):
        return

    def update_event(self, event: Event):
        return

    def write_new_event(self, event: Event):
        return
