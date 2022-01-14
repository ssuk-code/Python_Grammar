# 최적 부분 구조가 있음
# ↓
# 부분 문제들의 최적의 답을 이용해서 기존 문제를 풀 수 있음
# (기존 문제를 부분 문제로 나눠서 풀 수 있음)
# ↓
# 중복되는 부분 문제들이 있을 수 있음

# 1. 최적 부분 구조가 있음
# 2. 중복되는 부분 문제들이 있음
# Dynamic Programming으로 해결 가능

# Dynamic Programming : 한 번 계산한 결과를 재활용하는 방식
# 중복되는 부분 문제의 비효율을 해결
# 1. Memoization
# 2. Tabulation

# Memoization
# 재귀 기반의 하향식 접근(Top-down Approach) 방법
# 재귀 호출이 너무 일어나면 과부화(콜스택 쌓임)로 인한 오류 위험이 있음
def fib_memo(n, cache):
    # base case
    if n == 1 or n == 2:
        return 1
    
    # 이미 n번째 피보나치를 계산했으면:
    # 저장된 값을 바로 리턴
    if n in cache:
        return cache[n]
    
    # 이미 n번째 피보나치를 계산했으면:
    # 저장된 값을 바로 리턴
    cache[n] = fib_memo(n - 2, cache) + fib_memo(n - 1, cache)
    
    # 계산한 값을 리턴
    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
    
    return fib_memo(n, fib_cache)

# 테스트
print(fib(10))
print(fib(50))
print(fib(100))

# Tabulation : 표를 채우듯 하나씩 올라가서 계산
# 반복문 기반의 상향식 접근(Bottom-up Approach) 방법
# 처음부터 모두 계산하기 때문에 필요없는 계산을 할 수 있음
def fib_tab(n):
    # 이미 계산된 피보나치 수를 담는 리스트
    table = [0, 1, 1]
    
    # n번째 피보나치 수까지 리스트 채우기
    for num in range(3, n + 1):
        table.append(table[num - 2] + table[num - 1])
    
    # n번째 피보나치 수를 리턴
    return table[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))

# Tabulation 공간 최적화
def fib_optimized(n):
    # 리스트 대신 변수를 이용해 공간복잡도를 O(n)에서 O(1)로 줄임
    current = 1
    previous = 0

    # 반복적으로 변수 업데이트
    for num in range(1, n):
        current, previous = current + previous, current
    
    # n번째 피보나치 수를 리턴
    return current

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))