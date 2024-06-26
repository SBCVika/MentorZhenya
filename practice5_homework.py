from datetime import datetime
import os
import time
from argparse import ArgumentParser

class TooLargeContent(Exception):
    pass


def except_file_errors(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except FileNotFoundError as e:
                print(f"Error: File '{filename}' not found. Please run writer first to create this file {e}")
                raise e
            except PermissionError as e:
                print(f"Error: Permission denied for file '{filename}'. Please add permissions {e}")
                raise e
            except Exception as e:
                print(f"Error: An unexpected error occurred while reading file '{filename}': {e}")
                raise e
        return wrapper
    return decorator


def get_reader(log_file):
    current_pos = 0

    @except_file_errors(log_file)
    def read_next():
        with open(log_file, 'r') as file:
            nonlocal current_pos
            file.seek(current_pos, os.SEEK_SET)
            content = file.read()
            current_pos = file.tell()
            return content

    return read_next


def get_writer(output_file):
    @except_file_errors(output_file)
    def write_data(data_to_write):
        with open(output_file, 'a') as file:
            file.write(data_to_write)
            print("Data written to", output_file)
    return write_data


def print_lines(content):
    if len(content) > 1 << 32:
        raise TooLargeContent()
    lines = content.splitlines(keepends=True)
    for line in lines:
        print(line)


if __name__ == '__main__':
    parser = ArgumentParser(description="Reader/Writer")
    parser.add_argument('mode', type=int, choices=[0, 1], help='0 - reader; 1 - writer')
    parser.add_argument('filename', type=str, help='Filename')
    args = parser.parse_args()

    if args.mode == 0:
        read_func = get_reader(args.filename)
        while True:
            try:
                content = read_func()
                print_lines(content)
            except TooLargeContent:
                print('Too large. Skip.')
            time.sleep(1)
    elif args.mode == 1:
        writer = get_writer(args.filename)
        while True:
            current_date = datetime.now()
            new_line = "Current date:" + str(current_date) + "\n"
            writer(new_line)
            time.sleep(1)



