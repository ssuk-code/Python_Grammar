# 1. 지정연산자(=)

# 파이썬에서 등호는 '같다'의 의미가 아닌 값을 지정해주는 지정연산자
x = 7
x = x + 1

# 2. 함수의 실행 순서

# 14 -> 11 -> 12 -> 16
def hello():
	print("Hello!")
	print("Welcome to World!")

print("함수 호출 전")
hello()
print("함수 호출 후")

# 22 -> 20(파라미터 3) -> 20(파라미터 4) -> 23 -> 24
def square(x):
	return x * x

print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")

# 3. return문 제대로 이해하기

# return문 : 함수가 어떤 값을 돌려줌 + 함수 즉시 종료
# 31 -> 32(파라미터 3) -> 35 -> 36 *return으로 인해 33번 줄은 실행하지 않고 즉시 종료
def square(x):
	print('함수 시작')
	return x * x
	print('함수 끝')

print(square(3))
print('Hello World!')

# 4. return과 print의 차이

def print_sqaure(x):
	print(x * x)

def get_sqaure(x):
	return x * x

print_sqaure(3)	# 콘솔에 9 출력
get_sqaure(3)	# 아무일도 일어나지 않음(9라는 값을 가지지만 출력은 안됨)

print(get_sqaure(3))	# 콘솔에 9 출력
print(print_sqaure(3))
# 콘솔에 9(함수 자체의 출력) 출력, None(print_sqaure(3)은 리턴값이 없어 None으로 대체됨) 출력