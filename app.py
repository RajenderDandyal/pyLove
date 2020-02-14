print("hello world")

print("hello ji")
s = 3
r = 34
f = 23
g = 56

temp = 44

if temp < 10:
    print("its cold")
elif temp < 25:
    print("its good")
else:
    print("its hot")

age = 18
msg = "Yup" if age >= 18 else "Nope"  # js terniary operator
print(msg)

# check for age is more than 18 and less than 65
# js style

if age >= 18 and age < 65:
    print("old style condition")
if 18 <= age < 65:
    print("new math style condition")


if 10 == '10':
    print("nope")
else:
    print("js converts condition operands to number but not python")
    print("number 10 is not equal to string 10")


# range and loop

for number in range(5):
    print("Attempt", number)

for number in range(1, 6):
    print("Attempt", number, number*".")

# with step
for number in range(1, 10, 2):
    print("Attempt", number, number*".")


# for else loop
num = 4
for i in range(1, 4):
    print(i)
    if num == i:
        print("success")
        break
else:  # Executed because no break in for .. if break statement runs .. then else block of for loop will not run
    print("No Break")


# nested loops
# formated string
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")


# print even numbers
count = 0
for x in range(11):
    if x % 2 == 0:
        print(x)
        count += 1
        continue
print(f"We have {count} even numbers")

# function without return statement returns
# undefined in js
# None in python


# keyword arguments
# all default value parameters should comes after required parameters in func def..... not the case in js
def incremnt(number, by=1):
    return number + by


print(incremnt(number=4, by=99))


# agruments n ...rest operator equivalent in python
# *args ... returns a tuple
def multiply(*nums):
    print(nums)
    ttl = 1
    for num in nums:
        ttl = ttl*num

    return ttl


print(multiply(1, 2, 3, 4, 5, 6, 7, 8, 9))

# **args .. returns dict


def user_data(**user):
    print(user)
    return f'{user["first_name"]} {user["last_name"]}'


print(user_data(first_name="Rajender", last_name="Dandyal"))


# scope
# global scope and local to function scope
msg = "hello world"


def MyFunction():
    # msg = "new World"  # this is local scope variable
    global msg
    msg = "New to newest World"


print(msg)
print(MyFunction())
print(msg)


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 != 0:
        return "Fizz"
    elif num % 5 == 0 and num % 3 != 0:
        return "Buzz"
    elif num % 3 == 0 and num % 5 == 0:
        return "Fizz Buzz"
    else:
        return num


print(fizz_buzz(7))


# concatinating 2 arrays in js and python

# let arr1 = [1,2,3,4,5]
# let arr2 = [11,22,33,44,55,66]
# let arr3 = [...arr1, ...arr2]

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = arr1 + arr2
print(arr3)  # [1, 2, 3, 4, 5, 6]

# creating list or arrays
nums = list(range(20))
strArr = list("hello world")
print(nums)
print(strArr)
