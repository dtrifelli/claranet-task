from sys import argv, exit
from os import walk

if len(argv) != 4:
    exit("Error! Incorrect number of parameters.")

to_replace = str(argv[1])
replacement = str(argv[2])
dir_path = str(argv[3])

for (dir_path, dir_names, file_names) in walk(dir_path):
    for file in file_names:
        file_path = "{}\{}".format(dir_path, file)

        try:
            with open(file_path, 'r') as fh:
                file_data = fh.read()
        
            new_data = file_data.replace(to_replace, replacement)

            with open(file_path, 'w') as fh:
                fh.write(new_data)

        except Exception as e:
            exit("Error! File: {}\n{}".format(file, e))