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

# import <package.module.function> : 에러남
# import shapes.volume.cube     # 오류