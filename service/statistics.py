from repository.repository import Repository
from domain.car import Car


class StatisticsService:
    def __init__(self, car_repository: Repository, driver_repository: Repository):
        self.__car_repository = car_repository
        self.__driver_repository = driver_repository

    def __has_driver(self, car: Car):
        driver_list = self.__driver_repository.get_all()
        for driver in driver_list:
            if driver.get_car_name() == car.get_name():
                return True
        return False

    def get_cars_without_drivers(self):
        car_list = self.__car_repository.get_all()
        no_driver_list = []
        for car in car_list:
            if not self.__has_driver(car):
                no_driver_list.append((car))
        return no_driver_list
