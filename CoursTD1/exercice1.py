"""Code for calcultating area of different shapes with OOP"""
class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def get_area(self) -> float:
        return self.side ** 2

class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def get_area(self) -> float:
        return self.length * self.width

class Circle:
    PI = 3.14 # attribut qui sera le même pour tous les objets Circle instanciés
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def get_area(self) -> float:
        return self.PI * self.radius ** 2

if __name__ == "__main__":
    square1 = Square(side=5)
    print(f"Square 1: side={square1.side}, area={square1.get_area()}")

    square2 = Square(side=4)
    print(f"Square : side={square2.side}, area={square2.get_area()}")

    rectangle = Rectangle(length=5, width=3)
    print(f"Rectangle: length={rectangle.length}, width={rectangle.width}, area {rectangle.get_area()}")

    circle1 = Circle(radius=2)
    print(f"Circle 1: radius={circle1.radius}, area={circle1.get_area()}")

    circle2= Circle(radius=3)
    print(f"Circle 2: radius={circle2.radius}, area={circle2.get_area()}")