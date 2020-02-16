
# every method in class should have atleast one parameter ... self


class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # class level ...attribute or properties
    # remain same for all child objects

    default_color = "blue"

    # methods
    def draw(self):
        print(f"Point: ({self.x}, {self.y})")

    @classmethod
    def zero(cls):
        return cls(0, 0)


# changing class level attributes
Point.default_color = "lightBlue"

# self refer to the current object and its properties
point = Point(2, 3)
point2 = Point.zero()
point2.draw()
point.draw()
