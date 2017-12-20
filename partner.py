import pygame
import pygame.sprite
import assets
import location
import locationqueue

from pygame import *
from pygame.sprite import *
from assets import *
from location import Location
from locationqueue import LocationQueue

class Partner(Sprite):
	def __init__(self, x, y, target):
		super().__init__()
		
		self.image = Surface([15, 15])
		self.image.fill(BLUE)
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.dx = 0
		self.dy = 0
		
		self.cur_loc = Location(x, y)
		self.path = LocationQueue()
		self.target = target
		
	def update_target_position(self):
		temp = Location(self.rect.x, self.rect.y)
		
		#exclusive x movement
		if self.target.cur_loc.x_gr(self.cur_loc):
			temp.setx(self.target.cur_loc.xc - 50)
		
		if self.target.cur_loc.x_gr(self.cur_loc) and self.target.dx < 0:
			temp.setx(self.target.cur_loc.xc + 50)
			
		if self.target.cur_loc.x_lt(self.cur_loc):
			temp.setx(self.target.cur_loc.xc + 50)
		
		if self.target.cur_loc.x_lt(self.cur_loc) and self.target.dx > 0:
			temp.setx(self.target.cur_loc.xc - 50)
		
		#exclusive y movement
		if self.target.cur_loc.y_gr(self.cur_loc):
			temp.setx(self.target.prev_loc.xc)
			temp.sety(self.target.cur_loc.yc - 50)
		
		if self.target.cur_loc.y_lt(self.cur_loc):
			temp.setx(self.target.prev_loc.xc)
			temp.sety(self.target.cur_loc.yc + 50)
			
		if self.target.cur_loc.y_gr(self.cur_loc) and self.target.dx == 0 and self.target.dy < 0:
			temp.sety(self.target.cur_loc.yc + 50)
			
		if self.target.cur_loc.y_lt(self.cur_loc) and self.target.dx == 0 and self.target.dy > 0:
			temp.sety(self.target.cur_loc.yc - 50)
			
		#xy movement
		if self.target.cur_loc.y_gr(self.cur_loc) and self.target.dx < 0:
			temp.sety(self.target.prev_loc.yc)

		if self.target.cur_loc.y_gr(self.cur_loc) and self.target.dx > 0:
			temp.sety(self.target.prev_loc.yc)
			
		if self.target.cur_loc.y_lt(self.cur_loc) and self.target.dx < 0:
			temp.sety(self.target.prev_loc.yc)
		
		if self.target.cur_loc.y_lt(self.cur_loc) and self.target.dx > 0:
			temp.sety(self.target.prev_loc.yc)
			
		self.path.enqueue(temp)
	
	def follow_target(self):
		if not self.path.is_empty():
			target_loc = self.path.dequeue()
			
			if self.cur_loc.x_lt(target_loc):
				self.dx = 1
			elif self.cur_loc.x_gr(target_loc):
				self.dx = -1
			elif self.cur_loc.xc == target_loc.xc:
				self.dx = 0
			
			if self.cur_loc.y_lt(target_loc):
				self.dy = 1
			elif self.cur_loc.y_gr(target_loc):
				self.dy = -1
			elif self.cur_loc.yc == target_loc.yc:
				self.dy = 0
		
	def update(self):
		self.cur_loc.setx(self.rect.x)
		self.cur_loc.sety(self.rect.y)
		self.update_target_position()
		self.follow_target()
		self.rect.x += self.dx
		self.rect.y += self.dy
