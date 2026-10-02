class Car:
    def __init__(self):
        self.__petrol = 0
        self.__kilometres = 0

    def __str__(self):
        return f"Car: odometer reading {self.__kilometres} km, petrol remaining {self.__petrol} litres"

    def fill_up(self):
        self.__petrol += 60

    def drive(self, kilometres_amount):
        if kilometres_amount < self.__petrol:
            self.__kilometres += kilometres_amount
            self.__petrol -= kilometres_amount
        else:
            self.__kilometres += self.__petrol
            self.__petrol = 0