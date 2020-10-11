""" ./entities/event.py """
import random
import string

from connectors import Configuration, Database


class Event(object):
    def __init__(self, config: Configuration, payload: list = None):
        self.__database = Database(config, 'events')

        self.id = self.__create_id()
        self.title = ''
        self.description = ''
        self.channel = ''
        self.start_time = ''
        self.end_time = ''
        self.date = ''
        self.attendees = []
        self.presenter_id = ''
        self.type = ''
        self.time_zone = ''

        if payload:
            self.__read_payload(payload)

    @staticmethod
    def __create_id() -> str:
        letters = ''.join([random.choice(string.ascii_uppercase) for _ in range(3)])
        numbers = ''.join([random.choice(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']) for _ in range(3)])
        return letters + numbers

    def __read_payload(self, args: list) -> None:
        self.type = args[0]
        self.title = args[1]

    @property
    def create_payload(self):
        return {
            'title': self.title,
            'type': self.type
        }

    @property
    async def attendant_count(self):
        return

    async def cancel(self):
        return

    async def create(self):
        async with self.__database:
            await self.__database.insert(self.create_payload)

    async def notify_attendees(self):
        return

    async def notify_channel(self):
        return

    async def update(self, payload: dict):
        return
