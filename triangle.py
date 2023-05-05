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
        if self.a <= 0: return False
        if self.b <= 0: return False
        if self.c <= 0: return False 

        if not self.a+self.b>=self.c: return False
        if not self.a+self.c>=self.b: return False
        if not self.b+self.c>=self.a: return False

        return True
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        if self.is_valid():
            if self.a==self.b and self.b==self.c: return "Teng tomonli"
            if self.a==self.b or self.c==self.a or self.c==self.b: return "Teng yonli"
            return "Turli tomonli"
        return 'in_valid'
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        if self.is_valid():
            return self.a+self.b+self.c
        return 0

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        if self.is_valid():
            p = self.perimeter()/2

            s = sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

            return s
