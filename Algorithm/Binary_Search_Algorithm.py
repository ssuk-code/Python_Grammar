# ‘이진 탐색(Binary Search)’ 알고리즘
# 1회 비교를 거칠 때마다 탐색 범위가 (대략) 절반으로 줄어들어 탐색을 진행하는 알고리즘
# 선형탐색 알고리즘과 달리, 정렬된 리스트를 전제로 함

# 범위를 반으로 줄여가며 some_list에서 element를 찾는 함수
def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    # 중간 인덱스의 값과 element 비교하기
    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        # middle_index의 값과 element가 같다면 middle_index 리턴
        if some_list[middle_index] == element:
            return middle_index
        # middle_index의 값이 element보더 크다면 end_index 범위를 middle_index만큼 줄임
        elif element < some_list[middle_index]:
            end_index = middle_index - 1
        # middle_index의 값이 element보더 작다면 start_index 범위를 middle_index만큼 줄임
        else:
            start_index = middle_index + 1
    
    #  while문을 통과하면 element와 some_list 요소 불일치      
    return None

# 테스트 코드
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))