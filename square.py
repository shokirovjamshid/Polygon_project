class Square:
    def __init__(self, square_side:float):
        self.square_side = square_side
    
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        Args:
            No
        Returns:
            bool: This method checks if the square is valid.
        """
        side = self.square_side
        if side>0:
            return True
        else:
            return False
    
    def area(self) -> float:
        """
        This method finds the area of the square.
        Args:
            No
        Returns:
            float or int: return area of the square if the square is valid, 0 otherwise
        """
        side = self.square_side
        if side>0:
            return side**2
        else:
            return 0
    
    def perimeter(self) -> float:
        """
        This method finds the perimeter of the square.
        Args:
            No
        Returns:
            float: return perimeter of the square if the square is valid, 0 otherwise
        """
        side = self.square_side
        if side>0:
            return 4*side
        else:
            return 0
square = Square(5)
is_valid_square = square.is_valid()
square_perimeter = square.perimeter()
square_area = square.area()

print("Can it be a square?", is_valid_square)
# Can it be a square? True
print("The perimeter of the square is:", square_perimeter)
# The perimeter of the square is: 20
print("The area of the square is:", square_area)
# The area of the square is: 25