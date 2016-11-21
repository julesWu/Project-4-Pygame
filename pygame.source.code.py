#Julia Wu
#UMID: 38632603
#uniquename: shuyue
#References:

import random
import pygame, sys
import time
from pygame.locals import *

#Defining some constants for the game:
WIDTH = 800
HEIGHT = 600


#Define Colors
BLACK     = (  0,   0,    0)
GRAY 	  = (185, 185,  185)
WHITE     = (255, 255,  255)
YELLOW    = (155, 155,    0)
RED       = (255,   0,    0)
BLUE      = (  0,   0,  255)
GREEN     = (  0, 255,    0)
L_YELLOW  =	(155, 155,    0)
L_GREEN   = ( 20,  175,  20)
L_BLUE    = ( 20,   20, 175)
L_RED     = (175,   20,  20)


BACKG_COLOR1 = WHITE
BACKG_COLOR2 = BLACK 

class Cube(pygame.sprite.Sprite):
	def _init_(self, color, width, height):

		self.image = pygame.surface([width, height])

		self.image.fill(color)

		self.rect = self.image.get_rect()

pygame.init()

Cube_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()

for i in range(75):
	cube = Cube(BLUE, 20, 20)

	cube.rect.x = random.randrange(WIDTH)
	cube.rect.y = random.randrange(HEIGHT)

	Cube_list.add(cube)
	all_sprites_list.add(cube)
	
