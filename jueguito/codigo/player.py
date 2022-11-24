import pygame 
from disparar import Disparar

class Player(pygame.sprite.Sprite):
	def __init__(self,pos,constraint,speed):
		super().__init__()
		self.image = pygame.image.load('D:/Downloads/jueguito/grafi/jugador.png').convert_alpha()
		self.rect = self.image.get_rect(midbottom = pos)
		self.speed = speed
		self.max_x_constraint = constraint
		self.ready = True
		self.disparar_time = 0
		self.disparar_cooldown = 600

		self.disparar = pygame.sprite.Group()

		#self.disparar_sound = pygame.mixer.Sound('D:/Downloads/Space-invaders-main/audio/disparar.wav')
		#self.disparar_sound.set_volume(0.5)

	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.rect.x += self.speed
		elif keys[pygame.K_LEFT]:
			self.rect.x -= self.speed

		if keys[pygame.K_SPACE] and self.ready:
			self.shoot_disparar()
			self.ready = False
			self.disparar_time = pygame.time.get_ticks()
			#self.disparar_sound.play()

	def recharge(self):
		if not self.ready:
			current_time = pygame.time.get_ticks()
			if current_time - self.disparar_time >= self.disparar_cooldown:
				self.ready = True

	def constraint(self):
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right >= self.max_x_constraint:
			self.rect.right = self.max_x_constraint

	def shoot_disparar(self):
		self.disparar.add(Disparar(self.rect.center,-8,self.rect.bottom))

	def update(self):
		self.get_input()
		self.constraint()
		self.recharge()
		self.disparar.update()