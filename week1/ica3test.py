# always use the import keyword to use modules
# in this case you must import turtle to use it
import turtle

# create a graphics window
# a dot syntax notation means I am giving the object an action
wn = turtle.Screen()

# created a turtle object called henry
# giving turtle object some actions or characteristics
henry = turtle.Turtle()
turtle.color("red")
turtle.pencolor("blue")

# a set of movements starting with 150 units
henry.forward(150)
henry.left(90)
henry.forward(75)
henry.left(90)
henry.forward(150)
henry.left(150)

##################################################################

""" below is demo on for loops through lists and strings
    as well as for loops using the range function"""
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#
# for y in "hello":
#     print(y)
#
# for z in range(9):
#     print(z)
#
# for i in range(2, 9):
#     print(i)
