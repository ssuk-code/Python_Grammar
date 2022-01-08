# 숫자 합
# 시간복잡도 -> O(n)
def triangle_number(n):
    # base case
    if n == 1:
        return 1
    # recursive case
    return triangle_number(n - 1) + n

# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))
    
# 재귀 함수 -> 반복문
def triangle_number(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

def triangle_number(n):
    return sum(n for n in range(1, n + 1))