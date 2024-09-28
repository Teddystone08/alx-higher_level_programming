#!/usr/bin/python3
"""
Base
"""
import JSON
import csv

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            """ assign public instance attribute"""
            self.id = id
        else:
            """ instance attribute increment"""
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
