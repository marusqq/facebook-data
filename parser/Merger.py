"""class for merging fb downloaded data"""
from parser.logger import logger
import parser.util as util


class Merger:
    def __init__(self, path):
        self.path = path

    def merge_files(self):
        logger.info("Looking for files to merge")
        self._find_files()
        if self._need_unzip:
            self._unzip_files()
            # self._delete_zip_files()

    def _find_files(self):
        self.files = util.get_files_in_directory(self.path)
        for file in self.files:
            if file.suffix == '.zip':
                self._need_unzip = True
                return

        self._need_unzip = False

    def _unzip_files(self):
        for file in self.files:
            logger.info(f'Unzipping file: {file}, '
                        f'file size: ~{round(util.get_file_size(file) / (1024 * 1024),3)} MB')
            util.unzip_file(
                zip_path=file,
                dest_path=file.parent / 'data'
            )

    def _delete_zip_files(self):
        for file in self.files:
            util.delete_file(file)
