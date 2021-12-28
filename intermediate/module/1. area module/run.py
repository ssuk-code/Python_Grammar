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

# 모듈의 클래스도 가져올 수 있음
# import <module>
import shapes2d

circle = shapes2d.Circle(2)
print(circle.area())

# from <module> import <member(s)>
from shapes2d import Square, Circle

square = Square(3)
print(square.area())

# from <module> import <member(s)> as <별칭>
from shapes2d import Square as Sq

square = Sq(3)
print(square.area())

# dir(module)) : 모듈의 기능 확인하기
# 함수와 상수, 클래스뿐만 아니라 __특수변수__(__builtins__ 등) 확인 가능
print(dir(area))

# dir() : 현재 파일의 기능 확인하기
# import 방식에 따라 dir()로 나오는 기능의 이름이 바뀜
# as를 이용한 import는 축약형으로 출력
# 특정 함수만 import한 경우는 함수 이름만 출력
print(dir())

# 네임 스페이스
# 같은 함수명으로 여러개의 함수가 정의되었을 때 가장 나중에 정의된 함수 호출
from area import circle, square

def square(length):
    return 4 * length

# area의 square 함수가 아닌 나중에 정의한 square 함수를 출력
print(square(3))

# 중복을 막기 위해 모듈 그대로 import하거나 축약형을 써서 바꿔줘야 함
import area
print(area.square(3))

from area import circle as cr, square as sq
print(sq(3))

# from <module> import *이 권장되지 않는 이유
# 모듈의 모든것을 가져오기 때문에 가져온 것을 확인하기 어렵고, 중복될 확률이 높아짐

# 스크립트 : 프로그램을 작동시키는 코드를 담은 실행 용도의 파일
# 모듈 : 프로그램에 필요한 변수들이나 함수들을 정의해 놓은 파일
# area.py는 모듈 파일, run.py는 스크립트 파일이라고 할 수 있음
# 모듈 안에 실행문을 작성하면 import할 때 모두 실행됨
import area

x = float(input('원의 반지름을 입력해주세요: '))
print('반지름이 {}인 원의 면적은 {}입니다.\n'.format(x, area.circle(x)))

y = float(input('정사각형의 변의 길이를 입력해주세요: '))
print('변의 길이가 {}인 정사각형의 면적은 {}입니다.\n'.format(y, area.square(x)))