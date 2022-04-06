import turtle
import random

a = turtle.Turtle()
a.color("green")
a.shape("blank")
a.speed(0)
i = 0 #변수 i 선언
j = 0 #변수 j 선언
while True:
    i = random.randrange(-360,361)
    j = random.randrange(-360,361)
    a.forward(abs(i))
    a.right(i)
    a.circle(i)
    a.circle(j)
    a.goto(i,j)