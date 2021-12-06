# 1. number type(숫자형)

# integer(int, 정수형)와 floating point(float, 소수형)
# 정수형끼리 계산값은 정수형, 정수형과 소수형의 계산값은 소수형
# 소수형끼리 계산값은 소수형, 나눗셈은 항상 소수형

# 덧셈
print(7 + 4)

# 뺄셈
print(7 - 4)

# 곱셈
print(7 * 4)

# 나눗셈(나머지)
print(7 % 4)

# 거듭제곱(밑 ** 지수)
print(2 ** 3)

# 나눗셈
print(7 / 4)

# 연산자 우선 순위
# https://docs.python.org/ko/3/reference/expressions.html#operator-precedence 참고
# 곱셈이나 나눗셈 먼저 계산
# 괄호가 있다면 괄호 안부터 계산
print(1 + 3 * 7)
print((1 + 3) * 7)

# floor division(버림 나눗셈, 몫)
print(7 // 4)

# round(반올림할 숫자, n번째자리까지 반올림)
print(round(3.141926535, 2))