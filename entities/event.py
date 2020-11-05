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

    async def populate_from_db(self, event_id: str = ''):
        if not event_id:
            event_id = self.id

        async with self.__database:
            document = await self.__database.find_one({'id': event_id})
            self.__populate_properties(dict(document))

    def __populate_properties(self, data: dict):
        self.attendees = data['attendees'] if 'attendees' in data else []
        self.channel = data['channel'] if 'channel' in data else ''
        self.date = data['date'] if 'date' in data else ''
        self.description = data['description'] if 'description' in data else ''
        self.end_time = data['end_time'] if 'end_time' in data else ''
        self.presenter_id = data['presenter_id'] if 'presenter_id' in data else ''
        self.start_time = data['start_time'] if 'start_time' in data else ''
        self.time_zone = data['time_zone'] if 'time_zone' in data else ''
        self.title = data['title'] if 'title' in data else ''
        self.type = data['type'] if 'type' in data else ''

    @property
    def create_payload(self):
        return {
            'id': self.id,
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
