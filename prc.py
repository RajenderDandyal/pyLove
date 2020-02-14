# fint the most repeating letter in this string


str = "his is the long lasting string where we have to find the most repeating letter"
obj = {}
for ltr in str:
    if ltr == " ":
        continue

    if ltr in obj:
        obj[ltr] += 1
    else:
        obj[ltr] = 1
    print(ltr)

arr = [[item, obj[item]] for item in obj]
arr.sort(key=lambda item: item[1], reverse=True)
# [['e', 10], ['t', 9], ['i', 6], ['h', 5], ['s', 5], ['n', 5], ['g', 4], 
# ['r', 4], ['l', 3], ['o', 3], ['a', 3], ['w', 2], ['v', 1], ['f', 1], ['d', 1], ['m', 1], ['p', 1]]
print(arr)
print(obj)
