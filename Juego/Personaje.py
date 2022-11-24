import sys
import pygame
pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('personasa')
width, height = 800, 600
speed = [1, 1]
white = 255, 255, 255
per = pygame.image.load('per.png')
perrect = per.get_rect()
run=True
while run:
	pygame.time.delay(2)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: run = False
	perrect = perrect.move(speed)
	if perrect.left < 0 or perrect.right > width:
		speed[1] = -speed[1]
	screen.fill(white)
	screen.blit(per, perrect)
	pygame.display.flip()
pygame.quit()