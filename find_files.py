# Write a find_files function that will act like the Unix find utility.
#
# def find_files(root_dir, pattern='.*', min_size=0):
#     ...
#
# Where:
#
#     root_dir is where to start from
#     pattern is a regular expression that should match the file
#     min_size is the minimal size of the file
#
# The function should return only files (not directories) and one file at a time (generator).
#
# Hints:
#
#     pathlib.Path
#     re module

from pathlib import Path
import re


def find_files(root_dir, pattern='.*', min_size=0):
    path = Path(root_dir)
    for item in path.glob('**/*'):
        if item.is_file() and item.stat().st_size >= min_size and re.search(pattern, item.name):
            yield item


files = find_files("/home/gasper/work", "[a-z]", 15000000)
print(files)

for file in files:
    print(file)
