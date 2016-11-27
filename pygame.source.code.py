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

#Initialize Font Module
pygame.font.init()
#Specify the font that you want and size
myfont = pygame.font.SysFont("monospace", 75)


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
	x_speed = 0
	y_speed = 0
	def __init__(self, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 400
		self.rect.y = 550

	def update(self):
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed

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

class Game():
	#A list to keep track of all the cubes
	cube_list = None

	#A list to keep track of all the different objects in the game.
	all_sprites_list = None

	#Keep track of level
	level = 1

	#Variable to detect when game is gover
	game_over = False

	def __init__(self):
		self.game_over = False
		self.cube_list = pygame.sprite.Group()
		self.all_sprites_list = pygame.sprite.Group()

		#create the cubes in the game
		for i in range(50):
			cube = Cube(random_color(), 25, 25)
			cube.rect.x = random.randrange(WIDTH - 25)
			cube.rect.y = random.randrange(515)
			self.cube_list.add(cube)
			self.all_sprites_list.add(cube)

		#Create player
		self.player = Player(20, 20)
		self.all_sprites_list.add(self.player)

	def run_game_events(self):
		#Handling movement of the player
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.game_over:
					self.__init__()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.player.x_speed -= 10
				if event.key == pygame.K_RIGHT:
					self.player.x_speed += 10
				if event.key == pygame.K_UP:
					self.player.y_speed -= 3
				if event.key == pygame.K_DOWN:
					self.player.y_speed += 3 

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.player.x_speed = 0
				if event.key == pygame.K_RIGHT:
					self.player.x_speed = 0
				if event.key == pygame.K_UP:
					self.player.y_speed = 0
				if event.key == pygame.K_DOWN:
					self.player.y_speed = 0


	def game_logic(self):
		if not self.game_over:
			self.player.update()
			if pygame.time.get_ticks() < 85000:
				self.cube_list.update()
			cube_collide_list = pygame.sprite.spritecollide(self.player, self.cube_list, False)

			if len(cube_collide_list) == 0 and pygame.time.get_ticks() > 30000 and pygame.time.get_ticks() < 30050:
				self.level += 1
				for i in range(self.level * 10):
					new_cube = Cube(random_color(), 25, 25)
					new_cube.rect.x = random.randrange(WIDTH - 25)
					new_cube.rect.y = random.randrange(HEIGHT -25)
					self.cube_list.add(new_cube)
					self.all_sprites_list.add(new_cube)

			if len(cube_collide_list) == 0 and pygame.time.get_ticks() > 45000 and pygame.time.get_ticks() < 45050:
				self.level += 1
				for i in range(self.level * 10):
					new_cube = Cube(L_GREEN, 25, 25)
					new_cube.rect.x = random.randrange(WIDTH - 25)
					new_cube.rect.y = random.randrange(HEIGHT -25)
					self.cube_list.add(new_cube)
					self.all_sprites_list.add(new_cube)

			if len(cube_collide_list) == 0 and pygame.time.get_ticks() > 75000 and pygame.time.get_ticks() < 75050:
				self.level += 1
				for i in range(self.level * 10):
					new_cube = Cube(D_TURQ, 25, 25)
					new_cube.rect.x = random.randrange(WIDTH - 25)
					new_cube.rect.y = random.randrange(HEIGHT -25)
					self.cube_list.add(new_cube)
					self.all_sprites_list.add(new_cube)	

			if pygame.time.get_ticks() > 85000:
				for cube in self.cube_list:
					cube.rect.y += 5
					if cube.rect.y > 610:
						cube.rect.y = -25	

			if len(cube_collide_list) > 0:
				self.game_over = True

	def display_messages(self, screen):
		screen.fill(WHITE)

		if self.game_over:
			label = myfont.render("GAME OVER!", 1, BLACK)
			screen.blit(label, (100, 200))
		
		if not self.game_over:
			screen.fill(WHITE)
			self.all_sprites_list.draw(screen)
			
		pygame.display.flip()

def main():
	pygame.init()
	screen = pygame.display.set_mode([WIDTH, HEIGHT])
	pygame.display.set_caption("Cube Runner")
	done = False
	clock = pygame.time.Clock()

	game = Game()

	while not done:
		done = game.run_game_events()

		game.game_logic()

		game.display_messages(screen)

		clock.tick(20)

	pygame.quit()

#Calling the main function to start game
if __name__ == "__main__":
	main()
