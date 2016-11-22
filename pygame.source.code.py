#Julia Wu
#UMID: 38632603
#uniquename: shuyue
#References:

import random
import pygame, sys
import time
from pygame.locals import *

#initialize font module
pygame.font.init()

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

#A list to keep track of all the cubes
cube_list = pygame.sprite.Group()

#A list to keep track of all the different objects in the game.
all_sprites_list = pygame.sprite.Group()

#A list to track the player
player_list = pygame.sprite.Group()

class Cube(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

	def update(self):
		self.rect.y +=6
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

def game_over(collide_list):
	if len(collide_list) > 0:
		return True

def create_cubes():
	#Actually creating the cubes
	for i in range(75):
		cube = Cube(random_color(), 25, 25)

		cube.rect.x = random.randrange(WIDTH - 20)
		cube.rect.y = random.randrange(HEIGHT - 20)

		cube_list.add(cube)
		all_sprites_list.add(cube)

def messages(num):
	if num == 1:
		screen.fill(WHITE)
		label = myfont.render("GAME OVER!", 1, BLACK)
		screen.blit(label, (250, 200))
		pygame.display.flip()
	if num == 2:
		screen.fill(WHITE)
		label2 = myfont.render("CUBE RUNNER", 1, BLACK)
		screen.blit(label2, (250, 200))
		pygame.display.flip()


pygame.init()

#movement speed
x_speed = 0
y_speed = 0

#set screen dimensions
screen = pygame.display.set_mode([WIDTH, HEIGHT])

#add cubes into the game
create_cubes()

#Create a player
player = Player(20, 20)
player_list.add(player)
all_sprites_list.add(player)

#loop variable
done = False

#Initialize Font Module
pygame.font.init()
#Specify the font that you want and size
myfont = pygame.font.SysFont("monospace", 75)

#Keep track of time
clock = pygame.time.Clock()

#Displays Game Name at start
messages(2)
#Pauses program for a few seconds before running game
pygame.time.delay(1500)


#-----MAIN--LOOP------------MAIN--LOOP----------MAIN--LOOP----------#

while done == False:
	#Handling movement of the player
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed -= 7
			if event.key == pygame.K_RIGHT:
				x_speed += 7
			if event.key == pygame.K_UP:
				y_speed -= 3
			if event.key == pygame.K_DOWN:
				y_speed += 3 

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				x_speed = 0
			if event.key == pygame.K_RIGHT:
				x_speed = 0
			if event.key == pygame.K_UP:
				y_speed = 0
			if event.key == pygame.K_DOWN:
				y_speed = 0

	#Clear the screen first		
	screen.fill(WHITE)

	#Updating movement of the player based on the keys
	player.rect.x += x_speed
	player.rect.y += y_speed

	#detect if player has collided with cubes
	cube_collide_list = pygame.sprite.spritecollide(player, cube_list, False)

	#Draw player
	player_list.draw(screen)

	#Draw cubes
	cube_list.draw(screen)

	#moving the cubes down the screen
	cube_list.update()

	#GAME LOGIC
	if game_over(cube_collide_list):
		messages(1)
		done = True
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if event.type == KEYDOWN:
					if event.key == K_SPACE:
						done = False
					else:
						pygame.QUIT()
		
	
	#Limit to 20 Frames per second
	clock.tick(20)

	pygame.display.flip()




