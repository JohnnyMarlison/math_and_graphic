# import numpy as np

# # создание матрицы с помощью генератора случайных чисел


# def MakeMatr(n, a, b):
#     Matr = (b - a) * np.random.random(size=(n, n)) + a
#     return Matr


# # вывод матрицы на экран
# def PrintMatr(Matr):
#     (nRow, nCol) = Matr.shape
#     for Row in range(nRow):
#         for Col in range(nCol):
#             print("{0: 7.0f}".format(Matr[Row][Col]), end=" ")
#         print()
#     print()


# # меняем местами столбцы с минимальным и максимальным элементом
# def swape_cols(arr, frm, to):
#     arr[:, [frm, to]] = arr[:, [to, frm]]
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



def main():
    reg_size = 10000000
    reg_name = "Московская область"

    place_size = 10000
    place_name = "Бородинское поле"
    place_geography = "Историческое поле, находящееся к западу от Можайска, на территории\n сельского поселения Бородинское Можайского района\n Московской области, близ деревни Бородино"

    city_size = 100000
    city_geography = "Расположен в окрестностях леса с хвойными и лиственными деревьями"
    city_name = "Красногорск"
    city_popul = 500000

    megapol_size = 7000000
    megapol_geohraphy = "Находится в центральной части Восточно-Европейской\n равнины, в междуречье Оки и Волги, на средней высоте 180 м над уровнем моря", "Москва"
    megapol_name = "Москва"
    megapol_pop = 10000000

    print("******************************************************************\n")
    print("Класс Область:")
    reg = Region(reg_size, reg_name)
    reg.show_region()
    print("Площадь км^2:")
    reg.get_size()
    print("Увеличми площадь:")
    new_size = 10000000 + 2345678
    reg.change_size(new_size)
    reg.get_size()
    
    print("\n******************************************************************\n")
    print("Класс Место:")
    place = Place(place_size, place_name, place_geography)
    print("Площадь км^2:")
    place.get_size()
    print("Название места:")
    place.show_place()
    print("География места:")
    place.show_geography()
    
    print("\n******************************************************************\n")
    print("Класс Город:")
    city = City(city_size, city_geography, city_name, city_popul)
    print("Название города:")
    city.show_city()
    print("Население Города:")
    city.show_population()
    print("Изменим население города:")
    new_pop = 654321
    city.change_pop(new_pop)
    city.show_population()
    print("\n******************************************************************\n")
    print("Класс Мегаполиса")
    megalopolis = Megalopolis(megapol_size, megapol_geohraphy, megapol_name, megapol_pop, True)
    print("Название Мегаполиса:")
    megalopolis.show_megalopolis()
    print("Население Мегаполиса:")
    megalopolis.show_population()
    print("Москва Мегаполис?")
    print(megalopolis.show_overpopulation(7000000))
    print("Красногорск Мегаполис?")
    print(megalopolis.show_overpopulation(new_pop))
    print("\n******************************************************************\n")
    

if __name__ == "__main__"  :
    main()