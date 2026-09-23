import math
from pico2d import *

open_canvas(800, 600)
character = load_image('character.png')

r = 50
centerX = 400
centerY = 300
characterX = centerX + r * math.cos(math.radians(0))
characterY = centerY + r * math.sin(math.radians(0))
State = 0 #0:circle, 1: rectangle, 2: triangle

def move_circle():
    print('circle')
    clear_canvas()
    character.draw(centerX, centerY)
    update_canvas()

    pass

def move_rectangle():
    print('rectangle')
    pass

def move_triangle():
    print('triangle')
    pass

while True:
    if State == 0:
        move_circle()
    elif State == 1:
        move_rectangle()
    elif State == 2:
        move_triangle()

close_canvas()