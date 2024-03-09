from TaxiApp.entities import Car
from TaxiApp.exceptions import CustomException


class Service:
    def __init__(self):
        self.__car_list = [Car('audi', 'SB12TNH', 331, 2), Car('audi', 'SB31CAI', 666, 2)]

    def add_car(self, new_car: Car):
        """
        This function adds a new car to the list
        :param new_car:the car to be added (Car)
        :return:
        """
        for car in self.__car_list:
            if car == new_car:
                raise CustomException(f'The car {new_car.get_manufacturer()} already exists')
        self.__car_list.append(new_car)

    def __get_car_position(self, registration_to_find):
        for i in range(len(self.__car_list)):
            if self.__car_list[i] == registration_to_find:
                return i
        return None

    def remove_car(self, registration):
        car_position = self.__get_car_position(registration)
        if car_position is None:
            raise CustomException(f'The car to delete with reg {registration} does not exist')
        del self.__car_list[car_position]

    def show_cars(self):
        return self.__car_list

    def average_kilometers(self):
        """

        :return: average kilometers of the cars in the fleet
        """
        sum = 0
        for car in self.__car_list:
            sum += car.get_kilometers_on_board()
        average_km = sum / len(self.__car_list)
        return average_km

    def common_car(self):
        max_value = float('-inf')  # Initialize max_value with negative infinity
        final_car = None  # Initialize final_car with None

        lis = []
        manufacturer_dict = {}

        for i in range(len(self.__car_list)):
            lis.append(self.__car_list[i].get_manufacturer())

        for i in lis:
            manufacturer_dict.update({i: lis.count(i)})

        for key, value in manufacturer_dict.items():
            if value > max_value:
                max_value = value
                final_car = key

        return final_car
