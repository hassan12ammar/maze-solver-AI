from typing import Tuple, Union


def latter_indexing(l:str, file_path) -> Union[Tuple[int, int], None]: # Tuple[int, int] | None
    """
    takes: l as latter
    return its possition on maze (column & row)
    """
    with open(file_path, 'r+') as file:
        file_by_lines = file.readlines()

    for column, line in enumerate(file_by_lines):
        for row, latter in enumerate(line):
            if latter == l:
                return column, row




