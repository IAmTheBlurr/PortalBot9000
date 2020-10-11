""" ./entities/calendartron.py """
from discord import Client as DiscordClient
from discord import Message

from connectors import Configuration
from entities import Event


class CalendarTron(DiscordClient):
    def __init__(self, config: Configuration):
        super().__init__()
        self.events = []
        self.__config = config

    @property
    def __available_commands(self) -> dict:
        return {
            '!create-event': self.__create_event,
            '!show-events': self.__show_events
        }

    async def __create_event(self, message: Message, *args):
        new_event = Event(*args)
        # await new_event.create()
        self.events.append(new_event)
        await message.channel.send(f'Created event: {new_event.title}')

    @staticmethod
    async def __show_events(message: Message, *args):
        await message.channel.send('Here are the events coming up for the following fortnight')

    async def on_message(self, message: Message):
        # Ignore messages which don't start with the command prefix
        if not message.content.startswith(self.__config.command_prefix):
            return

        command_args = message.content.split(' ')
        command = command_args.pop(0)

        # Ignore commands which aren't registered in our available command list
        if command not in self.__available_commands.keys():
            return

        await self.__available_commands[command](message, command_args)

    @staticmethod
    async def on_ready():
        print(f'I am CalendarTron.  I fight for the users.  Never fear, I is here.')

    def transform_and_roll_out(self):
        self.run(self.__config.bot_token)
