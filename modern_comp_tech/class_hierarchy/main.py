from cls_person import *
from cls_employee import *
from cls_worker import *
from cls_engineer import *


def view_cls_person():
    person_age = 25
    person_gender = "male"
    person_name = "Steve"
    person = Person(person_age, person_gender, person_name)
    print("##############################################################################################\n")
    print("Class Person:\n")
    print("Name: " + str(person.get_name()) + "\nAge: " + str(person.get_age()) + "\nGender: " + str(person.get_gender()))
    print("\nLet's change name, gender and age!\n")
    person.change_age(35)
    person.change_gender("female")
    person.rename("Alisa")
    print("Name: " + str(person.get_name()) + "\nAge: " + str(person.get_age()) + "\nGender: " + str(person.get_gender()) + "\n")


def view_cls_employee():
    employee_age = 21
    employee_gender = "male"
    employee_name = "John"
    employee_subvision = "US Navy"
    employee = Employee(employee_age, employee_gender, employee_name, employee_subvision)

    print("##############################################################################################\n")
    print("Class Employee\n")
    print("Name: " + str(employee.get_name()) + "\nAge: " + str(employee.get_age()) + "\nGender: " + str(employee.get_gender()) + "\nSubvision: " + str(employee.get_subvision()))
    employee.employe()
    print("Let's change subvision and age!\n")
    employee.change_subvision("WWII USA\n")
    employee.change_age(24)
    print("Age: " + str(employee.get_age()) + " |", "Subvision: " + str(employee.get_subvision()))


def view_cls_worker():
    worker_age = 29
    worker_gender = "female"
    worker_name = "Mary"
    worker_specialization = "Labor protection specialist"
    worker = Worker(worker_age, worker_gender, worker_name, worker_specialization)

    print("##############################################################################################\n")
    print("Class Worker:\n")
    print("Name: " + str(worker.get_name()) + "\nAge: " + str(worker.get_age()) + "\nGender: " + str(worker.get_gender()) + "\nSpecialization: " + str(worker.get_specialization()))
    worker.work()

def view_cls_engineer():
    engineer_age = 40
    engineer_gender = "female"
    engineer_name = "Helen"
    engineer_specialization = "Engineer"
    engineer_position = "Senior Chemical Engineer"
    engineer = Engineer(engineer_age, engineer_gender, engineer_name, engineer_specialization, engineer_position)

    print("##############################################################################################\n")
    print("Class Worker:\n")
    print("Name: " + str(engineer.get_name()) + "\nAge: " + str(engineer.get_age()) + "\nGender: " + str(engineer.get_gender()) + "\nSpecialization: " + str(engineer.get_specialization()) + "\nPosition: " + str(engineer.get_position()) )
    engineer.projecting()

    print("Let's chanege name and position!\n")
    engineer.rename("Elis\n")
    engineer.change_position("Chef-Engineer\n")
    print("Age: " + str(engineer.get_age()) + " |", "Position:" + str(engineer.get_position()))
    print("##############################################################################################\n")


def main():
    view_cls_person()
    view_cls_employee()
    view_cls_worker()
    view_cls_engineer()

if __name__ == "__main__":
    main()