
# every method in class should have atleast one parameter ... self


class Point:
    # constructor
    # instance method
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # class level ...attribute or properties
    # remain same for all child objects

    default_color = "blue"

    # instance methods
    def draw(self):
        print(f"Point: ({self.x}, {self.y})")

    # class method
    # is a factory method
    @classmethod
    def zero(cls):
        # instead of point = Point(0,0)  we will write .. point = Point.zero()
        return cls(0, 0)
        # refering to same class with predefined values.. and returning the new object

    # magic methods
    # comparision magic method
    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    # numeric magic method
    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)


# changing class level attributes
Point.default_color = "lightBlue"

# self refer to the current object and its properties
point = Point(2, 3)

# class methods
point2 = Point.zero()  # is a factory method
# instance methods
point2.draw()
point.draw()

# magic methods
print(str(point))
print(point == point2)
print(point != point2)
print(point >= point2)
print(point <= point2)
print(point < point2)
print(point > point2)
print(point + point2)
