from domain.car import Car
from repository.repository import Repository


class CarService:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_car(self, new_car: Car):
        """
        This function adds a new car to the list
        :param new_car:the car to be added (Car)
        :return:
        """
        self.__repository.add(new_car)

    #def __get_car_position(self, registration_to_find):
    #   for car in self.__repository.get_all():
    #        if car.get_registration() == registration_to_find:
    #            return car.get_registration()
    #    return None

    #def delete_car(self, registration):
    #    car_position = self.__get_car_position(registration)
    #    if car_position is None:
    #        raise CustomException(f'The car to delete with reg {registration} does not exist')
    #    del self.__car_list[car_position]

    def delete_car(self, car_to_delete):
        self.__repository.delete(car_to_delete)

    def get_all_cars(self):
        return self.__repository.get_all()

    def average_kilometers(self):
        sum = 0
        for car in self.__repository.get_all():
            sum += car.get_kilometers_on_board()
        average_km = sum / len(self.__repository.get_all())
        return average_km


    def common_car(self):
        max_value = float('-inf')  # Initialize max_value with negative infinity
        final_car = None  # Initialize final_car with None

        lis = []
        manufacturer_dict = {}

        for car in self.__repository.get_all():
            lis.append(car.get_name())

        for i in lis:
            manufacturer_dict.update({i: lis.count(i)})

        for key, value in manufacturer_dict.items():
            if value > max_value:
                max_value = value
                final_car = key
        return final_car
