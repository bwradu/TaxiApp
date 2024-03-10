class Car:
    def __init__(self, manufacturer, registration, horsepower, kilometers_on_board):
        self.manufacturer = manufacturer
        self.horsepower = horsepower
        self.registration = registration
        self.__kilometers_on_board = kilometers_on_board

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_horsepower(self, horsepower):
        self.horsepower = horsepower

    def set_registration(self, registration):
        self.registration = registration

    def get_manufacturer(self):
        return self.manufacturer

    def get_kilometers_on_board(self):
        return self.__kilometers_on_board

    def get_registration(self):
        return self.registration

    def __is_broken(self):
        return self.__kilometers_on_board > 5000

    def drive(self):
        if self.__is_broken():
            return f'{self.manufacturer} has broken down'
        self.__kilometers_on_board += 1000
        return f'the {self.manufacturer} has driven for 1000 km'

    def __str__(self):
        return f'Name: {self.manufacturer}, registration: {self.registration}'

    def __eq__(self, other):
        return self.get_registration() == other.get_registration()

    def __repr__(self):
        return str(self)

