class Rectangle:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b

    def is_valid(self) -> bool:
        """
        This method checks if the rectangle is valid
        
        Args:
            No
        Returns: 
            bool: True if the rectangle is valid, False otherwise
        """ 
        a = self.a
        b = self.b
        if a>0 and b>0:
            return True
        else:
            return False
    def perimeter(self) -> float:
        """
        This method finds the perimeter of the rectangle.
        Args:
            No
        Returns:
            float or int: return perimeter of the rectangle if the rectangle is valid, 0 otherwise
        """
        a = self.a
        b = self.b
        if a>0 and b>0:
            return 2*(a+b)
        else:
            return 0

    def area(self) -> float:
        """
        This method finds the area of the rectangle.
        Args:
            No
        Returns:
            float or int:  return area of the rectangle if the rectangle is valid, 0 otherwise 
        """
        a = self.a
        b = self.b
        if a>0 and b>0:
            return a*b
        else:
            return 0
rectangle = Rectangle(4, 7)
is_valid_rectangle = rectangle.is_valid()
rectangle_perimeter = rectangle.perimeter()
rectangle_area = rectangle.area()

print("Can it be a square?", is_valid_rectangle)