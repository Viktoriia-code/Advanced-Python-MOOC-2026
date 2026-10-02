# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
             self.balance -= amount
             return True
        else:
            return False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        regular_lunch_price = 2.5
        if payment >= regular_lunch_price:
            self.funds += regular_lunch_price
            self.lunches += 1
            return payment - regular_lunch_price
        else:
            return payment
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of lunches sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.

    def eat_special(self, payment: float):
        special_lunch_price = 4.3
        if payment >= special_lunch_price:
            self.funds += special_lunch_price
            self.specials += 1
            return payment - special_lunch_price
        else:
            return payment
        # A special lunch costs 4.30 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of specials sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.

    def eat_lunch_lunchcard(self, card: LunchCard):
        regular_lunch_price = 2.5
        if card.balance >= regular_lunch_price:
            card.balance -= regular_lunch_price
            self.lunches += 1
            return True
        else:
            return False

    def eat_special_lunchcard(self, card: LunchCard):
        special_lunch_price = 4.3
        if card.balance >= special_lunch_price:
            card.balance -= special_lunch_price
            self.specials += 1
            return True
        else:
            return False
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount