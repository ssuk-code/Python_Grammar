# 리스트 뒤집기
# 시간복잡도 -> O(n)
# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    if len(some_list) < 2:
        return some_list
    return some_list[-1:] + flip(some_list[:-1])

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

# 재귀 함수 -> 반복문
def flip(some_list):
    reversed_list = []
    for i in range(-1, -len(some_list) - 1, -1):
        reversed_list.append(some_list[i])
    return reversed_list