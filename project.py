import turtle

a = turtle.Turtle()
a.color("green")
a.shape("blank")
a.speed(0)
i = 0   #i가 커질수록 무늬의 간격이 커진다
while True:
    a.forward(i)
    a.right(91)
    i += 0.5