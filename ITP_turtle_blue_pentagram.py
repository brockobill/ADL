'''
turtle_blue_pentagram.py drawns a blue pentagram star
'''

# import turtle
import turtle
 
# start working screen
ws = turtle.Screen()
 
# initialise turtle 
star = turtle.Turtle()

# move turtle 200 units left from the centre
star.penup()
star.goto(-200, 0)
star.pendown()

# set pen size and colour
star.pensize(5)
star.color("blue")
 
# execute loop 5 times to draw star
for i in range(5):
 
        # move turtle 140 units forward
        star.forward(400)
 
        # rotate turtle 144 degree right
        star.right(144)

# lets user close screen
turtle.done()