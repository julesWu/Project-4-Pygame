#Name: Julia Wu
#Project 4: Pygame
#References: Youtube Tutorials, pygame website, office hours
#More References: Paul Vincent Craven Website for Pygame

import random
import pygame, sys
import time
from pygame.locals import *
from pygame import mixer

#initialize font module and music module
pygame.font.init()
pygame.mixer.init()

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

#Initialize Font Module
pygame.font.init()
#Specify the font that you want and size
myfont = pygame.font.SysFont("monospace", 70)
myfont2 = pygame.font.SysFont("monospace", 30)

#A class definition for the cubes in my game
class Cube(pygame.sprite.Sprite):
	#default constructor for cube class
	def __init__(self, color, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()

	#updating cubes to move them down the screen
	def update(self):
		self.rect.y +=3
		#if they are already off the screen
		if self.rect.y > 610:
			#reset their y position
			self.rect.y = -25

#A class definition for the player in the game
class Player(pygame.sprite.Sprite):
	#variables to adjust the movement of the player
	#initialized to zero
	x_speed = 0
	y_speed = 0
	#default constructor for player class
	def __init__(self, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([width,height])
		self.image.fill(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = 400
		self.rect.y = 550

	#member function to update the movement of the player
	def update(self):
		self.rect.x += self.x_speed
		self.rect.y += self.y_speed
		#Handles the case when player tries to go off the screen
		if self.rect.y < 0:
			self.rect.y = 0
		elif self.rect.x < 0:
			self.rect.x = 0
		elif self.rect.x > WIDTH-20:
			self.rect.x = WIDTH-20
		elif self.rect.y > HEIGHT - 20:
			self.rect.y = HEIGHT - 20

#A function that produces random colors
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

#A class to handle the mechanics of the game
class Game():
	#A list to keep track of all the cubes
	cube_list = None

	#A list to keep track of all the different objects in the game.
	all_sprites_list = None

	#Keep track of level
	level = 1

	#Variable to detect when game is gover
	game_over = False

	#Keep track of score
	score = 0

	#Variable to make sure the score is accurate 
	#each time the person plays
	restart_time = 0

	#The default constructor for the game class
	def __init__(self):
		self.game_over = False
		self.level = 1
		self.score = 0
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

	# member function that deals with the movements in the game
	def run_game_events(self):
		#Handling movement of the player
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if self.game_over:
					self.__init__()
					self.restart_time = pygame.time.get_ticks()
					pygame.mixer.music.play()
			if event.type == pygame.USEREVENT+1:
				self.level += 1
				for i in range(self.level * 10):
					if self.level % 2 == 0:
						new_cube = Cube(random_color(), 25, 25)
						new_cube.rect.x = random.randrange(WIDTH - 25)
						new_cube.rect.y = random.randrange(HEIGHT -25)
						self.cube_list.add(new_cube)
						self.all_sprites_list.add(new_cube)
					else:
						new_cube = Cube(D_TURQ, 25, 25)
						new_cube.rect.x = random.randrange(WIDTH - 25)
						new_cube.rect.y = random.randrange(HEIGHT -25)
						self.cube_list.add(new_cube)
						self.all_sprites_list.add(new_cube)
				pygame.display.flip()

			#When the key is down, adjust player position accordingly
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.player.x_speed -= 10
				if event.key == pygame.K_RIGHT:
					self.player.x_speed += 10
				if event.key == pygame.K_UP:
					self.player.y_speed -= 3
				if event.key == pygame.K_DOWN:
					self.player.y_speed += 3 

			# When the key is up, adjust player position accordingly
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.player.x_speed = 0
				if event.key == pygame.K_RIGHT:
					self.player.x_speed = 0
				if event.key == pygame.K_UP:
					self.player.y_speed = 0
				if event.key == pygame.K_DOWN:
					self.player.y_speed = 0

	#Member function to handle the logic of the game
	def game_logic(self):
		#if the game is not over
		if not self.game_over:
			#update the player's movement
			self.player.update()
			#if the level is less than 4, update cubes using the update function in cube class
			if self.level < 4:
				self.cube_list.update()
			#A list to detect collisions between player and cubes
			cube_collide_list = pygame.sprite.spritecollide(self.player, self.cube_list, False)
			#if the level is greater than 3, speed up the cubes 
			if self.level > 3:
				for cube in self.cube_list:
					cube.rect.y += 5
					if cube.rect.y > 610:
						cube.rect.y = -25

			#if there is a collision, the game is over
			if len(cube_collide_list) > 0:
				self.game_over = True

	#Member function to print messages to the screen
	def display_messages(self, screen):
		screen.fill(WHITE)

		#if the game is not over
		if not self.game_over:
			#draw all the objects on the screen
			self.all_sprites_list.draw(screen)
			#keep track of score
			self.score = pygame.time.get_ticks()
			score_text = myfont2.render("SCORE: " + str(self.score - self.restart_time), 1, BLACK)
			#print score onto screen
			level_text = myfont2.render("LEVEL: " + str(self.level), 1, BLACK)
			screen.blit(level_text, (15, 35))
			screen.blit(score_text, (15, 15))

		#if the game is over
		elif self.game_over:
			#print game over
			label = myfont.render("GAME OVER! ", 1, BLACK)
			#print click to restart
			restart = myfont.render("Click to restart.", 1, BLACK)
			#print player score
			score_label = myfont.render("SCORE: " + str(self.score - self.restart_time), 1, BLACK)
			#Display these messages to the screen
			screen.blit(score_label, (265, 100))
			screen.blit(label, (275, 200))
			screen.blit(restart, (250, 300))
		

		pygame.display.flip()

#main loop
def main():
	#initialize pygame mixer 
	pygame.mixer.pre_init(44100, 16, 2, 4096)
	#initialize pygame
	pygame.init()
	#set screen
	screen = pygame.display.set_mode([WIDTH, HEIGHT])
	#set caption of the screen
	pygame.display.set_caption("Cube Runner")
	#initialize loop variable
	done = False
	#initialize game clock
	clock = pygame.time.Clock()
	#increase cubes every 25 seconds
	pygame.time.set_timer(USEREVENT+1, 25000)

	#create an instance of game
	game = Game()

	#Play background music in game
	if not game.game_over:
		pygame.mixer.music.load("background.wav")
		pygame.mixer.music.set_volume(0.5)
		pygame.mixer.music.play(5)

	#while the game is not done
	while not done:
		#Run the events in the game
		done = game.run_game_events()

		#Run game logic
		game.game_logic()

		#dispaly the messages of the game on the screen
		game.display_messages(screen)

		#set frames
		clock.tick(20)

		#make the music stop
		if game.game_over:
			pygame.mixer.music.stop()

	pygame.quit()

#Calling the main function to start game
if __name__ == "__main__":
	main()
