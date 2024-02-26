import pygame
from info import *
from arduino import *
from pygame.locals import *
from tkinter import *

pygame.init()

fenetre=pygame.display.set_mode((640,480))
#fond= pygame.image.load("image.png").convert()
font= pygame.font.Font(None,50)
#fenetre.blit(fond,(0,0))
pygame.display.flip()

speed=distance()
disp= font.rendr(f"Speed: {speed}", True ,(0,0,0))
text_disp= disp.get_rect(center=(400,300))

fenetre.fill((255,255,255))
fenetre.blit(disp,text_disp)
pygame.display.update()

for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


#todo cree deux base de donnée qui contient les informations de chaque point et une table qui contient les distances entre deux points comme par exemple (AB 2cm)


