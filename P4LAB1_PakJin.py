# Jin Pak
# 11/7/2024
# P4LAB1
# Draw a square and triangle using turtle library

import turtle
win = turtle.Screen()
t = turtle.Turtle()
win.bgcolor("#86cecb")

# add some display options
t.pensize(10)            # increase pensize (takes integer)
t.pencolor("#0eeadf")     # set pencolor (takes string)
t.shape("turtle")

# While loop to draw a square
side = 0
while side < 4:
    t.forward(150)
    t.right(90)
    side += 1
print("while loop ends")

# For loop to draw a triangle
for tr in range(0,3):
    t.forward(150)
    t.left(120)
print("For loop has ended")

