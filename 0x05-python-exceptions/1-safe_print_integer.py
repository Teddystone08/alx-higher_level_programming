#!/bin/python3

def safe_print_integer(value):
    """ pirnt integers with {:d}.format().
    value an integer or string of input

    """
    try:
        print("{:d}".format(value))
        return True
    except valueerror:
        return False
