"""class for menu workflow"""
import os

import parser.util as util
from parser.logger import logger

from parser.DataUnzipper import DataUnzipper
from parser.Analyzer import Analyzer

from consolemenu import *
from consolemenu.items import *


class Menu:
    def __init__(self):
        self.analyzer_settings = {
            'setting1': True,
            'setting2': False,
            'setting3': 3,
            'setting4': 'bam'
        }

    def menu(self, mode='main'):
        if mode == 'main':
            menu = ConsoleMenu("Main menu")
            start = FunctionItem(function=self.start_analyzing, text="Start analyzing")
            settings = FunctionItem(function=self.menu, args=['analyzer_settings'], text="Settings")

            menu.append_item(start)
            menu.append_item(settings)
            menu.show()
            input()

        elif mode == 'analyzer_settings':
            menu = ConsoleMenu("Setup analyzer")
            for setting, value in self.analyzer_settings:
                setting_item = FunctionItem(self._change_analyzer_settings(), args=[setting, not(value)])
                menu.append_item(setting_item)
            menu.show()

        else:
            self.menu()

    def _change_analyzer_settings(self, setting, value):
        self.analyzer_settings[setting] = value

    def start_analyzing(self):
        util.clear_screen()

        fb_data_path = os.getcwd() + '/data/'
        data_unzipper = DataUnzipper(path=fb_data_path)
        data_unzipper.unzip_files()

        # Ask for settings
        # TODO: ask if want to change settings
        # analyzer_settings = self.set_analyzer_settings()
        analyzer = Analyzer('settings.json', data_unzipper.get_ready_zips())

    def set_analyzer_settings(self):
        return