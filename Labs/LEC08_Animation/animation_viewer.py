from pico2d import *


SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FRAME_SIZE = 100
FRAME_COUNT = 8
FRAME_WIDTH = FRAME_SIZE
FRAME_HEIGHT = FRAME_SIZE
ANIMATION_COUNT = 4
SPRITE_ROW_COUNT = ANIMATION_COUNT
FIRST_SPRITE_ROW = SPRITE_ROW_COUNT - 1
VIEWER_CENTER = (SCREEN_CENTER_X, SCREEN_CENTER_Y)
REPEAT_COUNT = 5
DISPLAY_SIZE = 360
FRAME_DELAY = 0.08
REST_DELAY = 1.0
SCREEN_CENTER_X = SCREEN_WIDTH // 2
SCREEN_CENTER_Y = SCREEN_HEIGHT // 2


open_canvas(SCREEN_WIDTH, SCREEN_HEIGHT)
character = load_image('animg.png')


def draw_frame(animation_index, frame_index):
	clear_canvas()
	character.clip_draw(
		sprite_column(frame_index) * FRAME_WIDTH,
		sprite_row(animation_index) * FRAME_HEIGHT,
		FRAME_WIDTH,
		FRAME_HEIGHT,
		*VIEWER_CENTER,
		DISPLAY_SIZE,
		DISPLAY_SIZE,
	)
	update_canvas()


def sprite_row(animation_index):
	return FIRST_SPRITE_ROW - animation_index


def sprite_column(frame_index):
	return frame_index


def should_close():
	for event in get_events():
		if event.type == SDL_QUIT:
			return True
		if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			return True
	return False


try:
	while True:
		for animation_index in range(ANIMATION_COUNT):
			for _ in range(REPEAT_COUNT):
				for frame_index in range(FRAME_COUNT):
					draw_frame(animation_index, frame_index)
					if should_close():
						raise SystemExit
					delay(FRAME_DELAY)

			clear_canvas()
			update_canvas()
			delay(REST_DELAY)
			if should_close():
				raise SystemExit
finally:
	close_canvas()
