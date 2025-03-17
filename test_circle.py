import math
from circle import Circle

def test_circle_perimeter():
    circle_check = Circle(10)
    assert circle_check.perimeter() == round(2 * math.pi * circle_check.radius, 2)

def test_circle_area():
    circle_check = Circle(10)
    assert circle_check.area() == round(math.pi * circle_check.radius ** 2, 2)