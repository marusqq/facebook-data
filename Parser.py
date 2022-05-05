"""Parser class for parsing messages"""
import util


class Parser:
    def __init__(self, path):
        self.inbox_path = util.check_if_facebook_data_path_is_okay(path)
        self.messenger_group_archives = self.set_messenger_groups()
        self.unrar_groups()
        self.read_messenger_groups()

    def set_messenger_groups(self):
        return [x for x in self.inbox_path.iterdir() if x.is_file()]

    def read_messenger_groups(self):
        pass

    def parse_group_messages(self, group):
        pass

    def unrar_groups(self):
        for archive in self.messenger_group_archives:
            util.unrar_file(archive)
        pass

