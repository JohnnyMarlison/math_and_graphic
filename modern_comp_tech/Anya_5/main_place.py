from class_region import *
from class_place import *
from class_city import *
from class_megalopolis import *

def clsRegion():
    reg_size = 10000000
    reg_name = "Московская область"
    
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


def clsPlace():
    place_size = 10000
    place_name = "Бородинское поле"
    place_geography = "Историческое поле, находящееся к западу от Можайска, на территории\n сельского поселения Бородинское Можайского района\n Московской области, близ деревни Бородино"

    print("\n******************************************************************\n")
    print("Класс Место:")
    place = Place(place_size, place_name, place_geography)
    print("Площадь км^2:")
    place.get_size()
    print("Название места:")
    place.show_place()
    print("География места:")
    place.show_geography()


def clsCity():
    city_size = 100000
    city_geography = "Расположен в окрестностях леса с хвойными и лиственными деревьями"
    city_name = "Красногорск"
    city_popul = 500000

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


def clsMegalopolis():
    megapol_size = 7000000
    megapol_geohraphy = "Находится в центральной части Восточно-Европейской\n равнины, в междуречье Оки и Волги, на средней высоте 180 м над уровнем моря", "Москва"
    megapol_name = "Москва"
    megapol_pop = 10000000


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
    print(megalopolis.show_overpopulation(654321))
    print("\n******************************************************************\n")


if __name__ == "__main__"  :
    clsRegion()
    clsPlace()
    clsCity()
    clsMegalopolis()