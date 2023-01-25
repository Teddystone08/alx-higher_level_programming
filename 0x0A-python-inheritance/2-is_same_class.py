#!/usr/bin/python3

"""
============================
Module with class Mylist
============================
"""

class Mylist(list):
    """Class with print_sorted method"""
    pass

    def print_sorted(self):
        """Sorted list method"""

        print(sorted(list(self)))
