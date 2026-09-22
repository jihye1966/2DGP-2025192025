from pico2d import *

open_canvas()
character = load_image("character.png")
r = 200
x = 450
y = 300

while True:
    for i in range(0, 360, 5): 
        clear_canvas()
        character.draw(x, y)
        update_canvas()
        x = 400 + r * math.cos(math.radians(i))
        y = 300 + r * math.sin(math.radians(i))
        delay(0.01)

update_canvas()
delay(15)
close_canvas()