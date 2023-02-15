"""conditionals are if/else statements, basically you have one condition or sets of conditions, if something is first
evaluated to be true or false, it will proceed with an action or behavior
it a particular evaluation of a statement is false, the program continues evaluation with subsequent lines"""
#################### EQUALITY OPERATORS (2 ITEMS HAVE SAME VALUE)
print(10 > 9)
print(10 == 9)
print(10 < 9)
print(10 != 9)

#################### IS, IS NOT, IN (COMPARISON OPERATORS ARE THEY REFERRING TO SAME OBJECT IN MEMORY)
j = 1
p = 2
print('h' in "hello")
print('z' in "hello")
print(j is p) # same object in memory?
print(j is not p) #
print(j == p) # same value
j = 4
print(j is j) # same object in memory, diff value


#################### OR, NOT, AND
# a = 200
# b = 33
# c = 500
# if a > b and c > a: # &&
#   print("YOOOO Both conditions are True")
#
# if a > b or c > a: # ||
#   print("HEYYYYY Both conditions are True")

#####################
a = 33
b = 50
# one equal sign means an assignment operator
# double equal sign means actual equal in value, left and right are truly equal
if b > a:
    print("b is greater than a")
elif a == b:  # elif keyword is pythons way of saying
    # " of the previous conditions were not true, then try this condition
    print("a and b are equal")
else:  # the else keyword catches anything that isn't caught
    # by other preceding conditions
    print("a is greater than b")
#You can also have an else without the elif

######################### Bool Function
"""The bool() function returns the boolean value of a specified object.
The object will always return True, unless:
empty, like [], (), {}
is False
0
None"""

print(bool("Welcome"))
print(bool(22))
# print(bool(a))
print(bool(0))  # return false
print(bool(""))  # return false

########################
# real world example half natural language half code
# we did not get to go over this example in class on 11/17
"""
Lottery = input("Did you win the lottery? 1=yes, 2=no")
if lottery == 1:
  quit job
  have a party
  buy 10 cars
  buy 10 houses
else:
  continue 9-5 job
  keep doing other job stuff that sucks
"""

"""
if coffeemaker goes off:
    I am not grumpy
    I am in good mood
    I get to class on time
else:
    I am late to class
    I am very grumpy
    I do not have a good day
"""
