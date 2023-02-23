name = "Jos"
print(name)  # one way to print a string, stored in variable
print("cookies")  # another way to print string directly in print statement

# get the character at position 1, remember we count from 0
a = "Hello, World!"
print(a[2])

# slicing
# get characters from position 2 to position 5 (that last one is not included)
# acts similar to range(2, 10) in for loops
b = "Hi, Earth!"
print(b[2:5])
print(b[2:9])

# # concatenate
fruit = "banana"
bakedstuff = "nut bread"
print(fruit + " " + bakedstuff)
#
myList = ['coffee', 'tea', 'milk', 'sugar', 'bubble tea']
print(myList[8])
print(myList[4])

addons = myList[2:3]
others = myList[1:4:3]  # range(2, 10, 2)
print(addons)
print(others)

#
# with len/length you count from 1
c = len(myList)
print(c)
print(len(b))

for name in ["mary", "amy", "joe", "michael", "john"]:
    invite = "Hi " + name + " please come to my gathering"
    print(invite)


#
# def turnSnake(str1):
#     newString = str1.replace("s", "sss")
#     return newString
#
# print("snake")
# newS = turnSnake("snake")
# print(newS)
# #OR other way to get same result
# print(turnSnake("snake"))

# erics way
# def turnUpper(str1):
#     newString = str1.replace("s", "S")
#     return newString

# keshawn's way
def turnUpper(str1):
    newString = str1.upper()
    return newString

# upper? let's write it together!
print(turnUpper("i saw a frog in my bathtub"))

#ICA Q1
def firstVowel(string):
    vowels = 'aeiou'
    for i in range(len(string)):
        if string[i] in vowels:
            return i

def firstVowel(str):
    vowels = "aeiouAEIOU"
    for i in len(str):
        if vowels in str:
            return str[i]

print(firstVowel('shave'))

