"""class for messenger groups in facebook data"""
import util
from User import User


class MessengerGroup:
    def __init__(self, name, path, history=None):
        self._format_name(name)
        self._format_paths(path)
        self.history = history if history else []
        # To be set later from file
        self.title = None
        self.users = None

    # Private methods -----------------------------------------------------------------
    def _format_name(self, name):
        if '_' in name:
            name = name.split('_')[0]
        self.name = name

    def _format_paths(self, path):

        self.path = path

        gif_path = path / 'gifs'
        if gif_path.is_dir():
            self.gif_paths = [x for x in gif_path.iterdir() if x.is_file()]
        else:
            self.gif_paths = None

        photos_path = path / 'photos'
        if photos_path.is_dir():
            self.photo_paths = [x for x in photos_path.iterdir() if x.is_file()]
        else:
            self.photo_paths = None

        self.message_paths = [x for x in path.iterdir() if x.is_file()]

    # Public methods ------------------------------------------------------------------
    def set_users(self, users_to_set):
        self.users = []
        for user_to_set in users_to_set:

            user = User(name=util.get_ascii_string(user_to_set['name']))
            self.users.append(user)

    def add_history(self, history):
        self.history.append(history)

    def set_title(self, title):
        self.title = title
