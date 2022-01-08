# 자릿수 합
# 인풋 n의 자릿수 개수를 d
# 시간복잡도 -> O(d)
# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    # base case
    if n < 10:
        return n
    # recursive case
    return sum_digits(n // 10) + n % 10

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))

# 재귀 함수 -> 반복문
def sum_digits(n):
    sum = 0
    num = str(n)
    for i in range(len(num)):
        sum += int(num[i])
    return sum

def sum_digits(n):
    return sum(int(num) for num in str(n))

def sum_digits(n):
    return sum(map(int, str(n)))