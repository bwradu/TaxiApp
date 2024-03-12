class Driver:
    def __init__(self, name, age, car_name):
        self.__name = name
        self.__age = age
        self.__car_name = car_name

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_car_name(self, new_car_name):
        self.__car_name = new_car_name

    def get_car_name(self):
        return self.__car_name

    def __str__(self):
        return f'Name: {self.__name}, Age: {self.__age}, Car name: {self.__car_name}'

    def __eq__(self, other):
        return (self.get_name() == other.get_name()
                and self.get_age() == other.get_age()
                and self.get_car_name() == other.get_car_name())

    def __repr__(self):
        return str(self)
