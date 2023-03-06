#!/usr/bin/python3
"""function read file"""


def read_file(filename=""):
    """function read"""

    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:
            print(line, end="")
