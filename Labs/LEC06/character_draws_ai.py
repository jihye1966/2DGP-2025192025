import math

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
CHARACTER_IMAGE = 'character.png'

open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
character = load_image(CHARACTER_IMAGE)

center_x = CANVAS_WIDTH // 2
center_y = CANVAS_HEIGHT // 2
circle_radius = 200


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()


def move_circle():
    for angle in range(360):
        radians = math.radians(angle)
        x = center_x + circle_radius * math.cos(radians)
        y = center_y + circle_radius * math.sin(radians)
        draw_character(x, y)
        delay(0.01)


while True:
    move_circle()


close_canvas()