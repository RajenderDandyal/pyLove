
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


# building custom dict .. with magic methods

class MyDict:
    def __init__(self):
        self.myDict = {}
        self.__myDict2 = {}

    def add(self, tag):
        self.myDict[tag.lower()] = self.myDict.get(tag.lower(), 0) + 1

    # magic methods
    def __getitem__(self, tag):
        return self.myDict.get(tag.lower())

    def __setitem__(self, key, value):
        self.myDict[key.lower()] = value

    def __len__(self):
        return len(self.myDict)

    def __iter__(self):
        return iter(self.myDict)


dict = MyDict()
dict.add("PYTHON")
dict.add("python")
dict.add("python")
dict.add("python")
dict["python"] = 3
print(dict["python"])  # 4
print(dict.myDict)  # {'python': 4}
dict["python"] = 3
print(dict["python"])  # 3
print(dict.myDict)  # {'python': 3}

print(dict.myDict)  # is not private
# is private.... AttributeError: 'MyDict' object has no attribute 'myDict2'
# print(dict.myDict2)
# print(dict.__myDict2)  # is private

# but python dont have private and public keywords
# __prorerty is just a convention to prevent accidental access to private attributes/properties
# we can still access the private properties .. as all properties are stored in __dict__
print(dict.__dict__)  # {'myDict': {'python': 3}, '_MyDict__myDict2': {}}
# so we can still access the private property by
print(dict._MyDict__myDict2)  # {}


##############################################
########## getter n setter properties#########
##############################################

# simple way .... not using python features to full potential
class GetterSetter:
    def __init__(self, price):
        self.setPrice(price)

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price


price = GetterSetter(2)
print(price.getPrice())
price.setPrice(10)
print(price.getPrice())


# property built-in method .. to set and get a attribute
class Product:
    def __init__(self, price):
        self.setPrice(price)

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price
    # now we can directly use the price property .. to get and set the price
    price = property(getPrice, setPrice)


product = Product(20)
print(product.price)
product.price = 23
print(product.price)


# decorator property .... for getter n setter of price
class Product2:
    def __init__(self, value):
        self.price = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


product2 = Product2(20)
print(product2.price)
product2.price = 23
print(product2.price)
