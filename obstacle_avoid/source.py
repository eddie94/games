import pygame as pg
import sys
from random import randint

def quit():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

def check_speed(speed):

    move = randint(0,1)
    new_speed = [-1,1]

    if speed[0] == 0:
        speed[0] = new_speed[move]
    if speed[1] == 0:
        speed[1] = new_speed[move]

def input_box():

    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    input_box = pg.Rect(100, 100, 140, 32)

    ment = 'YOU ARE THE BEST SCORE!!!'
    ment_surface = ment_font.render(ment,False,(0,0,0))

    active = False
    text = ''
    done = False

    while not done:
        for event in pg.event.get():
            quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        return text
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode


        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y))
        screen.blit(ment_surface, (5,300))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()

white = 255,255,255
blue = 0, 128, 255

pg.init()
pg.font.init()

screen = pg.display.set_mode((600,600))
font = pg.font.SysFont('Arial',32)
ment_font = pg.font.SysFont('Arial', 50)