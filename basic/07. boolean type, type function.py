# 1. 불 대수

# 일상적인 논리를 수학적으로 표현한 것

# 일반 수학의 값 = 숫자, 일반 수학의 연산 = +, -, *, /
# 불 대수의 값 = 진리값(True, False), 불 대수의 연산 = AND, OR, NOT

# 명제 : 참과 거짓으로 판별할 수 있는 문장

# AND 연산 : 명제 x와 명제 y가 모두 참일 때만 x AND y는 참
# and 대신 &로 표현 가능
True and True	# True
True&True 		# True
True and False	# False
False and True	# False
False and False	# False

# OR 연산 : 명제 x와 명제 y 중 하나라도 참이면 x OR y는 참
# or 대신 |로 표현 가능
True or True	# True
True|True 		# True
True or False	# True
False or True	# True
False or False	# False

# XOR 연산 : 명제 x와 명제 y가 같으면 거짓, 다르면 참
# ^로 표현
True^True	# False
True^False	# True
False^True	# True
False^False	# False

# NOT 연산 : 명제를 부정
# not 대신 ~로 표현 가능
# not은 -(x + 1)을 반환함
# print(~True) True는 1이기 때문에 -(x + 1) = -2
# Print(~False ) False는 0이기 때문에 -(x + 1) = -1
not True	# False
~True 		# -2
not False 	# True
~False 		# -1

# 2. 불린(Boolean)

print(2 > 1)	# True
print(2 < 1)	# False
print(3 >= 2)	# True
print(3 <= 3)	# True
print(2 == 2)	# True
print(2 != 2)	# False

print('Hello' == 'Hello')	# True
print('Hello' != 'Hello')	# False

print(2 > 1 and 'Hello' == 'Hello')	# True

print(not not True)		# True
print(not not False)	# False

print(7 == 7 or (4 < 3 and 12 > 10))	# True

x = 3
print(x > 4 or not(x < 2 or x == 3))	# False

# 3. type function

# 자료형 확인 가능
print(type(3))		# <class 'int'>
print(type(3.0))	# <class 'float'>
print(type('3'))	# <class 'str'>

print(type('True'))	# <class 'str'>
print(type(True))	# <class 'bool'>

def hello():
	print("Hello World!")
print(type(hello))	# <class 'function'> 사용자정의함수
print(type(print))	# <class 'builtin_function_or_method'> 내장함수