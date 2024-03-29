#!/usr/bin/python3
"""Module of a rectangle"""


class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize instances with attributes"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """remove instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def __str__(self):
        """return a '#' representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        hashes = []
        for _ in range(self.__height):
            hashes.append(str(self.print_symbol) * self.__width)
        return '\n'.join(hashes)

    def __repr__(self):
        """returns representation"""
        return "{}({}, {})".format(type(self).__name__,
                                   self.__width, self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """staticmethod"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """classmethod"""
        return cls(size, size)

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
        """calculates the area of the rect.
        Returns:
            the current rect area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rect.
        Returns:
            the perimeter of a rect
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height
