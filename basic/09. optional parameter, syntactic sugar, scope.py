# 1. Optional parameter

# 함수 호출을 할 때 파라미터에 해당되는 값을 넘겨주지 않았을 경우, 기본값을 갖게 하는 파라미터
# 옵셔널 파라미터는 무조건 마지막에 있어야 함(여러 개도 가능함)
def myself(name, age, nationality = "한국"):
    print("내 이름은 %s" % name)
    print("나이는 %d살" % age)
    print("국적은 %s" % nationality)

myself("인숙", 1)			# 기본값이 설정된 파라미터를 바꾸지 않을 때(한국으로 출력)
myself("인숙", 1, "미국")	# 기본값이 설정된 파라미터를 바꾸었을 때(미국으로 출력)

# 파라미터를 표기하여 옵셔널 파라미터 중 일부만 수정 가능
def introduce(name, nation="korea", city="seoul"):
    print(f'{name}은(는) {nation}의 {city} 출신이다')

introduce("인숙"﻿, city="Busan")

# 2. Syntactic Sugar

# 간략하게 줄일 수 있는 문법
x += 1		# x = x + 1와 동일
x += 2		# x = x + 2와 동일
x *= 2		# x = x * 2와 동일
x -= 3		# x = x - 3와 동일
x /= 2		# x = x / 2와 동일
x %= 7		# x = x % 7와 동일

# 가독성을 올려줄 수 있는 문법
print(1_000_000_000_000) # print(1000000000000)와 동일

# list comprehension
# [ ( 변수를 활용한 값 ) for ( 사용할 변수 이름 ) in ( 순회할 수 있는 값 )]
size = 10
arr = [0] * size
for i in range(len(size)):
    arr[i] = i * 2

size = 10
arr = [i * 2 for i in range(size)]

# *args와 **kwargs
# *변수 : 여러 개가 아규먼트로 들어올 때, 함수 내부에서는 해당 변수를 '튜플'로 처리함
# **변수 : 키워드 = ''로 입력할 경우 그것을 각각 키와 값으로 가져오는 '딕셔너리'로 처리함

# 3. scope(범위) : 변수가 사용 가능한 범위

# 지역변수(Local Variable) : 변수를 정의한 함수 내에서만 사용 가능
# 전역변수(Global Variable) : 모든 곳에서 사용 가능
# 지역변수 확인 후 전역변수를 확인해야함

# 지역변수만 선언
# def my_function():
# 	x = 3
# 	print(x)

# my_function()
# print(x)	# x(지역변수)는 함수 내에 만들어진 지역변수이므로 에러가 발생함

# 전역변수만 선언
x = 2

def my_function():
	print(x)		# 2 출력

my_function()
print(x)			# 2 출력

# 지역변수와 전역변수 모두 선언
x = 2

def my_function():
	x = 3
	print(x)		# 3 출력

my_function()
print(x)			# 2 출력

# 상수(constant) : 프로그램 내내 바뀌지 않는 값
# 전역변수의 가장 좋은 예시, 예를 들면 원주율이 있음
# 상수는 처음에 설정하고 바꾸면 절대 안됨
# 상수의 이름은 대문자로 써줘야함

# 실습과제
# 짝수? 홀수?

# 함수 is_evenly_divisible은 number라는 정수값을 파라미터로 받고, 그 값이 짝수인지 홀수인지 판단
# 짝수인 경우 True를 리턴, 홀수인 경우 False를 리턴
def is_evenly_divisible(number):
    return number % 2 == 0

print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))

def is_evenly_divisible(number):
    result = "짝수" if number % 2 == 0 else "홀수"
    return result

print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))

# 실습과제
# 거스름돈 계산기

# '가장 적은 수'의 지폐를 거슬러 주기
def calculate_change(payment, cost):
    change = (payment - cost)
    a = int(change // 50000)
    b = int((change % 50000) // 10000)
    c = int((change % 10000) // 5000)
    d = int((change % 5000) // 1000)
    print(f'50000원 지폐: {a}장')
    print(f'10000원 지폐: {b}장')
    print(f'5000원 지폐: {c}장')
    print(f'1000원 지폐: {d}장')
    
# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)

# 반복문을 통해 간단히 출력
def calculate_change(payment, cost):
    money_list = [50000, 10000, 5000, 1000]

    change = payment - cost
    money_count_list = []
    for money in money_list:
        money_count = change // money
        money_count_list.append(money_count)
        change %= money

    for i in range(len(money_list)):
        print("%d원 지폐: %d장" % (money_list[i], money_count_list[i]))