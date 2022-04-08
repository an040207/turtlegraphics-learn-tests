import turtle
import random

a = turtle.Turtle()
a.color("green")
a.shape("blank")
a.speed(0)
def square(size):
    for _ in range(4):
        a.forward(size)
        a.left(90)
i = 0
j = 0
while True:
    i = random.randrange(-360,361)
    j = random.randrange(-360,361)
    a.forward(abs(i))
    a.right(i)
    a.circle(i)
    a.circle(j)
    square(i)
    a.goto(i,j)
