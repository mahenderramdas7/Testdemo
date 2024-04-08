# 1. Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.
"""
mylist = [1,2,2,3,3,4,5,6,6,7]
for x in range(len(mylist)):
    if mylist.count(x)>1:
        print(x, 'is duplicate')


List = [13,14,14,15,15,16,16,17,18,18]
for x in range(len(List)):
    if List.count(x)>1:
        print(x,"duplicate Value")

for x in range(len(mylist)):
    if mylist.count(x)>1:
        print(x, 'is duplicate')

List = [13, 14, 14, 15, 15, 16, 16, 17, 18, 18]

for x in List:
    if List.count(x) > 1:
        print(x, "is a duplicate value")

"""
List = [1,2,2,3,3,4,5,6,6,7]
for x in List:
    if List.count(x) > 1:
        print(x, "is a duplicate value")
