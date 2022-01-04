# '선형 탐색(Linear Search)' 알고리즘
# 리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘

# 리스트 요소와 비교하여 element 위치 찾는 함수
def linear_search(element, some_list):
    
    # 리스트 요소 처음부터 끝까지 비교
    # element를 some_list에서 발견할 시 그 위치(인덱스)를 리턴
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
    
    # for문을 통과하면 element와 some_list 요소 불일치
    return None

# 테스트 코드
print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))