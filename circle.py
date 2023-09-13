from math import pi


class Circle:
    def __init__(self, radius:float):
        self.radius = radius
        
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        
        Args:
            No
        Returns:
            bool: True if the circle is valid, False otherwise
        """
        radius = self.radius
        if  radius>0:
            return True
        else:
            return False
    def diameter(self) -> float:
        '''
        This method finds the diameter of the circle.
        Args:
            no
        Returns:
            float: return diameter of the circle if the circle is valid, 0 otherwise
        '''
        radius = self.radius
        if  radius>0:
            return 2*radius
        else:
            return 0
    
    
    def circumference(self) -> float:
        '''
        This method finds the circumference of the circle.
        Args:
            no
        Returns:
            float: return circumference of the circle if the circle is valid, 0 otherwise
        '''
        radius = self.radius
        if  radius>0:
            return 2*pi*radius
        else:
            return 0
    
    def area(self) -> float:
        '''
        This method finds the area of the circle.
        Args:
            no
        Returns:
            float: return area of the circle if the circle is valid, 0 otherwise
        '''
        radius = self.radius
        if  radius>0:
            return pi*radius**2
        else:
            return 0
circle = Circle(4)
is_valid_circle = circle.is_valid()
circle_diameter = circle.diameter()
circle_circumference = circle.circumference()
circle_area = circle.area()
print(circle_circumference)