#!/usr/bin/python3

"""
============================
Module with class Mylist
============================
"""

class Mylist(list):
    """Class with print_sorted method"""

    def print_sorted(self):
        """Method that sorted list"""
        self.sort()
        print(self)
