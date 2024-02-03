'''
turtle_square raws a squre.
'''

# import turtle
import turtle
 
# start working screen
ws = turtle.Screen()
 
# initialise turtle 
star = turtle.Turtle()

# move turtle x number of units left from the centre
star.penup()
star.goto(-50, 0) # make half object size to keep in centre
star.pendown()

# set pen size and colour
star.pensize(5)
star.color("black")
 
# execute loop x number of sides required
for i in range(4):
 
        # move turtle 100 units forward
        star.forward(100)

        # rotate turtle 90 degree right
        star.right(90)

# lets user close screen
turtle.done()