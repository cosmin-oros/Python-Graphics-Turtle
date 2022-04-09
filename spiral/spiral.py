import turtle

t=turtle.Turtle()

t.speed(0)
turtle.bgcolor("black")

for i in range(250):
    t.color("purple")
    t.circle(i)
    t.left(5)

turtle.done()