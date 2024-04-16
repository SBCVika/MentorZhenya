import sys
import time

log_file = "log.txt"
last_position = 0

def content_pos(log_file, last_position=0):
    with open(log_file, 'r') as file:
        file.seek(last_position)
        file_content = file.read()
        last_position = file.tell()
        content_position = (file_content, last_position)
        return content_position

def read_update(log_file, content_position):
    with open(log_file, 'r') as file:
        file.seek(content_position[1])
        current_content = file.read()

        if current_content != content_position[0]:
            new_lines = current_content.splitlines()
            old_lines = content_position[0].splitlines()
            # Find and print new lines
            new_content = ""
            for line in new_lines:
                if line not in old_lines:
                    print(line)
                    new_content += line + "\n"

            last_position = file.tell()
            content_position = (current_content, last_position)
        return content_position

if __name__ == "__main__":
    while True:
        content_position = content_pos(log_file)
        content_position = read_update(log_file, content_position)
        time.sleep(1)
