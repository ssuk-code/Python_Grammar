# 기본적인 모듈 호출법
import area

# 모듈을 통해 함수 호출 가능
print(area.circle(2))
print(area.square(3))

# 함수 뿐만 아니라 상수도 호출 가능
print(area.PI)

# 함수 일부분이 필요한 경우 메모리 효율을 위해 함수 일부분만 호출
from area import circle

print(circle(2))

# 호출할 함수가 여러 개인 경우 ,를 이용해 호출
from area import circle, square

print(square(2))

# 모듈 이름을 축약형으로 호출할 수 있음
import area as ar

print(ar.circle(2))

# 함수 이름을 축약형으로 호출할 수 있음
from area import square as sq

print(sq(2))

# 모듈의 모든 내용을 가져옴
# import 모듈과 다른점은 함수 호출할 때 모듈 이름을 안붙여도 됨
# 함수가 어디에서 왔는지 파악이 어렵고 쓸데없는 내용을 가져올 수 있기 때문에 권장 X
from area import *

print(circle(2))
print(PI)