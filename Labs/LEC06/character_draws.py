import math
from pico2d import *

open_canvas(800, 600)
character = load_image('character.png')

r = 50
centerX = 400
centerY = 300

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
    move_circle()
    move_rectangle()
    move_triangle()

close_canvas()