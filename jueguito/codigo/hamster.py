import pygame

class Hamster(pygame.sprite.Sprite):
	def __init__(self,color,x,y):
		super().__init__()
		self.image = pygame.image.load('D:/Downloads/jueguito/grafi/rojo.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = (x,y))

		if color == 'rojo': self.value = 100

	def update(self,direction):
		self.rect.x += direction
