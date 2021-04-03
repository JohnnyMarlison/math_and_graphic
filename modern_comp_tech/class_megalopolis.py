from class_city import *


class Megalopolis(City):
    def __init__(self, size, geography, name, population, overpopulation):
        self.name = name
        self.overpopulation = overpopulation
        
        super().__init__(size, geography, name, population)
        self.size = size
        self.geography = geography
        self.population = population

    def show_geography(self):
        print(self.geography)

    def get_size(self):
        print(self.size)

    def show_megalopolis(self):
        print(self.name)

    def show_population(self):
        print(self.population)

    def change_pop(self, item):
        self.population = item

    def show_overpopulation(self, item):
        return item >= 1000000 if True else False