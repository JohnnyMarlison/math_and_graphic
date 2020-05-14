from enum import Enum

from game_objects import *

class MapDifficult(Enum):
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
	for i in range(15, size_x - 10):
		coord.append((i, 6))

	# Generate second obstacle
	for i in range(15, size_x - 5):
		coord.append((i, size_y - 6))

	# Generate third obstacle
	for i in range(10, size_y - 15):
		coord.append((6, i))

	# Generate third obstacle
	for i in range(10, size_y - 12):
		coord.append((size_x - 5, i))

	return coord

def gen_medium_map_coord(size_x, size_y):
	coord = []

	return coord

def gen_hard_map_coord(size_x, size_y):
	coord = []

	return coord

class obstacle(object):
	def __init__(self, size_x, size_y, map_type):
		self.coodr = []
		self.map_type = map_type
		print('Current map: ' + get_maps_names()[self.map_type])
		if self.map_type == MapDifficult.MAP_FREE:
			pass
		elif self.map_type == MapDifficult.MAP_EASY:
			self.coord = gen_easy_map_coord(size_x, size_y)
		elif self.map_type == MapDifficult.MAP_MEDIUM:
			self.coord = gen_medium_map_coord(size_x, size_y)
		elif self.map_type == MapDifficult.MAP_HARD:
			self.coord = gen_hard_map_coord(size_x, size_y)

	def draw(self, surface):
		for i in self.coord:
			cube(i, 0, 0, (0, 0, 255)).draw(surface)

	def check_cube_collision(block):
		for i in self.coord:
			if i == block.get_coord():
				return True
		return False

	def check_snake_colision(snake):
		return check_cube_collision(snake.get_head_feature_cube())
