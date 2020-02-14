try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
# else keyword to define a block of code to be executed if no errors were raised:

try:
    print("h")
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# finally block, if specified, will be executed regardless if the try block raises an error or not.


# throw new Error() in code .. js
# raise exception .. python

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")


x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
