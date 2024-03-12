class Car:
    def __init__(self, name, registration, horsepower, kilometers_on_board):
        self.__name = name
        self.__horsepower = horsepower
        self.__registration = registration
        self.__kilometers_on_board = kilometers_on_board

    def set_name(self, name):
        self.__name = name

    def set_horsepower(self, horsepower):
        self.__horsepower = horsepower

    def set_registration(self, registration):
        self.__registration = registration

    def get_name(self):
        return self.__name

    def get_kilometers_on_board(self):
        return self.__kilometers_on_board

    def get_registration(self):
        return self.__registration

    def __is_broken(self):
        return self.__kilometers_on_board > 5000

    def drive(self):
        if self.__is_broken():
            return f'{self.__name} has broken down'
        self.__kilometers_on_board += 1000
        return f'the {self.__name} has driven for 1000 km'

    def __str__(self):
        return f'Name: {self.__name}, registration: {self.__registration}'

    def __eq__(self, other):
        return self.get_registration() == other.get_registration()

    def __repr__(self):
        return str(self)

