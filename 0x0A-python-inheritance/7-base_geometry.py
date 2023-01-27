#!/usr/bin/python3
"""
==============================
Class module with BaseGeometry
==============================
"""
class BaseGeometry:
    """BaseGeometry class"""
    
    def area(self):
        """Method for area calculation"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validator intehers"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            
            raise ValueError(f"{name} must be greater than 0")
