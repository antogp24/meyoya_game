import pygame
import collisions
from pygame.locals import *

class Input:
	def __init__(self):
		self.Left = False
		self.Right = False
		self.Up = False
		self.Down = False

class Player:
	def __init__(self, p_speed_x, p_texture_scalar):
		self.speed_x = p_speed_x
		self.momentum_y = 0
		self.air_timer = 0
		self.input = Input()
		self.texture_scalar = p_texture_scalar
		self.texture = pygame.image.load("data/gfx/monda.png").convert_alpha()
		self.rect = pygame.Rect((0, 0), (self.texture.get_width() * self.texture_scalar, self.texture.get_height() * self.texture_scalar))
	
	def scale_textures(self):
		self.texture = pygame.transform.scale(
			self.texture, 
			(
				self.texture.get_width()*self.texture_scalar, self.texture.get_height()*self.texture_scalar
			))

	def render(self, window):
		window.blit(self.texture, (self.rect.x, self.rect.y))

	def movement(self, p_tiles):
		intended_movement = [0, 0]
		if self.input.Left:
			intended_movement[0] -= self.speed_x
		if self.input.Right:
			intended_movement[0] += self.speed_x
		if self.input.Up:
			# Can jump off an edge before 8 frames
			if self.air_timer < 8:
				self.momentum_y = -16
		if self.input.Down:
			self.momentum_y += 8
		
		intended_movement[1] += self.momentum_y
		self.momentum_y += 1.6
		if self.momentum_y > 16:
			self.momentum_y = 16

		self.rect, colls = collisions.move(self.rect, p_tiles, intended_movement)
		if colls['bottom']:
			self.momentum_y = 0
			self.air_timer = 0
		else:
			self.air_timer += 1

	def input_check(self, event, left, right, up, down):
		if event.type == KEYDOWN:
			if event.key == left:
				self.input.Left = True
			if event.key == right:
				self.input.Right = True
			if event.key == up:
				self.input.Up = True
			if event.key == down:
				self.input.Down = True

		if event.type == KEYUP:
			if event.key == left:
				self.input.Left = False
			if event.key == right:
				self.input.Right = False
			if event.key == up:
				self.input.Up = False
			if event.key == down:
				self.input.Down = False
