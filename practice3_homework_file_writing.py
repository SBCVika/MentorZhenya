from datetime import datetime
import os
import time
import sys

# Set the environment variable
log_file = "log.txt"

def new_logfile():

    # Create a new log file or append to an existing one
    if not os.path.exists(log_file):
        with open(log_file, 'w') as file:
            file.write('--- Log file recreated at {} ---\n'.format(datetime.now()))
            
def generate_new_string():
    while True:
        current_date = datetime.now()
        new_line = "Current date:" + str(current_date)
        yield new_line
        
def append_line(max_lines):
    new_string = generate_new_string()
    with open(log_file, 'a') as log:
        for i in range(max_lines):
            next_line = next(new_string)
            log.writelines(f"New Date: {next_line}\n")
            sys.stdout.flush()

if __name__ == "__main__":
    while True:
        new_logfile()
        new_string = generate_new_string()
        append_line(1000)
        time.sleep(1)
