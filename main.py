""" ./main.py """
import os

from bots import CalendarTron
from connectors import Configuration


if __name__ == '__main__':
    config_file = os.path.abspath(os.curdir + os.path.normpath('/config.json'))
    config = Configuration(config_file)

    calendartron = CalendarTron(config)
    calendartron.transform_and_roll_out()
