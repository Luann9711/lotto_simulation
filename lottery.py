import random

# 6개의 1~45 중의 난수를 생성한다
def generate_numbers(n):
    number = list(range(1,46))
    random_number = random.sample(number, n)

    return sorted(random_number)

# 위에서 생성한 6개의 난수에 보너스 숫자를 하나 더 추가하여 반환한다
def draw_winning_numbers():
    winning_numbers = generate_numbers(6)
    number = list(range(1,46))
    bonus_number_list = []
    
    for i in number:
        if i not in winning_numbers:
            bonus_number_list += [i]
    
    bonus_number = random.choice(bonus_number_list)
    winning_numbers.append(bonus_number)
    
    return winning_numbers

# 리스트 2개를 대조하여 두 리스트 사이에 겹치는 번호 개수를 리턴한다
def count_matching_numbers(numbers, winning_numbers):
    same_num = list(set(numbers).intersection(set(winning_numbers)))
    return len(same_num)



def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
    
    # 1등 당첨시
    if (count == 6) and (bonus_count == 0):
        return 1000000000
    
    # 2등 당첨시
    elif (count == 5) and (bonus_count == 1):
        return 50000000
    
    # 3등 당첨시
    elif (count == 5) and (bonus_count == 0):
        return 1000000
    
    # 4등 당첨시
    elif (count == 4) and (bonus_count == 0):
        return 50000
    
    # 5등 당첨시
    elif (count == 3) and (bonus_count == 0):
        return 5000


# 테스트
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))