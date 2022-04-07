import turtle

turtle.bgcolor("black")
turtle.pensize(1)
turtle.speed(0)

for i in range(6):
    for colours in ["red","magenta","blue","cyan","yellow","pink","green"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)