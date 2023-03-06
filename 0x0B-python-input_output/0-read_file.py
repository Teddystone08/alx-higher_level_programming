#!/usr/bin/python3
"""function read file"""


def read_file(filename=""):
    """function read"""

    with open(filename, "f", encoding="UTF-8") as f:
        for line in file:
            print(line, end="")
