#!/usr/bin/env python3

from sys import argv, exit
from os import walk

# Check for correct number of paramteres.
if len(argv) != 4:
    exit("Error! Incorrect number of parameters.")

to_replace = str(argv[1])
replacement = str(argv[2])
dir_path = str(argv[3])

# Work on files recursively.
for (dir_path, dir_names, file_names) in walk(dir_path):
    for file in file_names:
        file_path = "{}\{}".format(dir_path, file)

        try:
            # Open file and read contents.
            with open(file_path, 'r') as fh:
                file_data = fh.read()
        
            # Replace string in file content.
            new_data = file_data.replace(to_replace, replacement)

            # Open file again and replace content with the edited one.
            with open(file_path, 'w') as fh:
                fh.write(new_data)

        except Exception as e:
            exit("Error! File: {}\n{}".format(file, e))