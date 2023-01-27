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

        def area(self):
        """Method to redefine a area method in the parent class"""

        return self.__width * self.__height

     def __str__(self):
        """__str__ method for return the next string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
