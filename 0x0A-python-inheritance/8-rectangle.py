#!/usr/bin/python3
"""
=========================
Class module as Rectangle
=========================
"""

class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry"""

     def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
