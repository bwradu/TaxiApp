from domain.driver import Driver
from service.driver_service import DriverService
from service.cars_ervice import CarService
from domain.car import Car
from domain.exceptions import CustomException
from service.statistics import StatisticsService


class UI:
    def __init__(self, car_service: CarService, driver_service: DriverService, statistics_service: StatisticsService):
        self.__car_service = car_service
        self.__driver_service = driver_service
        self.__statistics_service = statistics_service

        #self.__commands = {
        #    "1": self.__add_car(),
        #    "2": self.__delete_car(),
        #   "3": self.__show_all_cars(),
        #    "4": self.__show_common_car(),
        #    "5": self.__average_kilometers(),
        #    "6": self.__add_driver(),
        #    "7": self.__delete_car(),
        #    "8": self.__show_all_drivers(),
        #    "9": self.__show_cars_with_no_drivers(),
        #}

    def __print_menu(self):
        print("1. Add taxi car")
        print("2. Remove a car after the registration number")
        print("3. Show all the car of the fleet")
        print("4. Show the most common car in the taxi company")
        print("5. Show the average number of kilometers across the fleet of cars")
        print("6  Add driver")
        print("7. Remove driver")
        print("8. Show all drivers")
        print("9  Cars with no drivers")
        print("0. Exit")

    def __validate_horsepower(self, horsepower):
        try:
            int(horsepower)
        except ValueError:
            raise CustomException("horsepower name is not a number")

    def __add_car(self):
        name = input('name: ')
        registration = input('registration: ')
        horsepower = input('horsepower: ')
        kilometers_on_board = input('kilometers_on_board: ')
        self.__validate_horsepower(horsepower)
        self.__car_service.add_car(Car(name, registration, int(horsepower), int(kilometers_on_board)))

    def __delete_car(self):
        registration = input("REGISTRATION of the car to delete: ")
        name = 'a'
        horsepower = 2
        kilometers_on_board = 2
        self.__car_service.delete_car(Car(name, registration, int(horsepower), int(kilometers_on_board)))

    def __show_all_cars(self):
        for car in self.__car_service.get_all_cars():
            print(car)

    def __show_common_car(self):
        print(self.__car_service.common_car())

    def __average_kilometers(self):
        average_km = round(self.__car_service.average_kilometers(), 2)
        print(f'The average kilometers of the fleet is {average_km}')

    def __add_driver(self):
        name = input('name: ')
        age = input('age ')
        car_name = input('car driven: ')
        self.__driver_service.add_driver(Driver(name, int(age), car_name))
        print("Driver added!")

    def __show_all_drivers(self):
        for drivers in self.__driver_service.get_all_drivers():
            print(drivers)

    def __average_caretaker_age(self):
        average_age = round(self.__driver_service.average_age(), 2)
        print(f'The average age of all the caretakers is {average_age}')

    def __show_cars_with_no_driver(self):
        cars = self.__statistics_service.get_cars_without_drivers()
        if len(cars) == 0:
            print('No animals without caretakers!')
            return
        for animal in self.__statistics_service.get_cars_without_drivers():
            print(animal)

    def run(self):
        print("App started")
        while True:
            self.__print_menu()
            try:
                command = int(input("Choose the option: ").strip())  # sterge spatiile
                if command == 0:
                    return
                elif command == 1:
                    self.__add_car()
                elif command == 2:
                    self.__delete_car()
                elif command == 3:
                    self.__show_all_cars()
                elif command == 4:
                    self.__show_common_car()
                elif command == 5:
                    self.__average_kilometers()
                elif command == 6:
                    self.__add_driver()
                #elif command == 7:
                 #   self.__
                elif command == 8:
                    self.__show_all_drivers()
                elif command == 9:
                    self.__show_cars_with_no_driver()
            except CustomException as error:
                print(error)
