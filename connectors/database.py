""" ./connectors/database.py """
from pymongo import MongoClient
from pymongo.collection import Cursor, InsertOneResult

from connectors import Configuration


class Database(MongoClient):
    def __init__(self, config: Configuration, collection: str):
        super().__init__(config.database_url, config.database_port, connect=False)
        self.__database = None
        self.__desired_collection = collection
        self.__collection = None

    async def __aenter__(self):
        self.__database = self.portal_events
        self.__collection = self.__database[self.__desired_collection]

    async def __aexit__(self, exc_type, exc_val, exc_tb_):
        self.close()

    async def find(self, payload: dict) -> Cursor:
        return self.__collection.find(payload)

    async def find_one(self, payload: dict) -> Cursor:
        return self.__collection.find_one(payload)

    async def insert(self, payload: dict) -> InsertOneResult:
        return self.__collection.insert_one(payload)
