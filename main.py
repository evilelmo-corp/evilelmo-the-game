import sys, pygame as pg, time, random, numpy as np
import mapa
pg.init()
size = 1080,720
screen = pg.display.set_mode(size)
width,height = size
#board = pg.image.load('Images\Plano-de-casa-de-3-dormitorios-2-baño-y-jardín-frontal.jpg')
#board = pg.transform.scale(board, (1080,720))

black = (0,0,0)
pg.display.set_caption("Juego Héctor")
clock = pg.time.Clock()
elmo = pg.image.load('Images\evilelmo.png')
elmo = pg.transform.scale(elmo, (50,43))
elmorect = elmo.get_rect()
def car(pos):
    screen.blit(elmo,(pos))
pos = [0, 0]
x_change_left=0
x_change_right=0
y_change_up=0
y_change_down=0
sp = 0.5
run = True
def tiles(mapita):
    global tilewall
    for y, line in enumerate(mapita):
        for x, c in enumerate(line):
            if c == 1:
                screen.blit(mapa.tilewall, (x * 32, y * 32))
while run:
    screen.fill(black)
    car(pos)
    tiles(mapa.mapa1)
    for event in pg.event.get():
        if event.type == pg.QUIT: run=False
        keys = pg.key.get_pressed()
        # move_ticker = 0
        if event.type == pg.KEYDOWN:  # Controles
            if event.key == pg.K_LEFT:
                x_prior = -sp
                x_change_left = -sp
            if event.key == pg.K_RIGHT:
                x_prior = sp
                x_change_right = sp
            if event.key == pg.K_UP:
                y_prior = -sp
                y_change_up = -sp
            if event.key == pg.K_DOWN:
                y_prior = sp
                y_change_down = sp

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                x_change_left = 0
            if event.key == pg.K_RIGHT:
                x_change_right = 0
            if event.key == pg.K_UP:
                y_change_up = 0
            if event.key == pg.K_DOWN:
                y_change_down = 0
    pos[0] += x_change_left + x_change_right
    if x_change_left != 0 and x_change_right != 0:
        pos[0] += x_prior
    pos[1] += y_change_up + y_change_down
    if y_change_up != 0 and y_change_down != 0:
        pos[1] += y_prior  
    
    
    pg.display.flip()
pg.quit()
