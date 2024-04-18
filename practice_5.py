"""
 seek(offset, whence=os.SEEK_SET, /)

    Change the stream position to the given byte offset, interpreted relative to the position indicated by whence, and return the new absolute position. Values for whence are:

        os.SEEK_SET or 0 – start of the stream (the default); offset should be zero or positive

        os.SEEK_CUR or 1 – current stream position; offset may be negative

        os.SEEK_END or 2 – end of the stream; offset is usually negative

"""
import os
from math import ceil
from time import sleep


class TooLargeContent(Exception):
    pass

# Example of closure
def get_reader(log_file):
    current_pos = 0

    def read_next():
        with open(log_file, 'r') as file:
            nonlocal current_pos
            file.seek(current_pos, os.SEEK_SET)
            content = file.read()
            current_pos = file.tell()
            return content
    return read_next


def print_lines(content):
    """
    Reads next chunk of file , splits to lines and prints them out
    :param log_file: str: filenname
    :return: None
    """
    if len(content) > 1<<32:
        raise TooLargeContent()
    lines = content.splitlines(keepends=True)
    for line in lines:
        print(line)

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: func() missing 1 required positional argument: 'b'


# KeyError - dict doesn't have key
# ValueError - int('hello')
# RuntimeError - unexpected behavior ()
# MemoryError - memory overflow [45] * 1000000000000000000000000000000000000
# TypeError - def func(a,b)          func(1)
# KeyboardInterrupt - Ctrl + C
# OSError - when file doesn't exists
# ZeroDivisionError


# n = 5

# ZeroDivisionError
# OSError
# FileNotFoundError
# try:
#     a = ceil(1/n * 10)
#     file = open(f'file{a}.txt', 'r')
# except ZeroDivisionError as exc:
#     print('Zero division', type(exc))
# except (OSError, ValueError) as exc:
#     print('Os error', type(exc))
# except Exception as e:
#     print('Any other exception', e)




if __name__ == '__main__':
    # ArgumentParser

    read_func = get_reader('log.txt')

    while True:

        try:
            content = read_func()
            print_lines(content)
        except TooLargeContent as exc:
            print('Too large. skip')

        sleep(1)
