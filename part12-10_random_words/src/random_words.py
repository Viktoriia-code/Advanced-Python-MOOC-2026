import random

def word_generator(characters: str, length: int, amount: int):
    for i in range(amount):
        word = ""

        for j in range(length):
            word += random.choice(characters)

        yield word
