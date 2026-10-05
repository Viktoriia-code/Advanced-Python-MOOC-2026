def even_numbers(beginning: int, maximum: int):
    number = beginning + beginning % 2
    while number <= maximum:
        yield number
        number += 2
