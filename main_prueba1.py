import pygame
import time
import random
pygame.init() # Inicia pygame. Abre una ventana

# Resolución
display_width = 1080
display_height = 720

# Establecemos colores del juego
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)


gameDisplay = pygame.display.set_mode((display_width,display_height)) # Establecemos resolución
pygame.display.set_caption('evilelmo: The Game') # Establecemos título de la ventana
clock = pygame.time.Clock() # Reloj del juego

# Personaje:
carImg = pygame.image.load('images\cursedmario50.png') # Cargamos imagen coche
pj_width = 50
pj_heith = 50

# Enemigo movible:
elmoImg = pygame.image.load('images\evilelmotiny.png') # Cargamos enemigo
elmo_width = 50
elmo_height = 43

# Enemigo:
#speed = [1,1]
evilelmoImg = pygame.image.load('images\evilelmo710.png')
elmorect = evilelmoImg.get_rect()

# Funciones:

def square(squarex,squarey,squarew,squareh, color):
    pygame.draw.rect(gameDisplay, color, [squarex, squarey, squarew, squareh])


def car(x,y):   # función que blitea el car en x,y
    gameDisplay.blit(carImg,(x,y))

def elmo(x,y):
    gameDisplay.blit(elmoImg,(x,y))

def elmoed():
    run = True
    while run:
        pygame.time.delay(2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: run=False
        elmorect = elmorect.move(speed)
        if elmorect.left < 0 or elmorect.right > width:
            speed[0]=-speed[0]
        if elmorect.top < 0 or elmorect.bottom > height:
            speed[1]=-speed[1]
        gameDisplay.blit(evilelmoImg,elmorect)
        pygame.display.update()

def crash():
    message_display("You've been elmoed :)", black)

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text, color):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (display_width/2, display_height/2)
    gameDisplay.blit(evilelmoImg,elmorect)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)

    game_loop()


def game_loop():

    # Posición incial del personaje
    x = (display_width * 0.45)  # Posición inicial del coche
    y = (display_height * 0.7)

    x_change_left = 0
    x_change_right = 0
    y_change_up = 0
    y_change_down = 0

    sp = 15 # speed

    # Posición inicial de elmo:

    elx = random.randrange(0, display_width)
    ely = random.randrange(0, display_height)

    el_speedx = 10*random.choice([1,-1])
    el_speedy = 10*random.choice([1,-1])
    

    # Comienza el juego:
    gameExit = False


    while not gameExit:  # Función principal del juego
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pinchar la x es pygame.QUIT
                pygame.quit()
                quit()

            print(event) # Vemos en consola los imputs

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
        x += x_change_left + x_change_right   # Movemos el personaje
        if x_change_left != 0 and x_change_right != 0: # Si pulsamos dos teclas contrarias a la vez
            x += x_prior
        y += y_change_up + y_change_down
        if y_change_up != 0 and y_change_down != 0:
            y += y_prior      

        # Fondo:
        gameDisplay.fill(red)  # Color mate en la pantalla

        # Enemigo:

        # if elmorect.top < 0 or elmorect.bottom > display_height:
        #     el_speedy = -el_speedy
        # if elmorect.left < 0 or elmorect.right > display_width:
        #     el_speedx = -el_speedx

        if elx > display_width - elmo_width or elx < 0:
            el_speedx = -el_speedx
        if ely > display_height - elmo_height or ely < 0:
            el_speedy = -el_speedy

        elmo(elx,ely)
        elx += el_speedx
        ely += el_speedy

        # Muestra el personaje
        car(x,y)

        # Colisión con enemigo:

        if x in range(elx,elx+elmo_width) and y in range(ely, ely+elmo_height):
            crash()
        
        if x + pj_width in range(elx,elx+elmo_width) and y in range(ely, ely+elmo_height):
            crash()
        if y + pj_heith in range(ely, ely+elmo_height) and x in range(elx,elx+elmo_width):
            crash()
        if y + pj_heith in range(ely, ely+elmo_height) and x + pj_width in range(elx,elx+elmo_width):
            crash()

        # Definir límites en el escenario:
        if x > display_width - pj_width:
            x = display_width - pj_width
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if y > display_height - pj_heith:
            y = display_height - pj_heith

        pygame.display.update() # Puedes usar update o flip
        clock.tick(60) # fps


# Ejecución del juego:

game_loop()
pygame.quit()
quit()