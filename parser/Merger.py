"""class for merging fb downloaded data"""

import parser.util as util

# Order of merge:
# optional (get zips and upzip them)
#

class Merger:
    def __init__(self, path):
        self.path = path

        print(path)

    def merge_files(self):
        self._find_files_to_merge()


    def _find_files_to_merge(self):
        directories = util.get_directories_in_directory(self.path)
        print(directories)



