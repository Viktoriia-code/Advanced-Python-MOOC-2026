class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance -= self.__balance * 0.01

    def deposit(self, amount: float):
        if amount >= 0:
            self.__balance += amount
            self.__service_charge()
        else:
            raise ValueError("The amount must not be below zero")

    def withdraw(self, amount: float):
        if amount >= 0:
            self.__balance -= amount
            self.__service_charge()
        else:
            raise ValueError("The amount must not be below zero")