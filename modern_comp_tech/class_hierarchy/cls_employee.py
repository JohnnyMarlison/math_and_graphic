from cls_person import *

class Employee(Person):
    def __init__(self, age, gender, name, subdivision):
        self.subdivision = subdivision
        
        super().__init__(age, gender, name)
        self.name = name
        self.age = age
        self.gender = gender


    def employe(self):
        print("Serving in the US army!!!\n")

    def get_subvision(self):
        return self.subdivision

    def change_subvision(self, new):
        self.subdivision = new