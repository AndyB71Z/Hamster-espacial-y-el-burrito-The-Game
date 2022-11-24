import pygame

pygame.init()

W, H = 1000, 600
PANTALLA = pygame.display.set_mode((W, H))
pygame.display.set_caption('asdf')
icono=pygame.image.load('per.png')
pygame.display.set_icon(icono)

fondo = pygame.image.load('espacio.png')
quieto = pygame.image.load('per.png')
caminaDerecha = [pygame.image.load('per.png')]
caminaIzquierda = [pygame.image.load('per.png')]
salta = [pygame.image.load('per.png')]

x = 0
px = 50
py = 200
ancho = 40
velocidad = 10

reloj = pygame.time.Clock()

salto = False
cuentaSalto = 10

izquierda = False
derecha = False
cuentaPasos = 0

def recarga_pantalla():
	global cuentaPasos
	global x


	x_relativa = x % fondo.get_rect().width
	PANTALLA.blit(fondo, (x_relativa - fondo.get_rect().width, 0))
	if x_relativa < W:
		PANTALLA.blit(fondo, (x_relativa, 0))
	x -= 5

    
	if cuentaPasos + 1 >= 6:
		cuentaPasos = 0
	# a
	if izquierda:
		PANTALLA.blit(caminaIzquierda[cuentaPasos // 5], (int(px), int(py)))
		cuentaPasos += 1

		# d
	elif derecha:
		PANTALLA.blit(caminaDerecha[cuentaPasos // 5], (int(px), int(py)))
		cuentaPasos += 1

	elif salto + 1 >= 2:
		PANTALLA.blit(salta[cuentaPasos // 1], (int(px), int(py)))
		cuentaPasos += 1

	else:
		PANTALLA.blit(quieto,(int(px), int(py)))

ejecuta = True
while ejecuta:
	reloj.tick(18)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			ejecuta = False
	keys = pygame.key.get_pressed()
	# a
	if keys[pygame.K_a] and px > velocidad:
		px -= velocidad
		izquierda = True
		derecha = False
	# d
	elif keys[pygame.K_d] and px < 900 - velocidad - ancho:
		px += velocidad
		izquierda = False
		derecha = True
	else:
		izquierda = False
		derecha = False
		cuentaPasos = 0

	# w
	if keys[pygame.K_w] and py > 100:
		py -= velocidad

	# s
	if keys[pygame.K_s] and py < 300:
		py += velocidad
	if not salto:
		if keys[pygame.K_SPACE]:
			salto = True
			izquierda = False
			derecha = False
			cuentaPasos = 0
	else:
		if cuentaSalto >= -10:
			py -= (cuentaSalto * abs(cuentaSalto)) * 0.5
			cuentaSalto -= 1
		else:
			cuentaSalto = 10
			salto = False


	pygame.display.update()
	recarga_pantalla()

pygame.quit()