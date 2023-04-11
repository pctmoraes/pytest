import math

class Circle:
    def __init__(self, area):
        if type(area) not in [int, float]:
            raise TypeError("The radius must be either int or float type")
        if area < 0:
            raise ValueError("The radius must be greater than or equal to zero")
        
        self.area = area
        
    def get_area(self):
        """
        Calculates the area of the circle.

        Returns:
            A float representing the area of the circle
        """
        area = math.pi * (self.area ** 2)
        return area
    
    def get_circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            A float representing the circumference of the circle
        """
        circumference = math.pi * self.area * 2
        return circumference

