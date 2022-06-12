"""class for menu workflow"""
import logging
import sys


class Logger:
    def __init__(self):
        self.logger = logging.getLogger(name="fb-data")
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s : %(message)s')

        self.config_console_handler()
        self.logger.addHandler(self.console_handler)

    def config_console_handler(self):
        self.console_handler = logging.StreamHandler(sys.stdout)
        self.console_handler.setLevel(logging.DEBUG)
        self.console_handler.setFormatter(self.formatter)

    def get_logger(self):
        return self.logger


logger_obj = Logger()
logger = logger_obj.get_logger()
