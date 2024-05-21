import turtle as t
import random

tt = t.Turtle()
tt.speed(0)
t.colormode(255)
color = [(215, 155, 114), (135, 170, 191), (212, 130, 147), (219, 75, 93), (31, 116, 147), (236, 209, 104)]
tt.hideturtle()
tt.setheading(225)
tt.penup()
tt.forward(320)
tt.setheading(0)
for i in range(10):
    for j in range(10):
        tt.dot(20, random.choice(color))
        tt.penup()
        tt.forward(50)
        tt.pendown()
    tt.setheading(90)
    tt.penup()
    tt.forward(50)
    tt.setheading(180)
    tt.penup()
    tt.forward(500)
    tt.setheading(0)

screen = t.Screen()
screen.exitonclick()
