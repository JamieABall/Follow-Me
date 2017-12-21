import pygame
import assets
import player
import partner
import location


from pygame import *
from assets import *
from player import Player
from partner import Partner


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
				player.change_speed(-1, 0)
			elif event.key == pygame.K_RIGHT:
				player.change_speed(1, 0)
			elif event.key == pygame.K_UP:
				player.change_speed(0, -1)
			elif event.key == pygame.K_DOWN:
				player.change_speed(0, 1)
			elif event.key == pygame.K_q or event.key == 27:
				done = True
		
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.change_speed(1, 0)
			elif event.key == pygame.K_RIGHT:
				player.change_speed(-1, 0)
			elif event.key == pygame.K_UP:
				player.change_speed(0, 1)
			elif event.key == pygame.K_DOWN:
				player.change_speed(0, -1)
					
	
	all_sprites.update()
	
	screen.fill(BLACK)
	all_sprites.draw(screen)
	pygame.display.flip()
