"""class for messages"""
import util


class Message:
    def __init__(self, content, sender, timestamp,
                 message_type, is_unsent, is_taken_down,
                 bumped_message, in_group, photos=None, gifs=None):
        self.sender = sender
        self.content = content
        self.timestamp = timestamp
        self.message_type = message_type
        self.is_unsent = is_unsent
        self.is_taken_down = is_taken_down
        self.bumped_message = bumped_message
        self.in_group = in_group

        self.photos = photos if photos is not None else None
        self.gifs = gifs if gifs is not None else None

