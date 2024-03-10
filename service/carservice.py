from TaxiApp.domain.animal import Car
from TaxiApp.domain.exceptions import CustomException
from TaxiApp.repository.repository import Repository

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
    #   for i in range(len(self.__car_list)):
    #        if self.__car_list[i] == registration_to_find:
    #            return i
    #    return None

    #def remove_car(self, registration):
    #    car_position = self.__get_car_position(registration)
    #    if car_position is None:
    #        raise CustomException(f'The car to delete with reg {registration} does not exist')
    #    del self.__car_list[car_position]

    def remove_car(self, registration):
         try:
             self.__repository(registration)
         except CustomException:
             raise CustomException("Car does not exist")



    def show_cars(self):
        return self.__repository.get_all()

    def average_kilometers(self):
        """

        :return: average kilometers of the cars in the fleet
        """
        sum = 0
        for car in self.__repository.get_all():
            sum += car.get_kilometers_on_board()
        average_km = sum / len(self.__repository.get_all())
        return average_km

    #def common_car(self):
     #   max_value = float('-inf')  # Initialize max_value with negative infinity
      #  final_car = None  # Initialize final_car with None

#        lis = []
 #       manufacturer_dict = {}
#
 #       for i in range(len(self.__car_list)):
  #          lis.append(self.__car_list[i].get_manufacturer())

   #     for i in lis:
    #        manufacturer_dict.update({i: lis.count(i)})

     #   for key, value in manufacturer_dict.items():
      #      if value > max_value:
       #         max_value = value
        #        final_car = key

        #return final_car

    def common_car(self):
        max_value = float('-inf')  # Initialize max_value with negative infinity
        final_car = None  # Initialize final_car with None

        lis = []
        manufacturer_dict = {}

        for i in range(len(self.__repository.get_all())):
            lis.append(self.__repository.get_all().get_manufacturer())

        for i in lis:
            manufacturer_dict.update({i: lis.count(i)})

        for key, value in manufacturer_dict.items():
            if value > max_value:
                max_value = value
                final_car = key

        return final_car

