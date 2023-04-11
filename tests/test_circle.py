from src.circle import Circle
from math import pi

def test_get_area():
    # Test the radius of a circle with an area of 1
    c1 = Circle(area=1)
    assert c1.get_area() == pi

    # Test the radius of a circle with an area of 100
    c2 = Circle(area=10)
    assert c2.get_area() > 314
    
    # Test the radius of a circle with an area of 100
    c3 = Circle(area=100)
    assert c3.get_area() != 0

def test_get_circumference():
    # Test the circumference of a circle with an area of 2
    c1 = Circle(area=5)
    assert round(c1.get_circumference(), 2) == 31.42

    # Test the circumference of a circle with an area of 10
    c2 = Circle(area=10)
    assert c2.get_circumference() > 62