# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
        
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def area(self):
        return self.width * self.length
    
rect = Rectangle(7, 2)
print(f"The area of rectangle is: {rect.area()}")