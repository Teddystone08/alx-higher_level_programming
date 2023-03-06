#!/usr/bin/python3
def red_file(filename=""):
    with open(filename, "f", encoding="UTF-8") as f:
        print(f.read(), end="")
