import pygame
pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("test")

x = 50
y = 50
width = 40
height = 60
vel = 5 
jump = False
jump_count = 10
run = True

while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# keyboard
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
	if keys[pygame.K_RIGHT] and x < 500 - width - vel:
		x += vel
	if not (jump):	
		if keys[pygame.K_UP] and y > vel:
			y -= vel
		if keys[pygame.K_DOWN] and y < 500 - height - vel:
			y += vel
		if keys[pygame.K_SPACE]:
			jump = True
	else:
		if jump_count >= -10:
			neg = 1
			if jump_count < 0:
				neg = -1		
			y = (jump_count ** 2) * 0.5
			jump_count -= 1
		else:
			jump = False
			jump_count = 10

	# graphic
	window.fill((0, 0, 0))
	pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
	pygame.display.update()

pygame.quit()