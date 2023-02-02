import math
import turtle

# s = math.sin(math.pi)
# print(s)
"""
rad = math.radians(30)
print("30  degrees as radians is  = ", rad)
s = math.sin(rad)
print("sin of 30 is  = ", s)

rad = math.radians(60)
print("60  degrees as radians is  = ", rad)
s = math.sin(rad)
print("sin of 60 is  = ", s)

rad = math.radians(90)
print("90  degrees as radians is  = ", rad)
s = math.sin(rad)
print("sin of 90 is  = ", s)

for i in range(1, 90):
    rad = math.radians(i)
    s = math.sin(rad)
    print("sin(", i, ") = ", s)
    
"""

"""
#### starting phase 2 with turtle

window = turtle.Screen()
pikachu = turtle.Turtle()

# pikachu.up()
# pikachu.goto(0, 0)
# pikachu.down
# pikachu.goto(70, 80)

pikachu.up()
pikachu.goto(0, 0)
pikachu.write("(0, 0)")

pikachu.goto(200, 200)
pikachu.write("(200, 200)")

pikachu.goto(-200, 200)
pikachu.write("(-200, 200)")

pikachu.goto(-200, -200)
pikachu.write("(-200, -200)")

pikachu.goto(200, -200)
pikachu.write("(200, -200)")


window.exitonclick()
"""


####Phase 3
#I have added something to help you visualize the problem better in instruction form
# Problem: Create a sine wave using the turtle
#     Algorithm:
#         1. Create and set up the turtle screen
#         2. Iterate the angles from 0 to 360
#             1. generate the sine value for each angle
#             2. Move the turtle to that position (leave a line behind)
#         3. Exit the turtle window


# 1. Create & setup the turtle and screen
win = turtle.Screen()
myTurtle = turtle.Turtle()

# ADD SET WORLD COORDINATES HERE, USE PYTHON DOCUMENTATION
# THIS ALLOWS US TO SEE ACTUAL SINE WAVE
win.setworldcoordinates(-15, -10, 375, 2)

myTurtle.up()
myTurtle.goto(0, 0)
myTurtle.down()

# 2. Iterate the angles from 0 to 360
# for loop to calculate sine of angles between 0 and 360
for i in range(360): # 0 - 359
    # converts degrees to radians
    rad = math.radians(i)
    # calculate the sine of rad
    s = math.sin(rad)
    # print("sin(", i, ") =", s)
    # eventually create line of code for turtle to venture to i,s
    myTurtle.goto(i, s)

win.exitonclick()
