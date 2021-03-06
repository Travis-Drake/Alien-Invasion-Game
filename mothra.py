import pygame
from pygame.sprite import Sprite

class Mothra(Sprite):
	"""A class to manage your kaiju"""
	def __init__(self,ai_game):
		"""initialize your beast and set its starting position"""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		#load the monster and get its rect.
		self.image = pygame.image.load('Space_Butterfly.bmp')
		self.rect = self.image.get_rect()
		#Start each new monster at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom
		# store a decimal value for ship's horizontal position
		self.x = float(self.rect.x)
		# store a decimal value for ship's vertical position
		self.y = float(self.rect.y)
		# Movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""update ship's position based on movement flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.mothra_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.mothra_speed
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.mothra_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.mothra_speed
		#update rect object from self.x and self.y
		self.rect.x = self.x
		self.rect.y = self.y
	def blitme(self):
		"""Draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)
	def center_mothra(self):
		"""Center the ship on the screen"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)