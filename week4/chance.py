import random
import turtle

############Notes on the Random Module and its methods and functions

# random.random() method which generates a random float number between 0.0 and 1.0
# so it will likely give us a decimal each time
prob = random.random()
print(prob)

"""return a random number in a range from 1 - 7 int one of 1, 2, 3, 4, 5, 6"""
# Returns a random number between the given range
diceThrow = random.randrange(1, 7) # range(1, 29, 2)
print(diceThrow)

states = ['minnesota', 'new york', 'michigan', 'illinois', 'california']
nums = [2, 3, 5.5, 7, 9]
print(states[2]) # this would print just the word michigan
print(nums[3])
print(random.choice(states))
print(random.choice(nums))

numbers = [12, 23, 45, 67, 65, 43]
random.shuffle(numbers)
print(numbers)

cake = ["redvelvet", "lemon", "cheesecake"]
random.shuffle(cake)
print(cake)

###################Start of ICA 7 code
# wind = turtle.Screen()
# hermoine = turtle.Turtle()
#
# for i in range(20): # 0-19
#     x = random.randrange(-200, 200)
#
#     hermoine.goto()

#For each time, use the goto() function and the randrange() function
# to generate two random numbers that are the positions that the turtle will be going to.

# randrange(20, 100) goto(x, y)

# wind.exitonclick()


