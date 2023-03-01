####### STARTING ICA

# fileIn = open("TextFiles/alice.txt", 'r')
# print(fileIn)

# fileIn = open("TextFiles/alice.txt", 'r')
# count = 0
# for textLine in fileIn:
#   textLine = textLine.strip() # remove newline from end of line
#   print("Line", count, ":", textLine)
#   count = count + 1
# fileIn.close()

# did together in class!
def printAbbrev(str1):
    fileIn = open(str1, 'r') # step 1
    for line in fileIn: #step 2
        print(line[0:20]) #step 3 and step 4
    fileIn.close() #step 5

printAbbrev("TextFiles/alice.txt")