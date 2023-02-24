###################### LISTS
# List items are ordered collections, changeable, and allow duplicate values

# myList = ['coffee', 'tea', 'milk', 'sugar', 'bubble tea']
# print(myList[0])
# print(myList[4])
# addons = myList[2:3] # slicing operator
# others = myList[1:4:3]  # range(2, 10, 2)
# print(addons)
# print(others)

# with len/length you count from 1,
# you count actual items not index [0]
# c = len(myList)
# print(c)
# the same way to do it in one line below
# print(len(myList))

# empty = [] # accumulator variable
# empty1 = "" # accumulator variable

vocabulary = ["iteration", "selection", "control"]
numbers = [17, 123]

mixedList = ["hello", 2.0, "5*2", True, [10, 20]]
#
# print(numbers)
# print(vocabulary)
print(mixedList)
print(mixedList[4])
# print(mixedList[5]) # er
print(mixedList[4][1])
#
# merge 2 previous lists of different data types together as 2 nested lists in one list
newList = [numbers, vocabulary]
print(newList)

anotherList = ["apple", "samsung", "HTC", "motorola"]
print(anotherList[1])
anotherList[1] = "cricket"
print(anotherList)
#
anotherList.append("Google Pixel")
print(anotherList)

aList = [1, 3, 5, 7, 9, 2]
sum1 = aList[0] + aList[2] + aList[4] # 1 + 5 + 9
sum2 = aList[1] + aList[3] + aList[5] # 3 + 7 + 2
print(sum1, "\t", sum2)

#ALIASING
# listB will only be a reference to listA, and changes made in listA will
# automatically also be made in listB.
listA = [1, 2, 3, 4]
print(listA)
listB = listA
print(listB)
print(listA is listB) # used to test if two variables refer to the same object
print(listA == listB) # used to test same value

#Copy a list
firstlist = ["blue", "red", "black"]
mylist = firstlist.copy()
print(mylist)

for x in ["blue", "red", "black"]:
    print(x)




