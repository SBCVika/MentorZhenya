from datetime import datetime
import os
import time
import sys

# Set the environment variable
log_file = "log.txt"
MAX_LINES_PER_CYCLE = 512

def main():
    # Create a new log file or append to an existing one
    if not os.path.exists(log_file):
        with open(log_file, 'w') as file:
            file.write('--- Log file recreated at {} ---\n'.format(datetime.now()))

while True:  # Repeat indefinitely
    # Run the main logic
    main()
    # Generator for logs
    def add_string():
        while True:
            current_date = datetime.now()
            new_line = "Current date:" + str(current_date)
            yield new_line

    new_string = add_string()

    with open(log_file, 'a') as log:
        for i in range(MAX_LINES_PER_CYCLE):
            next_line = next(new_string)
            log.writelines(f"New Date: {next_line}\n")
            sys.stdout.flush()
            time.sleep(1)
    # Rename the log file to .old
    new_file_name = log_file + '.old'
    if os.path.exists(log_file):
        os.rename(log_file, new_file_name)