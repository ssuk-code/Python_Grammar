# 1. function(함수)

# 내장 함수(패키지, 라이브러리 등)
# 내장 함수의 경우 함수명을 작성하면 됨
# print(), round()...
'''
사용자 정의 함수
def 함수명():	# 함수 정의 부분
	기능 1		# 함수 정의 부분
	기능 2 ...	# 함수 정의 부분

함수명()			# 함수 실행
'''
'''
함수를 사용하는 이유
- 여러 개의 함수로 나누어 작성하면, 모듈화로 인해 전체적인 코드의 가독성이 좋아짐
- 중복을 제거하여 반복적인 프로그래밍을 피하고 문제가 발생하거나 기능을 변경할 때 유지보수가 용이함
'''

# 실습과제
# 카페 모카 레시피

# 함수 정의 
def cafe_mocha_recipe():
    print('1. 준비된 컵에 초코 소스를 넣는다.')
    print('2. 에스프레소를 추출하고 잔에 부어 준다.')
    print('3. 초코 소스와 커피를 잘 섞어 준다.')
    print('4. 거품기로 우유 거품을 내고, 잔에 부어 준다.')
    print('5. 생크림을 얹어 준다.')

# 함수 실행
cafe_mocha_recipe()