"""class for merging fb downloaded data"""

import parser.util as util


class Merger:
    def __init__(self, path):
        self.path = path

    def merge_files(self):
        self._find_files_to_merge()
        if self._need_unzip:
            self._unzip_files()

    def _find_files_to_merge(self):

        self.files = util.get_directories_in_directory(self.path)
        if len(self.files) == 0:
            self.files = util.get_files_in_directory(self.path)

        for file in self.files:
            if file.suffix == '.zip':
                self._need_unzip = True
                return

        self._need_unzip = False

    def _unzip_files(self):
        for file in self.files:
            util.unzip_file(
                zip_path=file,
                dest_path=file.parent / 'data'
            )

    def _delete_zip_files(self):
        for file in self.files:
            util.delete_file(file)
