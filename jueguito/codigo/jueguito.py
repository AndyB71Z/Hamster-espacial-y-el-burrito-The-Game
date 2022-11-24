import pygame 
import sys
from player import Player
from random import choice, randint
from disparar import Disparar
from hamster import Hamster
 
class Game:
	def __init__(self):
		player_sprite = Player((screen_width / 2,screen_height),screen_width,5)
		self.player = pygame.sprite.GroupSingle(player_sprite)

		
		self.vidas = 3
		self.vida_surf = pygame.image.load('D:/Downloads/jueguito/grafi/vida.png').convert_alpha()
		self.vida_x_start_pos = screen_width - (self.vida_surf.get_size()[0] * 2 + 20)
		self.puntaje = 0 
		self.font = pygame.font.Font('D:/Downloads/jueguito/font/Pixeled.ttf',20)
		 
		self.hamsters = pygame.sprite.Group()
		self.hamster_disparar = pygame.sprite.Group()
		self.hamster_setup(rows = 6, cols = 8)
		self.hamster_direction = 1

	
	##Hamsters

	def hamster_setup(self,rows,cols,x_distance = 60,y_distance = 48,x_offset = 70, y_offset = 100):
		for row_index, row in enumerate(range(rows)):
			for col_index, col in enumerate(range(cols)):
				x = col_index * x_distance + x_offset
				y = row_index * y_distance + y_offset
				
				if row_index == 0: hamster_sprite= Hamster('rojo',x,y)
				self.hamsters.add(hamster_sprite)

	def hamster_posicion_c(self):
		all_hamsters = self.hamsters.sprites()
		for hamster in all_hamsters:
			if hamster.rect.right >= screen_width:
				self.hamster_direction = -1
				self.hamster_mover_abajo(2)
			elif hamster.rect.left <= 0:
				self.hamster_direction = 1
				self.hamster_mover_abajo(2)

	def hamster_mover_abajo(self,distance):
		if self.hamsters:
			for hamster in self.hamsters.sprites():
				hamster.rect.y += distance
	################################################3
	def coliciones_veri(self):

		# jugador disparo 
		if self.player.sprite.disparar:
			for disparar in self.player.sprite.disparar:
				#if pygame.sprite.spritecollide(disparar,self.blocks,True):
				#	disparar.kill()
					

				# hamster colicioness
				hamsters_hit = pygame.sprite.spritecollide(disparar,self.hamsters,True)
				if hamsters_hit:
					#for hamster in hamsters_hit:
						#self.puntaje += hamster.value
					disparar.kill()
					#self.explosion_sound.play()


		# hamster disparar 
		if self.hamster_disparar:
			for disparar in self.hamster_disparar:
				if pygame.sprite.spritecollide(disparar,self.blocks,True):
					disparar.kill()

				if pygame.sprite.spritecollide(disparar,self.player,False):
					disparar.kill()
					self.lives -= 1
					if self.lives <= 0:
						pygame.quit()
						sys.exit()

		# hamsters
		if self.hamsters:
			for hamster in self.hamsters:
				#pygame.sprite.spritecollide(hamster,self.blocks,True)

				if pygame.sprite.spritecollide(hamster,self.player,False):
					pygame.quit()
					sys.exit()
	#########################################

	def display_vidas(self):
		for vida in range(self.vidas - 1):
			x = self.vida_x_start_pos + (vida * (self.vida_surf.get_size()[0] + 10))
			screen.blit(self.vida_surf,(x,8))

	def display_puntaje(self):
		puntaje_surf = self.font.render(f'puntaje: {self.puntaje}',False,'white')
		puntaje_rect = puntaje_surf.get_rect(topleft = (10,-10))
		screen.blit(puntaje_surf,puntaje_rect)

	def ganaste_message(self):
		if not self.hamsters.sprites():
			ganaste_surf = self.font.render('Ya ganaste Tu!',False,'white')
			ganaste_rect = ganaste_surf.get_rect(center = (screen_width / 2, screen_height / 2))
			screen.blit(ganaste_surf,ganaste_rect)


	def run(self):
		self.player.update()
		self.hamster_disparar.update()

		self.hamsters.update(self.hamster_direction)
		self.hamster_posicion_c()
		self.coliciones_veri()
		
		self.player.sprite.disparar.draw(screen)
		self.player.draw(screen)
		self.hamsters.draw(screen)
		
		self.display_vidas()
		self.display_puntaje()
		self.ganaste_message()
	

class CRT:
	def __init__(self):
		self.tv = pygame.image.load('D:/Downloads/jueguito/grafi/tv.png').convert_alpha()
		self.tv = pygame.transform.scale(self.tv,(screen_width,screen_height))

	def create_crt_lines(self):
		line_height = 3
		line_amount = int(screen_height / line_height)
		for line in range(line_amount):
			y_pos = line * line_height
			pygame.draw.line(self.tv,'black',(0,y_pos),(screen_width,y_pos),1)

	def draw(self):
		self.tv.set_alpha(randint(75,90))
		self.create_crt_lines()
		screen.blit(self.tv,(0,0))

if __name__ == '__main__':
	pygame.init()
	screen_width = 600
	screen_height = 600
	screen = pygame.display.set_mode((screen_width,screen_height))
	clock = pygame.time.Clock()
	game = Game()
	crt = CRT()

	hamsterdisparar = pygame.USEREVENT + 1
	pygame.time.set_timer(hamsterdisparar,800)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		screen.fill((30,30,30))
		game.run()
		#crt.draw()
			
		pygame.display.flip()
		clock.tick(60)