# import <package.module>
import shapes.volume

print(shapes.volume.cube(3))

# import <package.module> as <축약형>
import shapes.volume as vol

print(vol.cube(3))

# from <package.module> import <function>
from shapes.area import square

print(square(3))

# from <package> import <modules>
from shapes import volume

print(volume.cube(3))

# import <package>
# <package.module.function> : 에러남
# import shapes

# print(shapes.area.circle(2))  # 오류
# 오류를 없애기 위해서 __init__.py 파일에 from shapes import area, volume 코드 추가

# __init__.py에 from shapes.area import circle, square를 추가했다면
# shapes.circle(2)로 함수 사용 가능

# import <package.module.function> : 에러남
# import shapes.volume.cube     # 오류

# __init__.py에서 정의한 상수 사용
# 패키지 밖에서도 사용 가능함
from shapes import PI

import shapes

shapes.PI