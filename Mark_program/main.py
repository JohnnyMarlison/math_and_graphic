import pygame
import os
import GridClass

#os.environ["SDL_VIDEO_CENTERED"]='1'

# width, height = 1920, 1000
width, height = 2560, 1440
size = (width, height)

pygame.init()
pygame.display.set_caption("Cell's life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

black = (0, 0, 0)
blue = (0, 14, 71)
white = (255, 255, 255)

scaler = 30
offset = 1

Grid = GridClass.Grid(width, height, scaler, offset)
Grid.random2d_array()

run = True
while run:
    # clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Grid.Cells(off_color=white, on_color=blue, surface=screen)
    pygame.display.update()

pygame.quit()