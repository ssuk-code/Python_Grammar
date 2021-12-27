from random import randint

# 무작위로 1과 45 사이의 서로 다른 번호 n개를 추출 
# 그 번호들이 담긴 리스트를 리턴
def generate_numbers(n):
    # 리턴할 리스트 생성
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        # 중복을 막기 위한 조건문
        if num not in numbers:
            numbers.append(num)
    
    return numbers

# 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴
# 일반 당첨 번호 6개는 정렬, 보너스 번호는 마지막에 추가
def draw_winning_numbers():
    # 7자리 당첨 번호 받아오기
    winning_numbers = generate_numbers(7)
    # 6자리 정렬 후 보너스번호 추가
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

# 파라미터로 리스트 list_1과 리스트 list_2 받음
# 두 리스트 사이에 겹치는 번호 개수를 리턴
def count_matching_numbers(numbers, winning_numbers):
    count = 0

    for num in numbers:
        if num in winning_numbers:
            count += 1

    return count

# 참가자의 당첨 금액을 리턴
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0