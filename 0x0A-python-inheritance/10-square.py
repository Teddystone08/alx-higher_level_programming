#1/usr/bin/python3
"""Class module Square"""
class Square(Rectangle):

    def __init__(self, size)
    """Method init, which initialize size"""

        super().__init__(self, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Method rectangle area"""

        return self.__size ** 2
