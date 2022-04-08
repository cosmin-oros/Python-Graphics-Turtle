import turtle
import math

Bob = turtle.Turtle()
Bob.color("purple","yellow")
Bob.speed(0)

Bob.begin_fill()

for i in range(100):
    Bob.forward(math.sqrt(i)*30)
    Bob.left(170)

Bob.end_fill()

turtle.done()