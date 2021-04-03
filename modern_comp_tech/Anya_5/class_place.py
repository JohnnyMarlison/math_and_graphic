from class_region import *

class Place(Region):
    def __init__(self, size, name, geography):
        self.geography = geography
        self.name = name
        super().__init__(size, name)
        self.size = size

    def get_size(self):
        print(self.size)

    def show_place(self):
        print(self.name)
    
    def show_geography(self):
        print(self.geography)
