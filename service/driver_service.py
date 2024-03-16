from domain.driver import Driver
from repository.repository import Repository


class DriverService:
    def __init__(self, repository: Repository):
        self.__repository = repository

    def add_driver(self, new_driver: Driver):
        """
        This function adds a new driver to the list
        :param new_driver:the driver to be added (Driver)
        :return:
        """
        self.__repository.add(new_driver)

    def delete_driver(self, driver_to_delete):
        self.__repository.delete(driver_to_delete)

    def get_all_drivers(self):
        return self.__repository.get_all()

    def average_age(self):
        """
        :return: average age of the drivers in the fleet
        """
        sum = 0
        for driver in self.__repository.get_all():
            sum += driver.get_age()
        average_age = sum / len(self.__repository.get_all())
        return average_age

