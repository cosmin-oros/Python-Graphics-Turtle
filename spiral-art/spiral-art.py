import turtle

colors = ["red","green","blue","orange","purple","yellow"]

t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)

for i in range(200):
    t.pencolor(colors[i%6])
    t.width(i/100+1)
    t.forward(i)
    t.left(59)
