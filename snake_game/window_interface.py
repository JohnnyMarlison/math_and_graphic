import pygame
from pygame import font
import tkinter as tk
from tkinter import messagebox
from enum import Enum

from game_objects import *

class InterfaceState(Enum):
	GAME = 0
	MAIN_MENU = 1
	PAUSE_MENU = 2
	DEATH_MENU = 3


def create_rect(x, y, size):
	return [ [x - size[0]/2, y - size[1]/2],
			 [x + size[0]/2, y - size[1]/2],
			 [x + size[0]/2, y + size[1]/2],
			 [x - size[0]/2, y + size[1]/2]]

def draw_rectagnle(surface, x, y, size, color = (255, 255, 255), font_module = None, text = ''):
	draw.polygon(screen.get_surface(), color, create_rect(x, y, size))
	if (font_module != None):
		rend = font_module.render(goal_text1, True, (0, 255, 255))
		surface.blit(rend1, (x + (size[0] - pygame.Surface.get_width(rend)) // 2, y + (size[1] - pygame.Surface.get_height(rend) // 2)))


def set_footer_text(surface, width, size_grid, font_module, snake):
	win_width = width - (width // size_grid)
	goal_text1 = 'Score: ' + str((snake.get_length() - 1) * 10) 
	goal_text1 += '.   Record: ' + str('None') 
	rend1 = font_module.render(goal_text1, True, (255, 255, 255))
	rend2 = font_module.render('Pause: Press Esc', True, (255, 255, 255))
	surface.blit(rend1, (10, win_width))
	surface.blit(rend2, (win_width - pygame.Surface.get_width(rend2) - 10, win_width))


def redrawWindow(surface, width, size_grid, snake, snack, font_module):
    surface.fill((0, 0, 0))
    snake.draw(surface)
    snack.draw(surface)
    set_footer_text(surface, width, size_grid, font_module, snake)
    pygame.display.update()


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def font_init():
	pygame.font.init()
	_font_name = pygame.font.match_font('Times New Roman')
	return pygame.font.Font(_font_name, 24)

def window_init(win_width, size_grid):
	return pygame.display.set_mode((win_width - (win_width // size_grid), win_width))

def clock_init():
	return pygame.time.Clock()

def snake_init(win_width, size_grid):
	rows = win_width // size_grid
	size_game_field = win_width - (win_width // size_grid)
	return snake(rows, size_game_field, (255, 0, 0), (10, 10))

def snack_init(snake, win_width, size_grid):
	rows = win_width // size_grid
	size_game_field = win_width - (win_width // size_grid)
	return cube(randomSnack(rows, snake), rows, size_game_field, color = (0, 255, 0))

def keyboard_game_handler(snake):
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		dirnx = -1
		dirny = 0
		snake.move(True, dirnx, dirny)

	elif keys[pygame.K_RIGHT]:
		dirnx = 1
		dirny = 0
		snake.move(True, dirnx, dirny)

	elif keys[pygame.K_UP]:
		dirnx = 0
		dirny = -1
		snake.move(True, dirnx, dirny)

	elif keys[pygame.K_DOWN]:
		dirnx = 0
		dirny = 1
		snake.move(True, dirnx, dirny)

	elif keys[pygame.K_ESCAPE]:
		return InterfaceState.PAUSE_MENU

	return InterfaceState.GAME
	


def keyboard_handler(state, snake):
	flag_new_move_event = False
	for event in pygame.event.get():
		if state == InterfaceState.GAME: # game time
			state = keyboard_game_handler(snake)
		elif state == InterfaceState.MAIN_MENU: # main menu
			pass
		elif state == InterfaceState.PAUSE_MENU: # pause menu
			pass
		elif state == InterfaceState.DEATH_MENU: # end game menu
			pass
		else:
			pass
	snake.move()

			

def game_process(window_width, size_grid):
	rows = window_width // size_grid
	_font_module   = font_init()
	_window_module = window_init(window_width, size_grid)
	_clock_module  = clock_init()
	_snake         = snake_init(window_width, size_grid)
	_snack         = snack_init(_snake, window_width, size_grid)
	
	while True:
		pygame.time.delay(40)
		_clock_module.tick(8)
		keyboard_handler(InterfaceState.GAME, _snake)
		if _snake.body[0].pos == _snack.pos:
			_snake.addCube()
			_snack = snack_init(_snake, window_width, size_grid)
	
		for x in range(len(_snake.body)):
			if _snake.body[x].pos in list(map(lambda z:z.pos,_snake.body[x + 1:])):
				message_box('You Lose!', 'Play again...')
				_snake.reset((10, 10))
				break
	
		redrawWindow(_window_module, window_width, size_grid, _snake, _snack, _font_module)
	
def main_interface_window():	
	pass