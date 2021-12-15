import random

def generate_numbers(n):
    number = list(range(1,46))
    random_number = random.sample(number, n)

    return sorted(random_number)


def draw_winning_numbers():
    winning_numbers = generate_numbers(6)
    number = list(range(1,46))
    bonus_number_list = []
    
    for i in number:
        if i not in winning_numbers:
            bonus_number_list += [i]
    
    bonus_number = random.choice(bonus_number_list)
    winning_numbers.append(bonus_number)
    
    print(winning_numbers)

draw_winning_numbers()

