# 1. comment(주석)

#, ''''''로 표현 가능
# 한 줄로 표현 가능시 맨 앞에 #을 붙여 사용
# 여러 줄인 경우에 '''''' 사이에 넣어 사용
# 주석 처리하고 싶은 영역을 드래그 하여 ctrl + /로 한번에 주석 처리 가능
'''
코멘트 사용 이유
- 복잡한 코드 설명
- 하다가 만 부분 표시
- 다른 개발자들과 소통
'''

# 2. variable(변수)

# '변수명 = 데이터 값'로 선언과 값 저장을 한 번에 함
# 'a, b, c, ... = 1, 2, 3, ...'
# 여러 개의 변수를 한 번에 저장 가능
# 파이썬은 데이터의 종류(자료형)를 표기하지 않아도 돰
'''
변수를 사용하는 이유
- 코드의 재활용성과 가독성을 높여줌
- 중복을 제거하여 유지보수가 용이함
'''

# 실습과제
# 칼로리 계산기

# 변수 선언
kitkat_calorie = 190
oreos_calorie = 502
pringles_calorie = 292
twix_calorie = 135.9
cheetos_calorie = 485

# 다양한 과자 조합
print(kitkat_calorie + oreos_calorie * 2)
print(cheetos_calorie * 4)
print(pringles_calorie + oreos_calorie + twix_calorie)
print(pringles_calorie * 3 + oreos_calorie * 2)