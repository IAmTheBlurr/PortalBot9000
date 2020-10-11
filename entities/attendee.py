""" ./entities/attendee.py """


class Attendee(object):
    def __init__(self):
        self.events = []
        self.discord_id = ''

    async def attend(self, event_id: str):
        return

    async def notify(self, payload: dict):
        return

    async def show_attending(self):
        return

    async def unattend(self, event_id: str):
        return
