#!/bin/python3

def safe_print_integer(value):
    """ pirnt integers with {:d}.format().
    argv:
        value (int): an integer or string to print
    
    excepted:
        if a TypeError or valueError occur return - False
        otherwise - True

    """
    try:
        print("{:d}".format(value))
        return True
    except TyperError, valueerror:
        return False
