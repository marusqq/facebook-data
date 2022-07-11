"""class for merging fb downloaded data"""
from parser.logger import logger
import parser.util as util


# make sure all paths are correct after merging
class DataUnzipper:
    def __init__(self, path):
        self.unzipped_paths = []
        self.files_to_unzip = []
        self.path = path
        self.read_files_to_unzip()
        self.unzip_files()

    def read_files_to_unzip(self):
        for time_period_folder in util.get_directories_in_directory(self.path):
            files_in_time_period_folder = util.get_files_in_directory(time_period_folder)
            logger.info(msg=f"files in {time_period_folder}: {files_in_time_period_folder}")
            for period_file in files_in_time_period_folder:
                logger.info(f'is this file a zip? {period_file}')
                if util.check_extension(period_file, '.zip'):
                    self.files_to_unzip.append(period_file)

    def check_path_correct(self):
        if not util.check_if_facebook_data_path_is_okay(self.path):
            raise ValueError(f'#1 Bad facebook data path specified. Path: {self.path}')

    def unzip_files(self):
        util.unzip_files(files_to_unzip=self.files_to_unzip)