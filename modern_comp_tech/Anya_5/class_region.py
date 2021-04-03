class Region():
    def __init__(self, size, name):
        self.size = size
        self.name = name

    def show_region(self):
        print(self.name)

    def get_size(self):
        print(self.size)

    def change_size(self, item):
        self.size = item
