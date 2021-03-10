import pygame
from pygame.locals import *

pygame.init()
run = True

pygame.event.clear()
while run:
	window = pygame.display.set_mode((500, 500))
	win_name = pygame.display.set_caption("test")
	win_delay = pygame.time.delay(100)
	clock = pygame.time.Clock()
	event = pygame.event.wait()
    if event.type == QUIT:
		pygame.quit()
		sys.exit()
# pygame.quit()