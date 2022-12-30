"""class for merging fb downloaded data"""
import parser.util as util
from parser.logger import logger


class DataUnzipper:
    def __init__(self, path):
        self.ready_zips = []
        self.files_to_unzip = []
        self.path = path
        self.read_files_to_unzip()

    def read_files_to_unzip(self):
        for time_period_folder in util.get_directories_in_directory(self.path):
            files_in_time_period_folder = util.get_files_in_directory(time_period_folder)
            zip_size_in_period_folder = 0
            files_to_maybe_unzip = []
            for period_file in files_in_time_period_folder:
                if util.check_extension(period_file, '.zip'):
                    zip_size_in_period_folder = zip_size_in_period_folder + util.get_file_size(period_file)
                    files_to_maybe_unzip.append(period_file)

            # now look for unzipped data and if it is similar in size, dont add files to to unzip
            folders_in_time_period_folder = util.get_directories_in_directory(time_period_folder)

            if not len(folders_in_time_period_folder):
                for file_ in files_to_maybe_unzip:
                    logger.info(file_)
                    self.files_to_unzip.append(file_)

            for folder in folders_in_time_period_folder:
                if util.check_if_directory(folder):
                    if folder.stem == 'unzipped_data':
                        unzipped_folder_size = util.get_directory_size(folder)
                        logger.debug(time_period_folder)
                        zip_size_in_period_folder = \
                            util.convert_bytes_to_megabytes(
                                bytes_to_convert=zip_size_in_period_folder,
                                string_format=False
                            )
                        unzipped_folder_size = \
                            util.convert_bytes_to_megabytes(
                                bytes_to_convert=unzipped_folder_size,
                                string_format=False
                            )
                        logger.debug(f'{zip_size_in_period_folder}mb vs {unzipped_folder_size}mb')
                        zip_diff = zip_size_in_period_folder/unzipped_folder_size

                        for file_ in files_to_maybe_unzip:
                            if zip_diff < 0.5:
                                self.files_to_unzip.append(file_)
                            else:
                                self.ready_zips.append(file_)

    def check_path_correct(self):
        if not util.check_if_facebook_data_path_is_okay(self.path):
            raise ValueError(f'#1 Bad facebook data path specified. Path: {self.path}')

    def unzip_files(self):
        if len(self.files_to_unzip):
            logger.info('Unzipping files....')
            new_ready_paths = util.unzip_files(files_to_unzip=self.files_to_unzip)
            for ready_path in new_ready_paths:
                self.ready_zips.append(ready_path)

    def get_ready_zips(self):
        return self.ready_zips
