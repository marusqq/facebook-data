# -*- coding: utf-8 -*-
import json
from datetime import datetime
from json import JSONDecodeError
from pathlib import Path
from typing import List

from alive_progress import alive_bar, alive_it

from parser.logger import logger
import pyunpack
import os


# --------------------------------------------------------------------------------------------------------------------
# Directory commands

def get_directory_size(path='.'):
    total = 0
    for entry in os.scandir(path):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            total += get_directory_size(entry.path)
    return total


def get_directories_in_directory(path) -> List[Path]:
    _path = Path(path)
    return [x for x in _path.iterdir() if x.is_dir()]


def create_directory(directory_name):
    os.mkdir(directory_name)


# --------------------------------------------------------------------------------------------------------------------
# File commands

def check_extension(file_name, extension) -> bool:
    return file_name.suffix == extension


def load_json_file(filepath):
    if type(filepath).__name__ in ['str', Path, 'WindowsPath', 'UnixPath']:
        filepath = open(filepath, 'r')

    data = json.load(filepath)
    return data


def unzip_file(zip_path, dest_path):
    # Unzip part
    if not check_if_directory(dest_path):
        create_directory(dest_path)
    try:
        pyunpack.Archive(zip_path).extractall(dest_path)
    except pyunpack.PatoolError as e:
        quit(f'Patool error. Probably need to install an unzip tool. {e}')

    # Check unzipped result
    if not check_if_directory(dest_path):
        return False, None

    return True, dest_path


def delete_file(file_path) -> bool:
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False


def get_file_size(path):
    file_stats = os.stat(path)
    return file_stats.st_size


def get_files_in_directory(path) -> List[Path]:
    _path = Path(path)
    return [x for x in _path.iterdir() if x.is_file()]


def unzip_files(files_to_unzip):
    unzipped_files_paths = []
    logger.info('Unzipping files')
    for file_to_unzip in alive_it(files_to_unzip):
        unzip_destination = file_to_unzip.parent / 'unzipped_data'
        if not check_if_directory(unzip_destination):
            create_directory(unzip_destination)

        unzip_success, unzip_path = unzip_file(
            zip_path=file_to_unzip,
            dest_path=unzip_destination
        )

        unzipped_files_paths.append(unzip_success)

    return unzipped_files_paths


# ---------------
# Path commands

def check_if_file_in_path(path) -> str:
    if not check_if_file(path):
        raise ValueError(f'#2 get_file_from_path() received path with no file in path. Path: {path}')
    return str(path.name)


def check_if_directory(path) -> bool:
    return path.is_dir()


def check_if_file(path) -> bool:
    return path.is_file()


def check_if_facebook_data_path_is_okay(path) -> Path:
    """
    Checks inputted_path for path/inbox dir,
    then checks for path/inbox having subdirectories
    Returns path on success, raises SystemExit exception on failure
    :param path: inputted path
    :return: path: checked path
    :raises: ValueError: on failure
    """

    _path = Path(path)

    inbox = _path / 'inbox'
    if not inbox.is_dir():
        raise ValueError(f'#3 Bad path for facebook data in directory: "{path}"')

    dirs = [x for x in _path.iterdir() if x.is_dir()]
    if not len(dirs):
        raise ValueError(f'#4 No directories found in directory: "{inbox}"')

    return inbox


# --------------------------------------------------------------------------------------------------------------------
# Misc commands

# --------------------------------------------------------
# Date:
def get_datetime_from_string(string_date):
    year = string_date.split('-')[0]
    month = string_date.split('-')[1]
    day = string_date.split('-')[2]

    datetime_object = datetime.strptime(month, "%b")
    month_number = datetime_object.month

    string_date = year + '-' + str(month_number) + '-' + day

    return datetime.strptime(string_date, "%Y-%m-%d").date()


def get_difference_between_datetimes(datetime1, datetime2=datetime.now(), interval="default"):
    duration = datetime1 - datetime2
    duration_in_s = duration.total_seconds()

    def years():
        return divmod(duration_in_s, 31536000)  # Seconds in a year=31536000.

    def days(seconds=None):
        return divmod(seconds if seconds is not None else duration_in_s, 86400)  # Seconds in a day = 86400

    def hours(seconds=None):
        return divmod(seconds if seconds is not None else duration_in_s, 3600)  # Seconds in an hour = 3600

    def minutes(seconds=None):
        return divmod(seconds if seconds is not None else duration_in_s, 60)  # Seconds in a minute = 60

    def seconds(seconds=None):
        if seconds != None:
            return divmod(seconds, 1)
        return duration_in_s

    def total_duration():
        y = years()
        d = days(y[1])  # Use remainder to calculate next variable
        h = hours(d[1])
        m = minutes(h[1])
        s = seconds(m[1])

        return "Time between dates: {} years, {} days, {} hours, {} minutes and {} seconds".format(int(y[0]), int(d[0]),
                                                                                                   int(h[0]), int(m[0]),
                                                                                                   int(s[0]))

    return {
        'years': int(years()[0]),
        'days': int(days()[0]),
        'hours': int(hours()[0]),
        'minutes': int(minutes()[0]),
        'seconds': int(seconds()),
        'default': total_duration()
    }[interval]


def get_current_time_and_date_for_path():
    return datetime.now().strftime("%Y_%m_%d-%I_%M_%S")


def get_datetime_from_timestamp(timestamp):
    return datetime.fromtimestamp(float(timestamp))


# --------------------------------------------------------
# Convertions

# ---------------------
# File size
def convert_bytes_to_megabytes(bytes_to_convert, string_format=False):
    megabytes = round(bytes_to_convert / 1000000, 2)
    if not string_format:
        return megabytes
    return str(megabytes) + 'MB'


def clear_screen():
    os.system('cls')


# ---------------------
# Ascii
def get_ascii_string(string):
    decoded_string = string.encode('latin1').decode('utf8')
    if string != decoded_string:
        return decoded_string

    else:
        return string
