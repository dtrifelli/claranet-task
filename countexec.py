from sys import argv, exit
from os import walk
import re

if len(argv) != 2:
    exit("Error! Incorrect number of parameters.")

path = str(argv[1])

enum_scripts = dict()

for (dir_path, dir_names, file_names) in walk(path):
    for file in file_names:
        file_path = "{}/{}".format(dir_path, file)
        try:
            with open(file_path, 'r') as fh:
                line = str()
                while not line:
                    line = fh.readline().strip()
                if re.findall("^#!", line):
                    enum_scripts[line] = 1 if line not in enum_scripts else enum_scripts[line]+1
        except Exception as e:
            print("Warning! Error on file: {}\n{}".format(file_path, e))

for key, value in enum_scripts.items():
    print("{} {}".format(value, key))