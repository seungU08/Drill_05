from pico2d import *
import random

Tuk_width, Tuk_height = 1280 , 1024
open_canvas(Tuk_width , Tuk_height)

TUK_Ground = load_image("TUK_GROUND.png")
character = load_image("animation_sheet.png")
point = load_image("hand_arrow.png")

def draw_points(x,y):
    pass

def draw_character(x,y):
    pass

def random_move():
    p = [(random.randint(-500,500)),(random.randint(-300,300))]

    draw_points(p[0],p[1])
    draw_character(p[0],p[1])


while True:
    random_move()

