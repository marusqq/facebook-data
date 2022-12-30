# -*- coding: UTF-8 -*-
__author__ = "Marius Pozniakovas"
__email__ = "pozniakovui@gmail.com"

# from parser.logger import logger
# from parser import util

"""class used to find, parse, analyze Messages of facebook data"""


class FacebookMessageInvestigator:
    def __init__(self, parse_path):
        self.parse_path = parse_path
        print('333')

    def _find_message_folders(self):
        print("_find_message_folders")
        print(util.get_directories_in_directory(self.parse_path))
        return 'gg'

    def parse(self):
        pass
        # find all folders containing 'messages' folder in path
        self.parse_message_folders = self._find_message_folders()


# if __name__ == '__main__':
print('?')
path = "C:/Users/marius.pozniakovas/Desktop/marus/facebook-data/data/may22_2020-may22_2021/unzipped_data/"

message_investigator = FacebookMessageInvestigator(path)
message_investigator.parse()
