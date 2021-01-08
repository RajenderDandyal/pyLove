# list

from copy import deepcopy


letters = ["a", "b", "c", "d"]
print(letters)

# reassigning to list
letters[0] = "A"

# slicing
print(letters[0:])  # ['A', 'b', 'c', 'd']
print(letters[:4])  # ['A', 'b', 'c', 'd']
print(letters[:3])  # ['A', 'b', 'c']

print(letters[2:4])  # ['c', 'd']
print(letters[2:3])  # ['c']

# slicing with step
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::2])  # [1, 3, 5, 7, 9]

# reverse a list
nums.reverse()
print(nums)
nums2 = nums.reverse()

print(nums2)
print(nums[::-1])


# destructuring ...js
# let [first,second, ...rest] = [1,2,3,4,5]
# list unpacking python

array = [1, 2, 3, 4, 5, 6, 6, 7, 7, 6]
first, second, *others = array


print(first, second, others)


# loop through an array
# js .. for 0f loop
# python for in loop for every thing

for num in array:
    print(num)

for num in enumerate(array):
    print(num)
(0, 1)
(1, 2)
(2, 3)
(3, 4)
(4, 5)
(5, 6)
(6, 6)
(7, 7)
(8, 7)
(9, 6)

# equivalent to jf forEach loop
for index, item in enumerate(array):
    print(index, item)
    
    
# add to list
array.append(9)
array.insert(1, 23)

# find index
ind = array.index(2)
print(ind)
# if we try to find the index of item thats not in the list
# js .. gives .. -1
# python gives .. error
# so use this before finding index in python
if 24 in array:
    print(array.index(24))

# create shallow copy
array2 = array.copy()

# to count no. of occurance of a item in list
print(array.count(2))
print(len(array))

# remove from list
array.pop()  # removes the last item
array.remove(6)
del array[0:3]  # last item not included
array.clear()  # del a[:]   both clear the list
print(array)


# sorting list

numm = [9, 3, 4, 5, 1, 3, 5, 8, 9]
numm.sort()  # sort the actual numm list
print(numm)
numm.sort(reverse=True)  # sort the actual numm list in reverse order
print(numm)

# same as .sort but return the new sorted list
numm2 = sorted(numm, reverse=True)
print(numm2)


# sorting array of array

productList = [
    ("p1", 110),
    ("p2", 102),
    ("p3", 329),
    ("p4", 222),
    ("p5", 343)
]


def sortProductList(productList):
    return productList[1]


sortedList = sorted(productList, key=sortProductList)
print(sortedList)


# sorting array of dicts

proList = [
    {"price": 110},
    {"price": 10},
    {"price": 232},
    {"price": 22},

]


def sortDictList(list):
    return list["price"]


proList.sort(key=sortDictList)
print(proList)


# map functions

# from above product list get the price list

priceList = map(lambda list: list["price"], proList)
# map, filter return a class object that is iterable n we can loop over it ... so convert it to ... list


# filter
print(list(priceList))  # [10, 22, 110, 232]

y = filter(lambda item: item["price"] > 100, proList)
print(list(y))


# List Comprehensions
# [expression for item in items]
# [expression for item in items if item["smthng"] >= 12318]

# for map method
xx = [item["price"] for item in proList]
print(xx)

# for filter method
yy = [item["price"] for item in proList if item["price"] > 100]
print(yy)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ dict $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

point = {"x": 1, "y": 2}
# same as point = dict(x=1, y=2)


# getting smthng not there in dict
# print(point["a"])  gives an error in python .. udefined in js
# sol
if "a" in proList:
    print(point["a"])

# or .. use.get method .. will not give error if key is not present.. here we can also provide default value .. if key is not present

print(point.get("a", 3))


keys = point.keys()
values = point.values()
items = point.items()
x, y = point.items()
# ['x', 'y'] [1, 2] [('x', 1), ('y', 2)]
print(list(keys), list(values), list(items), x, y)

for keys in point:
    print(keys)  # prints x,y


for key, value in point.items():
    print(key, value)

for values in point.values():
    print(values)

smthng = {}

for x in range(8):
    smthng[x] = x*4

 # with dict comprehensions

newSmthng = {x: x*5 for x in range(8)}

print(newSmthng)

# sgallow copy .. deep copy
# from copy import deepcopy

# deep copy

lst1 = [{"a": {"c": {"f": "e"}}}]

list2 = deepcopy(lst1)
list3 = lst1.copy()
print(list3)
print(list2)
