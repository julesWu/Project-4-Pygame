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
L_GREEN   = (124, 252,    0)
ORANGE    = (255, 140,    0)
PURPLE    = (148,   0,  211)
D_TURQ	  = (  0, 206,  209)

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

def game_over(collide_list):
	if len(collide_list) > 0:
		return True

def level_1_cubes():
	#Actually creating the cubes
	for i in range(50):
		cube = Cube(random_color(), 25, 25)
		cube.rect.x = random.randrange(WIDTH - 25)
		cube.rect.y = random.randrange(515)
		cube_list.add(cube)
		all_sprites_list.add(cube)

def level_up():
	level += 1
	for i in range(level * 7):
		new_cube = Cube(random_color(), 25, 25)
		new_cube.rect.x = random.randrange(WIDTH - 25)
		new_cube.rect.y = random.randrange(HEIGHT -25)
		cube_list.add(new_cube)
		all_sprites_list.add(new_cube)

def messages(num):
	if num == 1:
		screen.fill(WHITE)
		label = myfont.render("GAME OVER!", 1, BLACK)
		screen.blit(label, (250, 200))
		pygame.display.flip()
	if num == 2:
		screen.fill(WHITE)
		label2 = myfont.render("CUBE RUNNER", 1, BLACK)
		screen.blit(label2, (230, 200))
		pygame.display.flip()


pygame.init()

#movement speed
x_speed = 0
y_speed = 0

#set screen dimensions
screen = pygame.display.set_mode([WIDTH, HEIGHT])

#add cubes into the game
level_1_cubes()

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

level = 1


#-----MAIN--LOOP------------MAIN--LOOP----------MAIN--LOOP----------#

while done == False:
	#Handling movement of the player
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_speed -= 10
			if event.key == pygame.K_RIGHT:
				x_speed += 10
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

	#Draw player
	player_list.draw(screen)


	#detect if player has collided with cubes
	cube_collide_list = pygame.sprite.spritecollide(player, cube_list, False)
	
	cube_list.draw(screen)

	cube_list.update()


	if len(cube_collide_list) == 0 and pygame.time.get_ticks() > 30000 and pygame.time.get_ticks() < 30050:
		level += 1
		for i in range(level * 7):
			new_cube = Cube(random_color(), 25, 25)
			new_cube.rect.x = random.randrange(WIDTH - 25)
			new_cube.rect.y = random.randrange(HEIGHT -25)
			cube_list.add(new_cube)
			all_sprites_list.add(new_cube)

	if len(cube_collide_list) == 0 and pygame.time.get_ticks() > 45000 and pygame.time.get_ticks() < 45050:
		level += 1
		for i in range(level * 7):
			new_cube = Cube(L_GREEN, 25, 25)
			new_cube.rect.x = random.randrange(WIDTH - 25)
			new_cube.rect.y = random.randrange(HEIGHT -25)
			cube_list.add(new_cube)
			all_sprites_list.add(new_cube)

	if len(cube_collide_list) == 0 and pygame.time.get_ticks() > 75000 and pygame.time.get_ticks() < 75050:
		level += 1
		for i in range(level * 7):
			new_cube = Cube(D_TURQ, 25, 25)
			new_cube.rect.x = random.randrange(WIDTH - 25)
			new_cube.rect.y = random.randrange(HEIGHT -25)
			cube_list.add(new_cube)
			all_sprites_list.add(new_cube)

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




