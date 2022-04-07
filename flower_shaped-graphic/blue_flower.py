import turtle

turtle.bgcolor("black")
turtle.speed(0)
turtle.pensize(2)
turtle.pencolor("blue")

def drawCircle(radius):
    for i in range(10):
        turtle.circle(radius)
        radius=radius-4

def drawDesign():
    for i in range(10):
        drawCircle(150)
        turtle.right(36)

drawDesign()
turtle.done()