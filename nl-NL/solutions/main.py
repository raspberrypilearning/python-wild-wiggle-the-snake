from p5 import *
from math import sin

x = 0 # startpositie van de slang

def setup():
    size(400, 400)
    background('lightblue')
    no_stroke()

def draw():
    global x
    background('lightblue')
    fill('green')

    offset = sin(x * 0.1) * 10

    circle(x, 200, 50) # kop op x
    circle(x - 35, 200 + afstand, 40) # lichaam 1
    circle(x - 65, 200 - afstand, 35) # lichaam 2
    circle(x - 90, 200 + afstand, 30) # staart

    fill('white')
    circle(x + 10, 190, 10)
    circle(x + 25, 190, 10)

    fill('black')
    circle(x + 10, 190, 5)
    circle(x + 25, 190, 5)

    x += 2

run()
