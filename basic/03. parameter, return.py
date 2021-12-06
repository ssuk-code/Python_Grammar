# 1. parameter(매개 변수)

# 함수에 넘겨 주는 값, 지역변수의 일종
# 변수나 함수를 파라미터로 정할 수 있음
'''
파라미터에 떠라 함수 실행 값이 조금씩 달라짐
def 함수명(파라미터):
	기능(파라미터)

함수명(파라미터)
'''
'''
파라미터 조건
- 변수나 데이타에 할당 할 수 있어야 함
- 객체의 인자로 넘길 수 있어야 함
- 객체의 리턴값으로 리턴할 수 있어야 함
'''

# 2. 여러 개의 파라미터
# 파라미터는 개수 제한 없이 정할 수 있음

def print_sum(a, b, c):
	print(a + b + c)

print_sum(3, 7, 2)

# 실습과제
# 세 수의 곱

# 함수 정의
def multiply_three_numbers(a, b, c):
	print (a * b * c)

# 함수 실행
multiply_three_numbers(7, 3, 5)
multiply_three_numbers(21, 4, 9)
multiply_three_numbers(-7, 6, 3)

# 3. return

# 함수를 통해 돌려주는 값
def get_square(x):
	return x * x

# print(get_square(3))

# y = get_square(3)
# print(y)

print(get_square(3) + get_square(4))