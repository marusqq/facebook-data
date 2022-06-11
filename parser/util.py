import json
from pathlib import Path
from typing import List

import pyunpack
import os


def clear_screen():
    os.system('cls')


def check_if_facebook_data_path_is_okay(path) -> Path:
    """
    Checks inputted_path for path/inbox dir,
    then checks for path/inbox having subdirectories
    Returns path on success, raises SystemExit exception on failure
    :param path: inputted path
    :return: path: checked path
    :raises: SystemExit: on failure
    """

    _path = Path(path)

    inbox = _path / 'inbox'
    if not inbox.is_dir():
        raise SystemExit(f'Bad path for facebook data in directory: "{path}"')

    dirs = [x for x in _path.iterdir() if x.is_dir()]
    if not len(dirs):
        raise SystemExit(f'No directories found in directory: "{inbox}"')

    return inbox


def get_files_in_directory(path) -> List[Path]:
    _path = Path(path)
    return [x for x in _path.iterdir() if x.is_file()]


def get_directories_in_directory(path) -> List[Path]:
    _path = Path(path)
    return [x for x in _path.iterdir() if x.is_dir()]


def create_directory(directory_name):
    os.mkdir(directory_name)


def load_json_file(filepath):
    return json.load(filepath)


def unrar_file(filepath):
    parent_path = filepath.parent
    try:
        pyunpack.Archive(filepath).extractall(parent_path)
    except pyunpack.PatoolError as e:
        quit(f'Patool error. Probably need to install an unzip tool. {e}')


def get_ascii_string(string):
    decoded_string = string.encode('latin1').decode('utf8')
    if string != decoded_string:
        return decoded_string

    else:
        return string
