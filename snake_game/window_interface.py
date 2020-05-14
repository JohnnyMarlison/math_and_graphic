import pygame
from pygame import font
import tkinter as tk
from tkinter import messagebox
from enum import Enum

from game_objects import *

class InterfaceState(Enum):
	GAME_START = 0
	MAIN_MENU = 1
	PAUSE_MENU = 2
	DEATH_MENU = 3
	EXIT_APPLICATION = 4
	EXIT_GAME = 5
	GAME_CONTINUE = 6

class ApplicationState(Enum):
	RESTART = 0
	CONTINUE = 1

def create_rect(x, y, size):
	return [ [x, y],
			 [x + size[0], y],
			 [x + size[0], y + size[1]],
			 [x, y + size[1]]]

def draw_rectagnle(surface, x, y, size, color = (255, 255, 255), font_module = None, text = ''):
	pygame.draw.polygon(surface, color, create_rect(x, y, size))
	if (font_module != None):
		rend = font_module.render(text, True, (125, 125, 255))
		surface.blit(rend, (x + (size[0] - pygame.Surface.get_width(rend)) // 2, y + (size[1] - pygame.Surface.get_height(rend)) // 2))


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

	return InterfaceState.GAME_CONTINUE
	
def template_menu(surface, menu_text, font_module, width, return_func):
	max_len_pixel = 0
	heigth_button = width // 10
	spacing = width // 50
	for i in menu_text:
		val = pygame.Surface.get_width(font_module.render(i, True, (0, 255, 255)))
		if val > max_len_pixel:
			max_len_pixel = val
	max_len_pixel += 40
	__pixel_menu_heigth = len(menu_text) * heigth_button + (len(menu_text) - 1) * spacing
	y_start = (width - __pixel_menu_heigth) // 2
	x_start = (width - max_len_pixel) // 2
	print((x_start, y_start))
	color_default = (255, 255, 255)
	color_select  = (255, 0, 0)
	item = 0
	while (True):
		y = y_start
		for i in range(len(menu_text)):
			if i == item:
				draw_rectagnle(surface, x_start, y, (max_len_pixel, heigth_button), color_select, font_module, menu_text[i])
			else:
				draw_rectagnle(surface, x_start, y, (max_len_pixel, heigth_button), color_default, font_module, menu_text[i])

			y += (heigth_button + spacing)

		for event in pygame.event.get():
			keys = pygame.key.get_pressed()

			if keys[pygame.K_UP]:
				item -= 1
				if item < 0:
					item = len(menu_text) - 1
			elif keys[pygame.K_DOWN]:
				item += 1
				if item >= len(menu_text):
					item = 0
			elif keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
				return return_func(item)
				
		pygame.display.update()

def keyboard_main_menu_handler(surface, font_module, width):
	menu_text = ['New Game', 'Exit']
	def _tmp(x):
		if x == 0:
			return InterfaceState.GAME_START
		else:
			return InterfaceState.EXIT_APPLICATION
	return template_menu(surface, menu_text, font_module, width, _tmp)

def keyboard_pause_menu_handler(surface, font_module, width):
	menu_text = ['Continue', 'New game', 'Exit']
	def _tmp(x):
		if x == 0:
			return InterfaceState.GAME_CONTINUE
		elif x == 1:
			return InterfaceState.GAME_START
		else:
			return InterfaceState.EXIT_GAME
	return template_menu(surface, menu_text, font_module, width, _tmp)

def keyboard_death_menu_handler(surface, font_module, width):
	menu_text = ['Restart', 'Exit']
	def _tmp(x):
		if x == 0:
			return InterfaceState.GAME_START
		else:
			return InterfaceState.EXIT_GAME
	return template_menu(surface, menu_text, font_module, width, _tmp)

window_width = 800
size_grid = 25

_font_module   = font_init()
_window_module = window_init(window_width, size_grid)
_clock_module  = clock_init()
_snake         = snake_init(window_width, size_grid)
_snack         = snack_init(_snake, window_width, size_grid)			

def game_process(window_width, size_grid, _clock_module, _snake, _snack, handler):
	rows = window_width // size_grid
	pygame.time.delay(40)
	_clock_module.tick(8)
	if _snake.body[0].pos == _snack.pos:
		_snake.addCube()
		_snack = snack_init(_snake, window_width, size_grid)

	_snake.move()
	state = handler(_snake)

	for x in range(len(_snake.body)):
		if _snake.body[x].pos in list(map(lambda z:z.pos,_snake.body[x + 1:])):
			message_box('You Lose!', 'Play again...')
			_snake.reset((10, 10))
			break
	
		redrawWindow(_window_module, window_width, size_grid, _snake, _snack, _font_module)
	
	return state

# def keyboard_handler(surface, font_module, width, size_grid, state, snake):
# 	global _clock_module, _snake, _snack
# 	for event in pygame.event.get():
# 		if state == InterfaceState.GAME_START: # game time
# 			print('GAME_START')
# 			print(_clock_module == None)
# 			_clock_module  = clock_init()
# 			_snake         = snake_init(window_width, size_grid)
# 			_snack         = snack_init(_snake, window_width, size_grid)	
# 			state = InterfaceState.GAME_CONTINUE
# 		elif state == InterfaceState.MAIN_MENU: # main menu
# 			print('MAIN_MENU')
# 			state = keyboard_main_menu_handler(surface, font_module, width)
# 		elif state == InterfaceState.PAUSE_MENU: # pause menu
# 			print('PAUSE_MENU')
# 			state = keyboard_pause_menu_handler(surface, font_module, width)
# 		elif state == InterfaceState.DEATH_MENU: # end game menu
# 			print('DEATH_MENU')
# 			state = keyboard_death_menu_handler(surface, font_module, width)
# 		elif state == InterfaceState.EXIT_APPLICATION:
# 			print('EXIT_APPLICATION')
# 			pass
# 		elif state == InterfaceState.EXIT_GAME:
# 			print('EXIT_GAME')
# 			start = InterfaceState.MAIN_MENU
# 		elif state == InterfaceState.GAME_CONTINUE:
# 			print('GAME_CONTINUE')
# 			state = game_process(width, size_grid, _clock_module, _snake, _snack, keyboard_game_handler)
			
# 	return state

def keyboard_handler(surface, font_module, width, size_grid, state, snake):
	global _clock_module, _snake, _snack
	pygame.event.get()
	if state == InterfaceState.GAME_START: # game time
		print('GAME_START')
		print(_clock_module == None)
		_clock_module  = clock_init()
		_snake         = snake_init(window_width, size_grid)
		_snack         = snack_init(_snake, window_width, size_grid)	
		state = InterfaceState.GAME_CONTINUE
	elif state == InterfaceState.MAIN_MENU: # main menu
		print('MAIN_MENU')
		state = keyboard_main_menu_handler(surface, font_module, width)
	elif state == InterfaceState.PAUSE_MENU: # pause menu
		print('PAUSE_MENU')
		state = keyboard_pause_menu_handler(surface, font_module, width)
	elif state == InterfaceState.DEATH_MENU: # end game menu
		print('DEATH_MENU')
		state = keyboard_death_menu_handler(surface, font_module, width)
	elif state == InterfaceState.EXIT_APPLICATION:
		print('EXIT_APPLICATION')
		pass
	elif state == InterfaceState.EXIT_GAME:
		print('EXIT_GAME')
		start = InterfaceState.MAIN_MENU
	elif state == InterfaceState.GAME_CONTINUE:
		print('GAME_CONTINUE')
		state = game_process(width, size_grid, _clock_module, _snake, _snack, keyboard_game_handler)
			
	return state

def main_interface_window(window_width, size_grid):	
	state = InterfaceState.MAIN_MENU
	while 1:
		state = keyboard_handler(_window_module, _font_module, window_width, size_grid, state, _snake)
