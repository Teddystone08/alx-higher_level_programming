#!/usr/bin/python3
"""Module write method"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
