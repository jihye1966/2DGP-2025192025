from pico2d import *

open_canvas()
character = load_image("character.png")

x = 100
y = 500

state = 0 #0-right, 1 - down, 2 - left, 3 - up
while True:
    if state == 0:
        while x < 700:
             clear_canvas()
             character.draw(x, y)
             update_canvas()
             x += 2
             delay(0.01)
        if x == 700 and y == 500:
            state = 1
        
    if state == 1:
        while y > 100:
             clear_canvas()
             character.draw(x, y)
             update_canvas()
             y -= 2
             delay(0.01)
        if x == 700 and y == 100:
            state = 2

    if state == 2:
        while x > 100:
             clear_canvas()
             character.draw(x, y)
             update_canvas()
             x -= 2
             delay(0.01)
        if x == 100 and y == 100:
            state = 3

    if state == 3:
        while y < 500:
             clear_canvas()
             character.draw(x, y)
             update_canvas()
             y += 2
             delay(0.01)
        if x == 100 and y == 500:
            state = 0


update_canvas()
delay(15)
close_canvas()