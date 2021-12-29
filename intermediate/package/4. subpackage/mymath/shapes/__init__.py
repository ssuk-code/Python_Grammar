# 절대 경로 임포트 : 임포트하려는 것의 경로를 다 풀어서 써 주는 것
# 상대 경로 임포트 : 임포트를 하는 곳의 위치를 기준으로 임포트하려는 것의 위치를 상대적으로 표현
# .은 현재 패키지 안, ..은 상위 패키지 안

# 절대경로 모듈 가져오기
from mymath.shapes import area, volume

# 상대경로 모듈 가져오기
from . import area, volume

# 절대경로 모듈의 함수 가져오기
from mymath.shapes.area import *
from mymath.shapes.volume import *

# 상대경로 모듈의 함수 가져오기
from .area import *
from .volume import *