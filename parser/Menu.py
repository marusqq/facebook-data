"""class for menu workflow"""
import os

import parser.util as util
from parser.logger import logger

from parser.DataUnzipper import DataUnzipper
from parser.Analyzer import Analyzer

from consolemenu import *
from consolemenu.items import *


class Menu:
    def menu(self, mode='main'):
        if mode == 'main':
            menu = ConsoleMenu("Main menu")
            start = FunctionItem(function=self.analysis, text="Start analyzing")
            settings = FunctionItem(function=self.menu, args=['analyzer_settings'], text="Settings")

            menu.append_item(start)
            menu.append_item(settings)
            menu.show()
            input()

        elif mode == 'analyzer_settings':
            menu = ConsoleMenu("Setup analyzer")
            menu.show()

        else:
            self.menu()

    def analysis(self):

        fb_data_path = os.getcwd() + '/data/'
        data_unzipper = DataUnzipper(path=fb_data_path)
        data_unzipper.unzip_files()

        # Ask for settings
        analyzer = Analyzer('settings.json', data_unzipper.get_ready_zips())
        analyzer.start_analysis()
