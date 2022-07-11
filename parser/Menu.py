"""class for menu workflow"""
import os
import parser.logger as logger
import parser.util as util
from parser.logger import logger
from parser.Merger import DataUnzipper


class Menu:
    def __init__(self):
        self.run()

    def run(self):
        util.clear_screen()
        waiting_in_menu = True
        while waiting_in_menu:
            # choice = self.give_choice()
            choice = "2"
            if choice == "1":
                waiting_in_menu = False
                self._parse_data()
            elif choice == "2":
                waiting_in_menu = False
                self._merge_files()
        logger.info("Press any key to return to menu (q to quit)")
        console_input = input()
        if console_input.lower() == 'q':
            return
        self.run()

    @staticmethod
    def give_choice():
        logger.info(msg="------------------")
        logger.info(msg="Choose an option:")
        logger.info(msg="[1] Parse data")
        logger.info(msg="[2] Merge downloaded files")
        choice = input('')
        return choice

    def give_choice_2(self):
        pass

    def _parse_data(self):

        pass

    def _merge_files(self):
        util.clear_screen()

        # logger.info(msg="Enter a path to merge downloaded facebook data files:")
        # fb_data_path = input('Path: ')
        fb_data_path = os.getcwd() + '/data/'

        merger = DataUnzipper(path=fb_data_path)
        logger.info(merger.unzipped_paths)
        # merger.merge_files()
