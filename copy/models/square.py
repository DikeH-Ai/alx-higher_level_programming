#!/urs/bin/python3

"""
Defines Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Square class initialization

         Parameters:
        - `size` (int): The size of the Square.
        - `x` (int): The x-coordinate of the Square.
        - `y` (int): The y-coordinate of the Square.
        - `id` (int): The unique identifier of the Square.
        """
        self.is_valid1(size, "width")
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """Return size value"""
        return self.width
    
    @size.setter
    def size(self, value):
        """set the size"""
        self.is_valid1(value, "width")
        self.width = value
        self.height = value
    
    def update(self, *args, **kwargs):
        """Update attributes"""
        if args:    
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """returns instance info"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
    
    def __str__(self):
        """
        String representation of Square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"