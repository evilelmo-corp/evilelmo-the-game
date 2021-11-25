import pygame
import pygame as pg
import numpy as np
from pygame.constants import CONTROLLER_BUTTON_INVALID

pygame.init()
clock = pygame.time.Clock()

screen_width, screen_height = 800,460
screen = pygame.display.set_mode((screen_width,screen_height))

# Establecemos colores del juego
black = (0,0,0)
dark_grey = (30,30,30)
white = (255,255,255)
red = (255,0,0)

# Personaje:
pjx = 60
pjy = 60
pj_width = 30
pj_heith = 30
pjImg = pygame.image.load('images\cursedmario50.png')
pjImg = pygame.transform.scale(pjImg, (pj_width,pj_heith))
pjRect = pygame.Rect(pjx,pjy,pj_width,pj_heith)


# Parámetros iniciales movimiento pj:
x_change_left = 0
x_change_right = 0
y_change_up = 0
y_change_down = 0

sp = 10 # speed

# Goal tile:
goalPosx = screen_width-(screen_width*0.1)
goalPosy = screen_height-(screen_height*0.165)

goalImg = pygame.image.load('images\green-square.png')
goalImg = pygame.transform.scale(goalImg, (50,50))
goalRect = pygame.Rect(goalPosx,goalPosy,50,50)

# Wall:
col_tol=10
tilex=10
tiley=10
tile_width = 15
tile_height = 15
tile = pygame.image.load('images\tilewall.jpg')
tile = pygame.transform.scale(tile, (15,15))
tileRect = pygame.Rect(tilex, tiley, 15,15)

map1 ="""                             
                             
wwwww  www   www  ww   ww  ww
w             w             w
w                           w
w    wwwwww    wwwww      www
www    w                  w w
w      w          w         w
w   wwwww     wwwwwww      ww
w      wwwwww     w     w   w
w    w      w   www  wwww   w
w      w          w     w   w
w   wwwwww www wwww     w   w
w     w              ww w   w
w                           w
wwwwwwwwwwwwwwwwwwwwwwwwwwwww"""

mapa = list()
for line in map1.split("\n"):
    lista = list()
    for c in line:
        if c == "w":
            lista.append(1)
        else:
            lista.append(0)
    mapa.append(lista)

mapa = np.array(mapa)

# def movimiento pj:
def movpj(event):
    global pjx, pjy
    

# def tiles:
def tiles(mapa):
    global tile, pjx, pjy
    for y, line in enumerate(mapa):
        for x, c in enumerate(line):
            if c == 1:
                tilex = x*32 + 5 
                tiley = y*32 - 45
                tileRect = pygame.Rect(tilex, tiley, 15,15)
                screen.blit(tile, tileRect)

                # Colisión con tiles:
                # if pjRect.colliderect(tileRect):   # Con collide (no funciona para movimiento manual?)
                #     if abs(tileRect.top - pjRect.bottom) < col_tol:
                #         pjy = tileRect.top - pj_heith
                
                # Colision con tiles y bliteo del personaje

                if pjRect.right > tileRect.left and pjRect.right < tileRect.right/2:
                    pjx = tileRect.left

                pjRect = pygame.Rect(pjx,pjy,pj_width,pj_heith)
                screen.blit(pjImg,pjRect)
                
                # if pjRect.left < 0:
                #     pjx = 0
                # if pjRect.bottom > screen_height:
                #     pjy = screen_height - pj_heith
                # if pjRect.top < 0:
                #     pjy = 0

# Se ejecuta el juego:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Controles pj:
        if event.type == pygame.KEYDOWN:  # Controles
            if event.key == pygame.K_LEFT:
                x_prior = -sp
                x_change_left = -sp
            if event.key == pygame.K_RIGHT:
                x_prior = sp
                x_change_right = sp
            if event.key == pygame.K_UP:
                y_prior = -sp
                y_change_up = -sp
            if event.key == pygame.K_DOWN:
                y_prior = sp
                y_change_down = sp

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change_left = 0
            if event.key == pygame.K_RIGHT:
                x_change_right = 0
            if event.key == pygame.K_UP:
                y_change_up = 0
            if event.key == pygame.K_DOWN:
                y_change_down = 0
        
     # Movimiento del personaje:
    pjx += x_change_left + x_change_right 
    if x_change_left != 0 and x_change_right != 0: # Si pulsamos dos teclas contrarias a la vez
        pjx += x_prior
    pjy += y_change_up + y_change_down
    if y_change_up != 0 and y_change_down != 0:
        pjy += y_prior 

    # Definir límites en el escenario:
    if pjRect.right > screen_width:
        pjx = screen_width - pj_width
    if pjRect.left < 0:
        pjx = 0
    if pjRect.bottom > screen_height:
        pjy = screen_height - pj_heith
    if pjRect.top < 0:
        pjy = 0

    screen.fill(dark_grey)

    # Bliteo goal:
    screen.blit(goalImg,goalRect)

    # Probando colisión con goal:
    if pjx + pj_width > goalPosx and pjx + pj_width < goalPosx + (50/2) and pjy + pj_heith > goalPosy and pjy < goalPosy+50 :
        pjx = goalPosx -pj_width

    # if pjRect.right > goalRect.left and pjRect.right < goalRect.right/2:
    #     pjx = goalRect.left

    # Bliteo personaje:
    pjRect = pygame.Rect(pjx,pjy,pj_width,pj_heith)
    screen.blit(pjImg,pjRect)

    # Bliteo tiles:
    for y, line in enumerate(mapa):
        for x, c in enumerate(line):
            if c == 1:
                tilex = x*32 + 5 
                tiley = y*32 - 45
                tileRect = pygame.Rect(tilex, tiley, tile_width,tile_height)
                screen.blit(tile, tileRect)


                if pjx + pj_width > tilex and pjx + pj_width < tilex + (tile_width/2) and pjy + pj_heith > tiley and pjy < tiley+tile_height :
                    pjx = tilex -pj_width


                # if pjRect.right > tileRect.left and pjRect.right < tileRect.right/2:
                #     pjx = tileRect.left

 

                # if pjx < tilex and pjx > tilex + (tile_width/2):
                #     pjx = tilex + tile_width

                pjRect = pygame.Rect(pjx,pjy,pj_width,pj_heith)
                screen.blit(pjImg,pjRect)
                

                # # Colisión con tiles:
                # if pjRect.colliderect(tileRect):
                #     if abs(tileRect.top - pjRect.bottom) < col_tol:
                #         pjy = tileRect.top - pj_heith

    pygame.display.update()
    clock.tick(60)