from pathlib import Path
import rarfile
import platform


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


def unrar_file(filepath):
    rar_file = rarfile.RarFile(filepath)
    parent_path = filepath.parent
    rar_file.extractall(parent_path / 'extracted' / filepath.stem)
