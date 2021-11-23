import pygame as pg,numpy as np 

tilewall = pg.image.load('Images\H9kT6.jpg')
tilewall = pg.transform.scale(tilewall, (15,15))
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

map1.splitlines()
mapa1 = list()

for line in map1.split("\n"):
    lista = list()
    for c in line:
        if c == "w":
            lista.append(1)
        else:
            lista.append(0)
    mapa1.append(lista)
    
mapa1 = np.array(mapa1)
