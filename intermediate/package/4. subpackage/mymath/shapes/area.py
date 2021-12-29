# 절대 경로 함수 가져오기
from mymath.stats.average import data_mean

# 상대 경로 함수 가져오기
# 상대 경로가 복잡해지는 경우 (주로 ..을 쓰는 경우)에는 그냥 절대 경로를 쓰는 것이 좋음
from ..stats.average import data_mean

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length