"""Parser class for parsing messages"""

import util
from Message import Message
from User import User
from MessengerGroup import MessengerGroup


class Parser:
    def __init__(self, path='messages'):
        self.inbox_path = util.check_if_facebook_data_path_is_okay(path)
        self._unrar_and_set_messenger_groups()
        self._get_info_from_messenger_groups()

    # Private methods -----------------------------------------------------------------
    def _unrar_and_set_messenger_groups(self):
        # Get messenger group archive names
        self.messenger_group_archives = [x for x in self.inbox_path.iterdir() if x.is_file()]

        # Unrar them
        for archive in self.messenger_group_archives:
            util.unzip_file(archive)

        # Create MessengerGroup objects
        messenger_groups = []
        for messenger_group in [x for x in self.inbox_path.iterdir() if x.is_dir()]:
            messenger_group = MessengerGroup(
                name=messenger_group.name,
                path=messenger_group.absolute()
            )
            messenger_groups.append(messenger_group)
        self.messenger_groups = messenger_groups

    def _get_info_from_messenger_groups(self):

        # for every messenger group, set possible json parameters to User, MessengerGroup
        for messenger_group in self.messenger_groups:
            with open(messenger_group.message_paths[0]) as json_file:
                json_data = util.load_json_file(json_file)

                # set title
                messenger_group.set_title(json_data['title'])
                # set users
                messenger_group.set_users(json_data['participants'])
                # set threadtype
                messenger_group.set_threadtype(json_data['thread_type'])
                # set is_still_participant
                messenger_group.set_is_still_participant(json_data['is_still_participant'])

                for message in json_data['messages']:
                    try:
                        content = message['content']
                    except ValueError:
                        content = None
                    message_obj = Message(
                        sender=message['sender_name'],
                        timestamp=message['timestamp_ms'],
                        content=content,
                        message_type=message['type']

                    )
                    print(message['timestamp_ms'])
                    print(message['content'])


        return json_data if json_data is not None else None

    # def _read_messenger_group(self, messenger_group, json_data):
    #     for messenger_group in self.messenger_groups:
    #         # messenger_group.print_messenger_group()

    def _get_users_from_group_file(self):
        pass

    # Public methods ------------------------------------------------------------------
