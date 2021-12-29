# module의 __all__ : 모듈에 해당하는 파일에서 정의
# from shapes.area import * : circle과 square 함수만 임포트
__all__ = ['circle', 'square'] 

# __init__.py에서 정의한 상수 사용
from shapes import PI

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length