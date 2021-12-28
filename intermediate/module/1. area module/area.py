print('area 모듈 이름 : {}'.format(__name__))

# 변하지 않는 값들은 상수로 처리하여 사용
PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length


# if __name__ == '__main__':
# 파일이 직접 실행되냐 아니면 임포트되냐에 따라서 코드의 흐름을 제어
# area 파일을 직접 실행시키면 파일의 __name__은 __main__이 되기 때문에 코드가 실행됨
# area 파일을 임포트하면 __name__은 area가 되기 때문에 조건문 안에 있는 코드가 실행되지 않음
if __name__ == '__main__':
    # circle 함수 테스트
    print(circle(2) == 12.56)
    print(circle(5) == 78.5)

    # square 함수 테스트
    print(square(2) == 4)
    print(square(5) == 25)

# 코드의 가독성을 높이는 법
# main함수가 요구되지 않더라도 if __name__ == '__main__'과 main() 사용을 권장
# 함수들을 테스팅 하는 메인 함수
def main():
      # circle 함수 테스트
      print(circle(2) == 12.56)
      print(circle(5) == 78.4)

      # square 함수 테스트
      print(square(2) == 4)
      print(square(5) == 25)

if __name__ == '__main__':
    main()