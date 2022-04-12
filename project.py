import turtle
import random

turtle.colormode(255)
a = turtle.Turtle()
a.shape("blank")
a.speed(0)
def square(size):
    for _ in range(4):
        a.forward(size)
        a.left(90)
while True:
    i = random.randrange(-360,361)
    j = random.randrange(-360,361)
    ca = random.randrange(0,256)
    cb = random.randrange(0,256)
    cc = random.randrange(0,256)
    a.color(ca,cb,cc)
    a.forward(abs(i))
    a.right(i)
    a.circle(i)
    a.circle(j)
    square(i)
    a.goto(i,j)