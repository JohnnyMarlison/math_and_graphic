from enum import IntEnum

from game_objects import *

class MapDifficult(IntEnum):
	MAP_FREE = 0
	MAP_EASY = 1
	MAP_MEDIUM = 2
	MAP_HARD = 3

__maps_names = ['Beginner', 'Easy', 'Medium', 'Hard']

def get_maps_names():
	global __maps_names
	return __maps_names

def gen_easy_map_coord(size_x, size_y):
	coord = []

	# Generate first obstacle
	for i in range(15, size_x - 10, 1):
		coord.append((i, 6))

	# Generate second obstacle
	for i in range(15, size_x - 5, 1):
		coord.append((i, size_y - 6))

	# Generate third obstacle
	for i in range(10, size_y - 15, 1):
		coord.append((6, i))

	# Generate third obstacle
	for i in range(10, size_y - 12, 1):
		coord.append((size_x - 5, i))

	return coord

def gen_medium_map_coord(size_x, size_y):
	coord = []

	return coord

def gen_hard_map_coord(size_x, size_y):
	coord = []

	return coord

class obstacle(object):
	coord = []

	def __init__(self, size, width):
		self.size_x = size[0]
		self.size_y = size[1]
		self.width = width

	def set_map(self, map_type):
		print('LOADING MAP: ' + get_maps_names()[map_type])

		if map_type == MapDifficult.MAP_FREE:
			self.coord = []
		elif map_type == MapDifficult.MAP_EASY:
			self.coord = gen_easy_map_coord(self.size_x, self.size_y)
		elif map_type == MapDifficult.MAP_MEDIUM:
			self.coord = gen_medium_map_coord(self.size_x, self.size_y)
		elif map_type == MapDifficult.MAP_HARD:
			self.coord = gen_hard_map_coord(self.size_x, self.size_y)

	def draw(self, surface):
		for i in self.coord:
			cube(i, self.size_x + 1, self.width, (0, 0, 255)).draw(surface)

	def check_cube_collision(self, block):
		for i in self.coord:
			if i == block.get_coord():
				return True
		return False

	def check_snake_colision(self, snake):
		return self.check_cube_collision(snake.get_head_cube())
