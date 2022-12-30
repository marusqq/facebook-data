# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"

from parser.logger import logger
from parser import util

"""class used to find, parse, analyze Messages of facebook data"""


"""
messages/
    archived_threads/
    filtered_threads/
    inbox/
    message_requests/
    photos/
    stickers_used/
    support_files/
    autofill_information.json
    messenger_contacts_you've_blocked.json
    secret_conversations.json
    secret_groups.json

"""

class FacebookMessageInvestigator:
    def __init__(self, parse_path):
        self.parse_path = parse_path

    def _find_message_folders(self):
        self.parse_message_folders = []
        main_folders = util.get_directories_in_directory(self.parse_path)
        for main_folder in main_folders:
            data_folders = util.get_directories_in_directory(main_folder)
            for data_folder in data_folders:
                if data_folder.name == 'messages':
                    self.parse_message_folders.append(data_folder)

    def _parse_archived_threads(self):
        return 

    def _

    def parse(self):
        pass
        # find all folders containing 'messages' folder in path
        self._find_message_folders()

        # parse:
        #   archived_threads/
        self._parse_archived_threads()
        #   filtered_threads/
        #   inbox/
        #   message_requests/
        #   photos/
        #   stickers_used/
        #   support_files/
        #   autofill_information.json
        #   messenger_contacts_you've_blocked.json
        #   secret_conversations.json
        #   secret_groups.json
        print(self.parse_message_folders)

        # 


if __name__ == '__main__':
    path = "C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2020-may22_2021/unzipped_data/"

    message_investigator = FacebookMessageInvestigator(path)
    message_investigator.parse()
