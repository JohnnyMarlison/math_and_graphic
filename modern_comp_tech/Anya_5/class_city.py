from class_region import *
from class_place import *

class City(Place, Region):
    def __init__(self, size, geography, name, population):
        self.name = name
        self.population = population
        
        super().__init__(size, name, geography)
        self.size = size
        self.geography = geography

    def show_city(self):
        print(self.name)

    def get_size(self):
        print(self.size)

    def show_geography(self):
        print(self.geography)

    def show_population(self):
        print(self.population)

    def change_pop(self, item):
        self.population = item