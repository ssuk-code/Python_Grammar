# 1. while

# while 조건:
#     실행문
# 조건이 True일 때만 수행, False면 반복문 종료
i = 1
while i <= 3:
    print("반복")
    i += 1

# 실습과제
# while문 연습 I

# while 반복문을 사용하여 1 이상 100 이하의 짝수를 모두 출력
i = 1
while i <= 50:
    print(i * 2)
    i += 1

# 실습과제
# while문 연습 II

# while문을 사용하여, 100 이상의 자연수 중 가장 작은 23의 배수를 출력
i = 100
while i % 23 != 0:
    i += 1
print(i)

# 2. break, continue

# 만약 while문의 조건 부분과 상관 없이 반복문에서 나오고 싶으면 break문을 사용
i = 100

while True:
    # i가 23의 배수면 반복문을 끝냄
    if i % 23 == 0:
        break
    i += 1

print(i)

# 현재 진행되고 있는 수행 부분을 중단하고 바로 조건 부분을 확인하고 싶으면 continue문을 사용
i = 0

while i < 15:
    i += 1
    # i가 홀수면 print(i) 안 하고 바로 조건 부분으로 돌아감
    if i % 2 == 1:
        continue
    print(i)

# 3. if, elif, else

# if 조건:
#     실행문
# elif 조건:
#     실행문
# else:
#     실행문
# 조건이 True일 때만 if 수행, False면 elif문으로 이동 후 True면 elif문 수행, 마지막까지 False면 else문 수행
temperature = 8

if temperature <= 10:
    print('자켓을 입는다.')
else:
    print('자켓을 입지 않는다.')

# 실습과제
# 학점 계산기

# rint_grade 함수는 파라미터로 중간고사 점수 midterm_score와 기말고사 점수 final_score를 받고, 최종 성적을 출력
# A: 90점 이상
# B: 80점 이상 90점 미만
# C: 70점 이상 80점 미만
# D: 60점 이상 70점 미만
# F: 60점 미만
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90:
        print('A')
    elif total < 90 and total >= 80:
        print('B')
    elif total < 80 and total >= 70:
        print('c')
    elif total < 70 and total >= 60:
        print('D')
    else:
        print('F')

# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)

# 실습과제
# 이상한 수학 문제 I

# while문과 if문을 활용하여, 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력
num = 1

while num <= 100:
    if num % 8 == 0 and num % 12 != 0:
        print(num)
    num += 1

# 실습과제
# 이상한 수학 문제 II

# while문과 if문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합 출력
num = 1
sum = 0

while num < 1000:
    if num % 2 == 0 or num % 3 == 0:
        sum += num
    num += 1

print(sum)

# 실습과제
# 약수 찾기

# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력
num = 0
i = 1

while i <= 120:
    if 120 % i == 0:
        print(i)
        num += 1
    i += 1

print(f'120의 약수는 총 {num}개입니다.')

# 실습과제
# 택이의 우승 상금

year = 1988
money = 50_000_000
rate = 0.12
apartment = 1_100_000_000

while year < 2016:
    money += money * rate
    year += 1

if money > apartment:
    print(f"{int(money - apartment)}원 차이로 동일 아저씨 말씀이 맞습니다.")
else: 
    print(f"{int(apartment - money)}원 차이로 미란 아주머니가 말씀이 맞습니다.")

# 실습과제
# 피보나치 수열

# 피보나치 수열의 첫 50개 항을 차례대로 출력하는 프로그램 작성
pre = 0
cur = 1
i = 1

while i <= 50:
    print(cur)
    pre, cur = cur, cur + pre
    i += 1

# 실습과제
# 구구단

# while문을 사용해서 구구단 프로그램 작성
i = 1

while i < 10:
    j = 1
    while j < 10:
        print(f'{i} * {j} = {i * j}')
        j += 1
    i += 1