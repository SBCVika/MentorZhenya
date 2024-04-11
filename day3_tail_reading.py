import sys
import time

log_file = "log.txt"
last_position = 0

with open(log_file, 'r') as file:
    file_content = file.read()
    print(file_content)
    last_position = file.tell()

while True:
    with open(log_file, 'r') as file:
        # Move the file pointer to the last position
        file.seek(last_position)

        # Read the lines from the last position to the end of the file
        current_content = file.read()

        if current_content != file_content:
            print("File updated:")
            file.seek(last_position)  # Move the file pointer back to the last position
            updated_lines = file.readlines()
            updated_lines = current_content.splitlines()  # Split content into separate lines
            for line in updated_lines:
                print(line)  # Print each updated line
            file_content = current_content

            # Update the last position to the current position
            last_position = file.tell()
            sys.stdout.flush()
    time.sleep(1)