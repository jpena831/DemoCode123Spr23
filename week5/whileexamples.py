# REFRESHER, BELOW IS A SIMPLE FOR LOOP
# FOR LOOPS ARE FIXED ITERATIONS
for x in range(10):
    print(x)

for j in "hello":
    print(j)

for i in ["red", "blue", "yellow"]:
    print("Hello, you like these colors", i)

# NOW THESE ARE 3 WHILE LOOPS EXAMPLES
# WHILE LOOPS CAN RUN INFINITELY, BE CAREFUL

# start of first while loop example
# i = 1
# while i < 6:  # this must be true, everything after it runs if its true
#     print(i)
#     # if you comment out counter below, it will produce infinite forever loop
#     # i += 1  # is the same as i = i + 1

# second example of while loop with break statement
# this just breaks after a full iteration or sequence, here stops at 3
# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1

# third example of while loop with continue statement
# here it stops midway during an iteration and picks up at the next iteration
# it prints 1-6 but skips 3
i = 0
while i < 6:
    i += 1  # i = i + 1
    if i == 3:
        continue
    print(i)
