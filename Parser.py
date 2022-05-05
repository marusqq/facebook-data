"""Parser class for parsing messages"""
import util


class Parser:
    def __init__(self, path):
        self.path = util.check_if_facebook_data_path_is_okay(path)
        self.split_messenger_groups()

    def split_messenger_groups(self):
        print(self.path)
        pass


