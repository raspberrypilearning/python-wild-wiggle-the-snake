from p5 import *
from math import sin

x = 0 # початкова позиція змії

def setup():
    size(400, 400)
    background('lightblue')
    no_stroke()

def draw():
    global x
    background('lightblue')
    fill('green')

    offset = sin(x * 0.1) * 10

    circle(x, 200, 50)          # голова в точці x
    circle(x - 35, 200 + offset, 40) # круг 1
    circle(x - 65, 200 - offset, 35) # круг 2
    circle(x - 90, 200 + offset, 30) # хвіст

    fill('white')
    circle(x + 10, 190, 10)
    circle(x + 25, 190, 10)

    fill('black')
    circle(x + 10, 190, 5)
    circle(x + 25, 190, 5)

    x += 2

run()
