#!/usr/bin/python3

"""Module of a rectangle"""


class Rectangle:
    """empty class method for rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize instances with attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the value of __width
        Sets the value of __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of __height
        Sets the value of __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Rectangle perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Creates a new string object from the given object
        """
        s = ''
        if self.__width > 0 and self.__height > 0:
            for _ in range(self.__height):
                for _ in range(self.__width):
                    s += '#'
                s += '\n'
        return s[: -1]

    def __repr__(self):
        """string representation of the object"""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Prints on instance delete"""
        print("Bye rectangle...")
