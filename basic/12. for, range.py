# 1. for문

# for 변수 in 범위:
#     실행문
my_list = [2, 3, 5, 7, 11]

# while문
i = 0
while i < len(my_list):
    print(my_list)
    i += 1

# for문
for number in my_list:
    print(number)

# range : 반복적인 작업을 할 때
# 간편하고 깔끔하게 범위를 지정할 수 있고, 메모리 효율성이 좋음
# 파라미터 1개
# 0부터 stop까지의 범위
# for i in range(stop):
#     실행문
for i in range(3, 11):
    print(i)    # 3부터 10 출력

# 파라미터 2개
# start부터 stop까지의 범위
# for i in range(start, stop):
#     실행문
for i in range(3, 11):
    print(i)    # 3부터 10 출력

# 파라미터 3개
# start부터 stop까지의 범위, 간격 step
# for i in range(start, stop, step):
#     실행문
for i in range(3, 17, 3):
    print(i)    # 3부터 16까지 3 간격(3, 6, 9, 12, 15)으로 출력

# 실습과제
# range 연습

# for문과 range 함수를 사용, numbers의 인덱스와 원소를 출력하기
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
for i in range(0, len(numbers)):
    print(i, numbers[i])

# 실습과제
# 거듭제곱

# "2의 n제곱"을 출력하는 프로그램
for i in range(11):
    print(f'2^{i} = {2 ** i}')

# 실습과제
# for문으로 구구단

# 구구단 프로그램을 while문이 아닌 for문을 사용해서 만들기
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')

# 실습과제
# 피타고라스 삼조

# 피타고라스 정리(a^2 + b^2 = c^2)를 만족하는 세 자연수 쌍(a, b, c) 구하기
for a in range(1, 400):
    for b in range(1, 400-a):
        c = 400 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)

# 실습과제
# 리스트 뒤집기

# numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집기
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
for left in range(len(numbers) // 2):
    # 인덱스 left와 대칭인 인덱스 right 계산    
    right = len(numbers) - left - 1
    # 위치 바꾸기
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))