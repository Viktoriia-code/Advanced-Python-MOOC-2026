def prime_numbers():
    number = 2

    while True:
        is_prime = True

        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            yield number

        number += 1
