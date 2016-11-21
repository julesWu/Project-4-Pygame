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
YELLOW    = (255, 255,    0)
RED       = (255,   0,    0)
BLUE      = (  0,   0,  255)
GREEN     = (  0, 255,    0)
ORANGE    = (255, 140,    0)
PURPLE    = (148,   0,  211)

BACKG_COLOR1 = WHITE
BACKG_COLOR2 = BLACK 


class Cube(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y +=3

		if self.rect.y > 610:
			self.rect.y = -25
		

class Player(pygame.sprite.Sprite):
	def __init__(self, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 400
		self.rect.y = 550

def random_color():
	num = random.randint(1,5)
	if num == 1:
		return RED
	elif num == 2:
		return ORANGE
	elif num == 3:
		return PURPLE
	elif num == 4:
		return BLUE 
	elif num == 5:
		return YELLOW	

pygame.init()

#set screen dimensions
screen = pygame.display.set_mode([WIDTH, HEIGHT])

#A list to keep track of all the cubes
cube_list = pygame.sprite.Group()

#A list to keep track of all the different objects in the game.
all_sprites_list = pygame.sprite.Group()

#Actually creating the cubes
for i in range(75):
	cube = Cube(random_color(), 20, 20)

	cube.rect.x = random.randrange(WIDTH - 20)
	cube.rect.y = random.randrange(HEIGHT - 20)

	cube_list.add(cube)
	all_sprites_list.add(cube)

#Create a player
player = Player(20, 20)
all_sprites_list.add(player)

#loop variable
done = False

clock = pygame.time.Clock()

#-----MAIN--LOOP------------MAIN--LOOP----------MAIN--LOOP----------#

while done == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	#Clear the screen first		
	screen.fill(WHITE)

	cube_collide_list = pygame.sprite.spritecollide(player, cube_list, False)

	#Draw all the sprites
	all_sprites_list.draw(screen)

	#moving the cubes down the screen
	cube_list.update()

	#Limit to 20 Frames per second
	clock.tick(20)

	pygame.display.flip()

pygame.quit()



