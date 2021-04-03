from cls_worker import *

class Engineer(Worker):
    def __init__(self, age, gender, name, specialization, position):
        self.position = position
        super().__init__(age, gender, name, specialization)

        self.name = name
        self.age = age
        self.gender = gender
        self.specialization = specialization

    def projecting(self):
        print("Development in progress...\n")
    
    def get_position(self):
        return self.position

    def change_position(self, new):
        self.position = new