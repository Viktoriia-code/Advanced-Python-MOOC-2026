# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.sum = 0

    def add_number(self, number:int):
        self.numbers += 1
        self.sum += number

    def count_numbers(self):
        return self.numbers
    
    def get_sum(self):
        return self.sum
    
    def average(self):
        if self.numbers:
            return self.sum / self.numbers
        return 0

user_numbers = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()
print("Please type in integer numbers:")
while True:
    number = int(input(""))
    if number == -1:
        break
    user_numbers.add_number(number)
    if number%2 == 0:
        even_numbers.add_number(number)
    else:
        odd_numbers.add_number(number)
print(f"Sum of numbers: {user_numbers.get_sum()}")
print(f"Mean of numbers: {user_numbers.average()}")
print(f"Sum of even numbers: {even_numbers.get_sum()}")
print(f"Sum of odd numbers: {odd_numbers.get_sum()}")