#!/usr/bin/python3
"""module function append"""


def append_write(filename="", text=""):
    """function append"""

    with open(filename, "a", encoding="UTF-8") as file:

        return f.write(text)
