import math
from circle import Circle

def test_circle():
    circle_check = Circle(10, "perimeter")
    assert circle_check.__str__() == str(round(2 * math.pi * circle_check.radius, 2))

    circle_check = Circle(10, "area")
    assert circle_check.__str__() == str(round(math.pi * circle_check.radius ** 2, 2))

    circle_check = Circle(10, "invalid")
    assert circle_check.__str__() == "Invalid operation"