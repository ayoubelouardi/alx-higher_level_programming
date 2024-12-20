#!/usr/bin/python3
"""
Defines the rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Represent the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the new Rectangle.
        Args:
            height (int): height of the new Rectangle.
            width (int): width of the new Rectangle.
            y (int): y coordinate of the new Rectangle.
            x (int): x coordinate of the new Rectangle.
            id (int): identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            TypeError: If either of x or y is not an int.
            ValueError: If either of width or height <= 0.
            ValueError: If either of x or y < 0.
        """
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        super().__init__(id)

    @property
    def width(self):
        """
        set/get the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Set/get the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Set/get the x coordinate of the Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Set/get the y coordinate of the Rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return the area of the hole Rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        print the Rectangle using the `#`
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        upgrade the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1nd argument represents id attribute
                - 2nd argument represents width attribute
                - 3nd argument represent height attribute
                - 4nd argument represents x attribute
                - 5nd argument represents y attribute
            **kwargs (is a dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """
        return the dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        return the print() and str() representation of the Rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
