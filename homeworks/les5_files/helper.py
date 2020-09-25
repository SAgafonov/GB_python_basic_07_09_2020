import os

dir_name = __file__
path_to_dir_for_file = os.path.dirname(dir_name) + os.path.sep + ".."


def path_maker(file_name: str) -> str:
    """
    Return path to a provided file
    :param file_name:str
    :return: str
    """
    return os.path.join(path_to_dir_for_file, file_name)
