
from TaxiApp.service.carservice import CarService
from TaxiApp.domain.animal import Car
from TaxiApp.domain.exceptions import CustomException


class UI:
    def __init__(self, car_service: CarService):
        self.__car_service = car_service

    def __print_menu(self):
        print("1. Add taxi car")
        print("2. Remove a car after the registration number")
        print("3. Show all the car of the fleet")
        print("4. Show the most common car in the taxi company")
        print("5. Show the average number of kilometers across the fleet of cars")
        print("0. Exit")

    def __validate_horsepower(self, horsepower):
        try:
            int(horsepower)
        except ValueError:
            raise CustomException("horsepower name is not a number")


    def __add_car(self):
        manufacturer = input('manufacturer: ')
        registration = input('registration: ')
        horsepower = input('horsepower: ')
        kilometers_on_board = input('kilometers_on_board: ')
        self.__validate_horsepower(horsepower)
        self.__car_service.add_car(Car(manufacturer, registration, int(horsepower), int(kilometers_on_board)))


    def __remove_car(self):
        registration = input("REGISTRATION of the car to delete: ")
        manufacturer = 'a'
        horsepower = 2
        kilometers_on_board = 2
        self.__car_service.remove_car(Car(manufacturer, registration, int(horsepower), int(kilometers_on_board)))

    def __show_cars(self):
        for car in self.__car_service.show_cars():
            print(car)

    def __show_common_car(self):
        print(self.__car_service.common_car())

    def __average_kilometers(self):
        average_km = self.__car_service.average_kilometers()
        average_km = round(self.__car_service.average_kilometers(), 2)
        print(f'The average kilometers of the fleet is {average_km}')

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
                    self.__remove_car()
                elif command == 3:
                    self.__show_cars()
                elif command == 4:
                    self.__show_common_car()
                elif command == 5:
                    self.__average_kilometers()
            except CustomException as error:
                print(error)
