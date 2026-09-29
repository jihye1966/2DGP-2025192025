import math
from pico2d import *

open_canvas(800, 600)
character = load_image('character.png')

r = 200
centerX = 400
centerY = 300
State = 0 #0:circle, 1: rectangle, 2: triangle

def move_circle():
    for i in range(0, 360, 1):
        x = centerX + r * math.cos(math.radians(i))
        y = centerY + r * math.sin(math.radians(i))
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        delay(0.01)
    pass

def move_top(y):
    return y + 3

def move_right(x):
    return x + 3

def move_bottom(y):
    return y - 3

def move_left(x):
    return x - 3

def move_rectangle():
    x = centerX + r * math.cos(math.radians(0))
    y = centerY + r * math.sin(math.radians(0))
   

    print('rectangle')
    pass

def move_triangle():
    print('triangle')
    pass

while True:
    if State == 1:
        move_circle()
    elif State == 0:
        move_rectangle()
    elif State == 2:
        move_triangle()

close_canvas()