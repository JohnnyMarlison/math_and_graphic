from cls_person import *

class Worker(Person):
    def __init__(self, age, gender, name, specialization):
        self.specialization = specialization
        super().__init__(age, gender, name)

        self.name = name
        self.age = age
        self.gender = gender

    def work(self):
        print("I'm at work...\n")

    def get_specialization(self):
        return self.specialization

    def change_specialization(self, new):
        self.specialization = new
    