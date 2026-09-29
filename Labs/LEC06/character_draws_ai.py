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


def move_segment(start, end):
    start_x, start_y = start
    end_x, end_y = end
    distance = math.hypot(end_x - start_x, end_y - start_y)
    frames = max(1, math.ceil(distance / 3))

    for frame in range(frames):
        progress = frame / frames
        x = start_x + (end_x - start_x) * progress
        y = start_y + (end_y - start_y) * progress
        draw_character(x, y)
        delay(0.01)


def move_circle():
    for angle in range(360):
        radians = math.radians(angle)
        x = center_x + circle_radius * math.cos(radians)
        y = center_y + circle_radius * math.sin(radians)
        draw_character(x, y)
        delay(0.01)


def move_rectangle():
    rectangle_corners = [
        (center_x - circle_radius, center_y - circle_radius),
        (center_x + circle_radius, center_y - circle_radius),
        (center_x + circle_radius, center_y + circle_radius),
        (center_x - circle_radius, center_y + circle_radius),
        (center_x - circle_radius, center_y - circle_radius),
    ]

    for start, end in zip(rectangle_corners, rectangle_corners[1:]):
        move_segment(start, end)


while True:
    move_circle()
    move_rectangle()


close_canvas()