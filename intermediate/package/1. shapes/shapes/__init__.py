# 패키지 : 모듈 파일의 모음 폴더
# 패키지 폴더를 만들 때 __init__.py 파일을 꼭 만들어야 실행됨
# 처음으로 패키지나 패키지 안에 있는 어떤 것을 임포트하면
# 가장 먼저 패키지의 init 파일에 있는 코드가 실행

# 패키지를 임포트할 때 패키지 안에 있는 내용도 함께 임포트하고 싶다면 init 파일을 활용
# import <package>
# 에러를 막기 위해 __init__.py 수정
# from shapes import area, volume

# 모듈 대신 모듈의 함수들을 직접 임포트
# from shapes.area import circle, square

# 패키지에 있는 여러 모듈이 필요로 하는 것들은
# 각 모듈에서 정의하지 않고 패키지 안에서 한 번만 정의
# 똑같은 걸 여러번 정의하는 것은 비효율적
# 실수로 모듈 하나에서 잘못 정의하면 프로그램에 오류가 남
# 여러 모듈에서 필요한 변수, 함수 또는 객체는 패키지의 init 파일에서 정의하는 걸 권장함
PI = 3.14

# import *
# from <module> import * : 모듈의 모든 내용이 임포트
# from <package> import * : 패키지의 모든 내용 임포트 되지 않음
# __all__(특수변수) : import *를 했을 때 임포트 대상에서 어떤 것들을 가져와야 하는지를 정해 주는 변수
# 모듈과 패키지에서 적용할 수 있음.
# 패키지의 __all__ : 패키지에 해당하는 init 파일에서 정의
# from shapes import * : area 모듈과 volume 모듈이 임포트
__all__ = ['area', 'volume']