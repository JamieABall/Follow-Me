import pygame
import pygame.sprite

import assets
import location

from location import Location
from pygame import *
from pygame.sprite import *

from assets import *

class Player(Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = Surface([15, 15])
		self.image.fill(WHITE)
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.dx = 0
		self.dy = 0
		self.cur_loc = Location(x, y)
		self.prev_loc = Location()
		
	
	def ismoving(self):
		return self.dx != 0 or self.dy != 0
		
	def change_speed(self, vx=0, vy=0):
		if not self.ismoving():
			self.prev_loc = self.cur_loc.make_copy()
		self.dx += vx
		self.dy += vy 
		
		
	def update(self):
		self.cur_loc.setx(self.rect.x)
		self.cur_loc.sety(self.rect.y)
		self.rect.x += self.dx
		self.rect.y += self.dy
			
