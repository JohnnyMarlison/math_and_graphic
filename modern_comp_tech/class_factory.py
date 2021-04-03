class Organization():
    def __init__(self, documents, workers, name):
        self.name = name
        self.documents = documents
        self.workers = workers

    def show_name(self):
        print(self.name)

    def show_workers(self):
        print(self.workers)

    def show_documents(self):
        print(self.documents)

    def add_worker(self, person):
        self.workers.append(person)
        print(str(person))

    def remove_worker(self, person):
        self.workers.remove(person) 
        print(str(person))



class InsuranceCompany(Organization):
    def __init__(self, documents, workers, name):
        super().__init__(documents, workers, name)

        self.name = name
        self.documents = documents
        self.workers = workers

    def insurance(self):
        print("Идет страхование клиента...")

    def show_name(self):
        print(self.name)

    def show_workers(self):
        print(self.workers)

    def show_documents(self):
        print(self.documents)

    def add_worker(self, person):
        self.workers.append(person)
        print(str(person))

    def remove_worker(self, person):
        self.workers.remove(person)
        print(str(person))


class Factory(Organization):
    def __init__(self, documents, workers, name):
        super().__init__(documents, workers, name)

        self.name = name
        self.documents = documents
        self.workers = workers

    def production(self):
        print("Производство в процессе...")

    def show_name(self):
        print(self.name)


    def show_workers(self):
        print(self.workers)

    def show_documents(self):
        print(self.documents)

    def add_worker(self, person):
        self.workers.append(person)
        print(str(person))

    def remove_worker(self, person):
        self.workers.remove(person) 
        print(str(person))



class ShipbuildingCompany(Organization):
    def __init__(self, documents, workers, name):
        super().__init__(documents, workers, name)

        self.name = name
        self.documents = documents
        self.workers = workers

    def projecting(self):
        print("Корабль спроектирован!")

    def show_name(self):
        print(self.name)

    def show_workers(self):
        print(self.workers)

    def show_documents(self):
        print(self.documents)

    def add_worker(self, person):
        self.workers.append(person)
        print(str(person))

    def remove_worker(self, person):
        self.workers.remove(person) 
        print(str(person))



def main():
    documets1 = ["doc1",  "doc2", "doc3"]
    documets2 = ["doc4",  "doc5", "doc6"]
    documets3 = ["doc7",  "doc8", "doc9"]

    workers0 = ["Попов Тихон Игнатиевич", "Пищальников Эммануил Феоктистович", "Куксилина Христина Ивановна"]

    workers1 = ["Сухарников Артём Захарович", "Тянникова Владлена Яновна", 
                    "Трусов Капитон Вячеславович", "Эфиров Андрон Титович", 
                    "Гринина Ольга Леонидовна", "Русскиха Фаина Федотовна"]
    workers2 = ["Еркулаева Валерия Захаровна", "Завражный Семён Эрнестович", 
                    "Кирпа Людмила Тимуровна", "Драчёва Агния Василиевна", 
                    "Лазуткин Валерьян Макарович", "РНиколаенко Стела Кузьмевна"]
    workers3 = ["Кологреева Таисия Фомевна", "Ухова Агата Константиновна", 
                    "Храмова Христина Алексеевна", "Жданова Вера Василиевна", 
                    "Гринина Ольга Леонидовна", "Русскиха Фаина Федотовна"]

    avangard_comp = InsuranceCompany(documets1, workers1, "Avangard_Company")
    tesla_motors = Factory(documets2, workers3, "Telsa_Motors")
    cyberships = ShipbuildingCompany(documets3, workers2, "CyberShips_Company")

    print("--------------------------------------------------")
    avangard_comp.show_name()
    print()
    print("Рабочий коллектив:")
    avangard_comp.show_workers()
    print("--------------------------------------------------")
    
    tesla_motors.show_name()
    print()
    tesla_motors.production()
    print()
    print("Совет директоров принял решение об увольнении -")
    tesla_motors.remove_worker(workers3[0])
    print("--------------------------------------------------")
    
    cyberships.show_name()
    print()
    print("На должность исполнительного директора вступает: ")
    cyberships.add_worker(workers0[1])
    print("--------------------------------------------------")
    print("Отчетность за прошедший год предоставили:\n")
    cyberships.show_name()
    print()
    cyberships.show_documents()
    print()
    tesla_motors.show_name()
    print()
    tesla_motors.show_documents()
    print("Отчетность за прошедший год HE предоставили:\n")
    avangard_comp.show_name()
    print("--------------------------------------------------")


if __name__ == "__main__":
    main()
