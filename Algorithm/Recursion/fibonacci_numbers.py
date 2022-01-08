# Recursive case: 현 문제가 너무 커서, 같은 형태의 더 작은 부분 문제를 재귀적으로 푸는 경우
# Base case: 이미 문제가 충분히 작아서, 더 작은 부분 문제로 나누지 않고도 바로 답을 알 수 있는 경우

# 피보나치 수열
# 시간복잡도 -> O(2^n)
# n번째 피보나치 수를 리턴
def fib(n):
    if n < 3:                       # base case
        return 1
    return fib(n - 2) + fib(n - 1)  # recursive case

# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))

# 재귀 함수 -> 반복문
def fib(n):
    pre = 0
    cur = 1
    for i in range(1, n + 1):
        print(cur)
        pre, cur = cur, cur + pre
        i += 1