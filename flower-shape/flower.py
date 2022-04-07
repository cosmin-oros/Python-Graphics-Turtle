from turtle import *

speed(0)  # remove in order to make it slower
color("red")


def fleur():
    for i in range(300):
        circle(190 - i, 90)
        left(90)
        circle(190 - i, 90)
        left(18)


fleur()
mainloop()
