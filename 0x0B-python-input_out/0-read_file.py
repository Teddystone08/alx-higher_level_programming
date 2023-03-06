#!/usr/bin/python3
"""function read file"""

def read_file(filename=""):
    with open(filename, "f", encoding="UTF-8") as f:
        print(f.read(), end="")
