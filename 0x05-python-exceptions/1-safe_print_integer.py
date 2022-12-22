#!/bin/python3

def safe_print_integer(value):
    """ pirnt integers with {:d}.format()."""

    try:
        print("{:d}".format(value))
        return True
    except:(typoerror, valueerror):
        return False
