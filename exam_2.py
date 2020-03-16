import pygame
import random

pygame.init()
clock = pygame.time.clock()
display = pygame.display.set_mode((500, 500))
apple_pos = [random.randint(1, 50) * 10, random.randint(1, 50) * 10]
snake_pos = [[250, 250], [240, 250], [230, 250]]
snake_head = [250, 250]
score = 0


def coll_with_apple(score):
	apple_pos = [random.randint(1, 50) * 10, random.randint(1, 50) * 10]
	score += 1
	return apple_pos, score


def coll_with_bound(snake_head):
	if snake_head[0] >= 500 or snake_head[0] < 0 or snake_head[1] >= 500 or snake_head[1] < 0:
		return 1
	else:
		return 0


def coll_with_self(snake_pos):



def generate(snake_head, snake_pos, apple_pos, but_dir, score):



def display_snake_apple(display, snake_pos, apple_pos):



def play_game(snake_head, snake_pos, apple_pos, but_dir, score):