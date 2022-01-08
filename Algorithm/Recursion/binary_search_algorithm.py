# 이진 탐색 재귀로 구현해보기
# 시간복잡도 -> O(lg n)
def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1
    
    # base case: start_index가 end_index보다 크면 some_list안에 element는 없음
    if start_index > end_index:
        return None
    
    # 범위의 중간 인덱스
    middle_index = (start_index + end_index) // 2
    
    # base case: 이 인덱스의 값이 찾는 값인지 확인
    if element == some_list[middle_index]:
        return middle_index
    
    # 찾는 항목이 중간 값보다 크면 리스트 오른쪽을 탐색
    elif element > some_list[middle_index]:
        return binary_search(element, some_list, middle_index + 1, end_index)
    
    # 찾는 항목이 중간 값보다 작으면 리스트 왼쪽을 탐색
    else:
        return binary_search(element, some_list, start_index, middle_index - 1)

# 테스트 코드
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))