import math 

class Circle:
    def __init__(self, radius, operation):
        self.radius = radius
        self.operation = operation
        
    def __str__(self):
        if self.operation == "area":
            return f'{round(math.pi * self.radius * self.radius,2)}'
        elif self.operation == "perimeter":
            return f'{round(2 * math.pi * self.radius,2)}'
        else:
            return "Invalid operation"