""" ./entities/event.py """
from connectors import Configuration, Database


class Event(object):
    def __init__(self, config: Configuration, payload: list = None):
        self.__database = Database(config, 'events')

        self.id = ''
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
