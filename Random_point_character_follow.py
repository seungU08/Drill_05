from pico2d import *
import random

Tuk_width, Tuk_height = 1280, 1024
open_canvas(Tuk_width , Tuk_height)

TUK_Ground = load_image("TUK_GROUND.png")
character = load_image("animation_sheet.png")
point = load_image("hand_arrow.png")

def draw_points(x,y):
    point.draw(x,y)

def random_move():
    global x,y,frame
    x1,y1 = x,y
    x2,y2 = random.randint(0,1280),random.randint(0,1024)


    for i in range(0,100,4):
        clear_canvas()
        TUK_Ground.draw(Tuk_width//2,Tuk_height//2)
        draw_points(x2, y2)
        t = i /100
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        character.clip_draw(frame*100,100*1,100,100,x,y)
        update_canvas()

        frame = (frame+1)%8
        delay(0.05)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

running = True
frame = 1
x, y = Tuk_width/2, Tuk_height/2

while running:
    clear_canvas()
    TUK_Ground.draw(Tuk_width//2,Tuk_height//2)
    character.clip_draw(frame*100,100*1,100,100,x,y)
    update_canvas()

    frame = (frame+1)%8
    random_move()
    handle_events()
    delay(0.05)

close_canvas()
