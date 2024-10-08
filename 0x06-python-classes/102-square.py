#!/usr/bin/python3
"""efines a class Square"""


class Square:
    """
	epresents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """
		nitializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """
		alculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """
		etter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
		etter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def __lt__(self, other):
        """
		ompare if square is less than another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size < other.size

    def __le__(self, other):
        """
		ompare if square is less than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size <= other.size

    def __eq__(self, other):
        """
		ompare if square is equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size == other.size

    def __ne__(self, other):
        """
		ompare if square is not equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size != other.size

    def __ge__(self, other):
        """
		ompare if square is greater than or equal to another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size >= other.size

    def __gt__(self, other):
        """
		ompare if square is greater than another by area
        Args:
            other (Square): square to compare against
        Returns:
            True or False
        """
        return self.size > other.size
