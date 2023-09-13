from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        a = self.a
        b = self.b
        c = self.c
        if a<c+b and c<a+b and b<a+c and a>0 and b>0 and c>0:
            return True
        else:
            False
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        a = self.a
        b = self.b
        c = self.c
        if a<c+b and c<a+b and b<a+c and a>0 and b>0 and c>0:
            if (a==b and c!=a) or (a==c and b!=a) or (b==c and a!=b):
                return 'Teng yonli'
            elif a==b and a==c and b==c:
                return 'Teng tomonli'
            else:
                return 'Turli tomonli'
        else:
            False
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        a = self.a
        b = self.b
        c = self.c
        if a<c+b and c<a+b and b<a+c and a>0 and b>0 and c>0:
            return a+b+c
        else:
            0

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        a = self.a
        b = self.b
        c = self.c
        if a<c+b and c<a+b and b<a+c and a>0 and b>0 and c>0:
            p = (a+b+c)/2
            s = sqrt(p*(p-a)*(p-b)*(p-c))
            return s
        else:
            0
triangle = Triangle(4, 7, 5)
is_valid_triangle = triangle.is_valid()
triangle_perimeter = triangle.perimeter()
triangle_area = triangle.area()

print("Can it be a triangle?", is_valid_triangle)
# Can it be a triangle? True
print("The perimeter of the triangle is:", triangle_perimeter)
# The perimeter of the triangle is: 16
print("The area of the triangle is:", triangle_area)
# The area of the triangle is: 9.797958971132712