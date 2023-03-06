#!/usr/bin/python3
"""Module write method"""


def write_file(filename="", text=""):
    """function write file"""

    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)
        return len(text)
