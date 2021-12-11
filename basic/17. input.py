# input : 사용자 입력

name = input('이름을 입력하세요: ')
print(name)

# input으로 들어온 데이터는 str형이기 때문에 형변환 필요
x = int(input('숫자를 입력하세요: '))
print(x + 5)

# 실습과제
# 숫자 맞히기 게임

# 프로그램을 실행하면 "기회가 *번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: "가 출력됩니다. 총 네 번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회 횟수가 줄어듭니다.
# 정답을 맞히면 "축하합니다. *번 만에 숫자를 맞히셨습니다."가 출력되고 프로그램은 종료됩니다.
# 사용자가 입력한 수가 정답보다 작은 경우 "Up"이 출력되고, 입력한 수가 정답보다 큰 경우 "Down"이 출력됩니다.
# 정답이 틀렸으면 1번부터 다시 진행합니다. 만약 네 번의 기회를 모두 사용했는데도 답을 맞히지 못했으면, "아쉽습니다. 정답은 *입니다."가 출력되고 프로그램은 종료됩니다.
import random

random_num = random.randint(1, 20)

count = 4
while count > 0:
    user_num = int(input(f'기회가 {count}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: '))
    if random_num == user_num :
        print(f'축하합니다. {5 - count}번 만에 숫자를 맞히셨습니다.')
        break
    elif random_num > user_num:
        print('Up')
        count -= 1
    elif random_num < user_num:
        print('Down')
        count -= 1

if count == 0:
    print(f'아쉽습니다. 정답은 {random_num}입니다.')

# # 상수 정의
# ANSWER = random.randint(1, 20)
# NUM_TRIES = 4

# # 변수 정의
# guess = -1
# tries = 0

# while guess != ANSWER and tries < NUM_TRIES:
#     guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(NUM_TRIES - tries)))
#     tries += 1    
    
#     if ANSWER > guess:
#         print("Up")
#     elif ANSWER < guess:
#         print("Down")

# if guess == ANSWER:
#     print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
# else:
#     print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))