
# every method in class should have atleast one parameter ... self


from abc import ABC, abstractmethod


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
########## getter n setter properties #########
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


###################################################
################# inheritance #####################
###################################################

class Animal:
    def __init__(self):
        print("Animal class")

    def eats(self):
        print("We eat food")

# Animal: parent, base
# Mamal: child, subClass


class Mammal(Animal):

    def __init__(self):
        super().__init__()  # init the parent constructor first
        print("Mamal class")

    def walks(self):
        print("We walk")


class Fish(Animal):
    def swim(self):
        print("We swim")


gellyFish = Fish()
gellyFish.eats()
gellyFish.swim()

elephant = Mammal()
elephant.eats()
elephant.walks()
print(isinstance(elephant, Animal))  # true
print(isinstance(elephant, Mammal))  # true
# true ... parent class always inherits from .. built-in object class
print(isinstance(Animal, object))
print(issubclass(Mammal, Animal))  # true


# multiple inheritance

class Person:
    def __init__(self):
        print("I am person")

    def eats(self):
        print("I eats")


class Employee:
    def __init__(self):
        print("I am Employee")

    def works(self):
        print("I work")


class Manager(Employee, Person):
    def __init__(self):
        super().__init__()
        print("I am Manager")

    def management(self):
        print("I manage workers")


manager = Manager()

manager.eats()
manager.works()
manager.management()


# abstract class and methods
# abstract method is just a method that sits in parent Adc class and defined and implemented in child class
# if we dont implement the abc method in child class then... child class cannot be instantiated

class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        print("Some implementation!")


class AnotherSubclass(AbstractClassExample):

    def do_something(self):
        super().do_something()
        print("The enrichment from AnotherSubclass")


x = AnotherSubclass()
x.do_something()


# Polymorphism in Python
# What is Polymorphism: The word polymorphism means having many forms. In programming, polymorphism means same function name(but different signatures) being uses for different types.

# Example of inbuilt polymorphic functions:

# filter_none
# edit
# play_arrow

# brightness_4
# Python program to demonstrate in-built poly-
# morphic functions

# len() being used for a string
print(len("geeks"))

# len() being used for a list
print(len([10, 20, 30]))
# Output:


# 5
# 3
# Examples of used defined polymorphic functions:

# filter_none
# edit
# play_arrow

# brightness_4
# A simple Python function to demonstrate
# Polymorphism


def add(x, y, z=0):
    return x + y+z


# Driver code
print(add(2, 3))
print(add(2, 3, 4))
# Output:
# 5
# 9
# Polymorphism with class methods:
# Below code shows how python can use two different class types, in the same way. We create a for loop that iterates through a tuple of objects. Then call the methods without being concerned about which class type each object is. We assume that these methods actually exist in each class.

# filter_none
# edit
# play_arrow

# brightness_4


class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi the primary language of India.")

    def type(self):
        print("India is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
# Output:
# New Delhi is the capital of India.
# Hindi the primary language of India.
# India is a developing country.
# Washington, D.C. is the capital of USA.
# English is the primary language of USA.
# USA is a developed country.


# Polymorphism with Inheritance:
# In Python, Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class. In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child class. In such cases, we re-implement the method in the child class. This process of re-implementing a method in the child class is known as Method Overriding.

# filter_none
# edit
# play_arrow

# brightness_4


class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
# Output:
# There are many types of birds.
# Most of the birds can fly but some cannot.
# There are many types of birds.
# Sparrows can fly.
# There are many types of birds.
# Ostriches cannot fly.


# Polymorphism with a Function and objects:
# It is also possible to create a function that can take any object, allowing for polymorphism. In this example, let’s create a function called “func()” which will take an object which we will name “obj”. Though we are using the name ‘obj’, any instantiated object will be able to be called into this function. Next, lets give the function something to do that uses the ‘obj’ object we passed to it. In this case lets call the three methods, viz., capital(), language() and type(), each of which is defined in the two classes ‘India’ and ‘USA’. Next, let’s create instantiations of both the ‘India’ and ‘USA’ classes if we don’t have them already. With those, we can call their action using the same func() function:

# filter_none
# brightness_4


def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)

# Code: Implementing Polymorphism with a Function

# filter_none
# edit
# play_arrow

# brightness_4


class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi the primary language of India.")

    def type(self):
        print("India is a developing country.")


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)
# Output:
# New Delhi is the capital of India.
# Hindi the primary language of India.
# India is a developing country.
# Washington, D.C. is the capital of USA.
# English is the primary language of USA.
# USA is a developed country.
