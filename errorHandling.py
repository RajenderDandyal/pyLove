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

if x > 0:
    raise Exception("Sorry, no numbers below zero")


x = "hello"

if not type(x) is int:
    print("")
    #raise TypeError("Only integers are allowed")
    # raise ValueError("Only int are allowed")

try:
    age = int(input("Age:"))
    xFactor = 10/age
except ValueError as err:
    print("Enter a valid age!!", err)
except ZeroDivisionError:
    print("Enter a valid age!!")


try:
    age = int(input("Age:"))
    xFactor = 10/age
except (ValueError, ZeroDivisionError, NameError, TypeError, SyntaxError):
    print("Enter a valid age!!")


# always close the resources that u open in try n finally

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()


# with statement
# is used for objects which have __exit__ __enter__ magical method
# now we don't need the finally block to close the files

try:
    with open("app.py") as app, open("dataStrs.py") as dataStr:
        dataStr.readlines()
        app.read()
        # app.__enter__
        # app.__exit__

except:
    print("Smthng went wrong")
