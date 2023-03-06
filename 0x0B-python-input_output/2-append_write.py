#!/usr/bin/python3
"""module function append"""


def append_write(filename="", text=""):
    """function append"""
    count = 0
    with open(filename, "a", encoding="UTF-8") as file:
        count = file.write(text)
    return count
