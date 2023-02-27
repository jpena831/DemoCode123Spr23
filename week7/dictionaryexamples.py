############## DICTIONARIES
# Dictionary items are ordered, changeable, and does not allow duplicates

# one way of creating a dictionary
MLB_teamA = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}
print(MLB_teamA) # printing out a dictionary
print(sorted(MLB_teamA))# sorts by key
print(sorted(MLB_teamA.items()))# sorts in tuples
print(sorted(MLB_teamA.values()))# sorts values
# second way of creating a dictionary
# using built in function dict()
# MLB_teamB = dict({
#     'Colorado': 'Rockies',
#     'Boston': 'Red Sox',
#     'Minnesota': 'Twins',
#     'Milwaukee': 'Brewers',
#     'Seattle': 'Mariners'
# })

# print access to single item value using the key
# x = MLB_teamB['Minnesota'] # myList[1] # you access instead with the key
# print(x)
#
# # using get() method is the same
# y = MLB_teamB.get("Minnesota")
# print(y)
#
#
# # add key-value pair
# MLB_teamB['St. Louis'] = "Cardinals"
# print(MLB_teamB)
#
# # update or change current dictionary item
# MLB_teamB['Seattle'] = "Seahawks"
# print(MLB_teamB)

MLB_teamB = dict({
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
})
# looping through a dictionary
for i in MLB_teamB:
    print(i)  # loops/prints through keys ONLY

for j in MLB_teamB:
    print(MLB_teamB[j])  # loops/prints through values ONLY

# delete item with key name
del MLB_teamB['Seattle']  # del is a special keyword
print(MLB_teamB)
#
# # copy a dictionary
myDictionary = MLB_teamB.copy()
print(MLB_teamB)
print(myDictionary)

########## NOTES ON COLLECTION DATA TYPES IN PYTHON
'''
1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''
'''
When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, and, 
it could mean an increase in efficiency or security.
'''