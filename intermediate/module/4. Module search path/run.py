# 파이썬은 임포트하려는 모듈을 찾기 위해서 sys.path 리스트에 있는 경로를 탐색함
import sys

print(sys.path)

# 새로운 경로를 sys.path에 추가하는 법
# append를 이용한 경로 추가는 프로그램이 종료되면 사라짐
sys.path.append('C:\\Users\\distn\\Desktop')    # Windows
# sys.path.append('/Users/distn/Desktop') # macOS