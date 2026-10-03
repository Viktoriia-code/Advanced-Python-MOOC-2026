# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents
    
    def __gt__(self, another):
        if self.__euros > another.__euros:
            return True
        elif self.__euros < another.__euros:
            return False
        return self.__cents > another.__cents
    
    def __lt__(self, another):
        if self.__euros < another.__euros:
            return True
        elif self.__euros > another.__euros:
            return False
        return self.__cents < another.__cents
    
    def __add__(self, another):
        new_money = Money(self.__euros, self.__cents)
        new_money.__cents += another.__cents
        if new_money.__cents >= 100:
            new_money.__euros += 1
            new_money.__cents -= 100
        new_money.__euros += another.__euros
        return new_money
    
    def __sub__(self, another):
        new_money = Money(self.__euros, self.__cents)
        if new_money < another:
            raise ValueError('a negative result is not allowed')
        new_money.__cents -= another.__cents
        if new_money.__cents < 0:
            new_money.__euros -= 1
            new_money.__cents = 100 + new_money.__cents
        new_money.__euros -= another.__euros
        return new_money

