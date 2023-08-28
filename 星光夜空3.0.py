from tkinter import Tk,messagebox
root = Tk()
root.withdraw()


import turtle
from random import randint, random

t = turtle.Turtle()
t.penup()
#t.speed('fastest')
t.speed(0)
#t.traser(0)
t.ht()

def inside_window():
    left_limit = (-turtle.window_width() / 2) + 100
    right_limit = (turtle.window_width() / 2) + 100
    top_limit = (turtle.window_height() / 2) + 100
    bottom_limit = (-turtle.window_height() / 2) + 100
    (x, y) = t.pos()
    inside = left_limit < x < right_limit and bottom_limit < y < top_limit
    return inside


def star(points, size, col, move, degree):
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()
    t.penup()
    if inside_window():
        t.right(degree)
        t.forward(move)
    else:
        t.backward(move * 3)
        t.right(degree)
        t.forward(move)


# counter setting
text_turtle = turtle.Turtle()
text_turtle.ht()
text_turtle.penup()
x = (turtle.window_width() / 2) - 50
y = (turtle.window_height() / 2) - 50
text_turtle.setpos(x, y)
text_turtle.pencolor("white")
num = 0


# Main code
turtle.Screen().bgcolor('dark blue')


while True:
    text_turtle.clear()
    num = num + 1
    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint(25, 50)
    ranCol = (random(), random(), random())
    ranMove = randint(100, 150)
    ranDeg = randint(10, 170)


    #text_turtle.write(str(num) + " stars", move = False, align = "center", font = ["consolas", 40, "normal"])
    star(ranPts, ranSize, ranCol, ranMove, ranDeg)
print("Total stars:" + str(num))
