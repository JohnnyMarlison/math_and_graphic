class Person():
    def __init__(self, age, gender, name):
        self.age = age
        self.gender = gender
        self.name = name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_name(self):
        return self.name

    def change_age(self, new_age):
        self.age = new_age

    def change_gender(self, new_gender):
        self.age = new_gender

    def rename(self, new):
        self.name = new
