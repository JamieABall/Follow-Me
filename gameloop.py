"""@author: Jamison Ball
   @date: 12.23.2017
   @last updated: 12.23.2017"""

import pygame
import assets
import player
import partner
import location


from pygame import *
from assets import *
from player import Player
from partner import Partner

left = False
right = False
up = False
down = False

def dbkeys():
	flags = ''
	
	if left:
		flags += 'l'
	if right:
		flags += 'r'
	if up:
		flags += 'u'
	if down:
		flags += 'd'
	print(flags)
	
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

pygame.display.set_caption('Player Test')

all_sprites = pygame.sprite.Group()

player = Player(100, 50)
partner = Partner(50, 50, player)
#add line about player.walls later
all_sprites.add(player)
all_sprites.add(partner)

clock = pygame.time.Clock()

done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if not right and not up and not down:
					player.change_speed(-10, 0)
					left = True
			elif event.key == pygame.K_RIGHT:
				if not left and not up and not down:
					player.change_speed(10, 0)
					right = True
			elif event.key == pygame.K_UP:
				if not left and not right and not down:
					player.change_speed(0, -10)
					up = True
			elif event.key == pygame.K_DOWN:
				if not left and not right and not up:
					player.change_speed(0, 10)
					down = True
			elif event.key == pygame.K_q or event.key == 27:
				done = True
		
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				if left:
					player.change_speed(10, 0)
					left = False
			elif event.key == pygame.K_RIGHT:
				if right:
					player.change_speed(-10, 0)
					right = False
			elif event.key == pygame.K_UP:
				if up:
					player.change_speed(0, 10)
					up = False
			elif event.key == pygame.K_DOWN:
				if down:
					player.change_speed(0, -10)
					down = False
					
	
	all_sprites.update()
	
	screen.fill(BLACK)
	all_sprites.draw(screen)
	pygame.display.flip()
	clock.tick(60)
