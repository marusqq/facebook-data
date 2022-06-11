"""class for menu workflow"""
import logging
import sys
import os
import parser.util as util
from parser.Merger import Merger

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
logger.console_handler = logging.StreamHandler(sys.stdout)
logger.console_handler.setLevel(logging.INFO)
logger.console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))


class Menu:
    def __init__(self):
        # setup logger
        logger.info(msg='Starting parser...')
        self.run()

    def run(self):
        util.clear_screen()
        waiting_in_menu = True
        while waiting_in_menu:
            choice = self.give_choice()
            if choice == "1":
                waiting_in_menu = False
                self._parse_data()
            elif choice == "2":
                waiting_in_menu = False
                self._merge_files()

        logger.warning(msg="Press any key to return to menu (q to quit)")
        console_input = input()
        if console_input.lower() == 'q':
            return
        self.run()

    def give_choice(self):
        logger.warning(msg="------------------")
        logger.warning(msg="Choose an option:")
        logger.warning(msg="[1] Parse data")
        logger.warning(msg="[2] Merge downloaded files")
        choice = input('')
        return choice
        pass

    def _parse_data(self):

        pass

    def _merge_files(self):
        util.clear_screen()
        logger.warning(msg="[2] Merge files")
        logger.warning(msg="Enter a path to merge downloaded facebook data files:")
        # fb_data_path = input('Path: ')
        fb_data_path = os.getcwd() + '/data/may22_2021-may22_2022/'

        merger = Merger(path=fb_data_path)
        merger.merge_files()

        pass
