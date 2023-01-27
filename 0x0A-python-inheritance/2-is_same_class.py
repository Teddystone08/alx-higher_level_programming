#!/usr/bin/python3
"""
================================
module with method is_same_class
================================
"""
def is_same_class(obj, a_class):
    """Method to check if an object is exactly an instance
    of s specified class"""

    return type(obj) is a_class
