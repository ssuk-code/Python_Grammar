def countdown(n):
    if n > 0:
        print(n)
        countdown(n - 1)

countdown(4)    # 4, 3, 2, 1

# 팩토리얼(Factorial)
def factorial(n):
    if n == 0:                  # base case : 문제가 충분히 작아서 바로 풀 수 있는 경우
        return 1
    return factorial(n - 1) * n # recursive case : 재귀적으로 부분 문제를 푸는 경우

print(factorial(4))

# 반복문으로 해결할 수 있는 건 재귀 함수로도 해결 가능함
# 반복문
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적
# 함수의 동작방식을 알아야 함
# 재귀 함수 호출이 너무 많으면 call stack(위치를 기록해두는 메모리 공간)이 많이 쌓여
# 과부화로 인해 프로그램 중단됨
# 파이썬은 call stack을 1000개까지만 허용함
# 재귀함수를 이용하면 반목문 코드보다 깔끔해짐
def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n