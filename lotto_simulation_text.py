import random

def generate_numbers(n):
    number = list(range(1,46))
    random_number = random.sample(number, n)

    print(sorted(random_number))


generate_numbers(6)