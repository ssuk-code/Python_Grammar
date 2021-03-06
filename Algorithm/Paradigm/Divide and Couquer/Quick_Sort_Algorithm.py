# 퀵 정렬(Quick) Sort) 알고리즘
# Divide and Conquer 방식으로 수행
# divide 단계가 복잡함
# 장점 : extra memory가 필요 없고 평균적으로 mergesort보다 빠름
# 단점 : pivot이 리스트의 최대값/최소값인 경우 시간복잡도가 O(n^2)까지 늘어남
# Divide : pivot을 기준으로 작은 값 큰 값 옮기기
# Conquer : 작은 값, 큰 값에서 순서대로 정렬하기
# Combine : 없음

# pivot을 정함
# pivot을 기준으로 값들을 새롭게 배치함

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 리스트 값 확인과 기준점 이하 값들의 위치 확인을 위한 변수 정의
    i = start
    b = start
    pivot = end
    
    # 범위안의 모든 값들을 볼 때까지 반복문 수행
    while i < pivot:
    # i 인덱스의 값이 기준점보다 작으면 i와 b 인덱스에 있는 값들을 교환하고 b를 1 증가
        if my_list[i] <= my_list[pivot]:
            swap_elements(my_list, i, b)
            b += 1
        i += 1
        
    # b와 기준점인 p 인덱스에 있는 값 바꾸기
    swap_elements(my_list, b, pivot)
    pivot = b
    
    # pivot의 최종 인덱스를 리턴
    return pivot

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)

# 퀵 정렬
def quicksort(my_list, start, end):
    # base case
    if end - start < 1:
        return # return None과 같은 효과
    
    # pivot을 기준으로 작은 값과 큰 값 정렬하기
    pivot = partition(my_list, start, end)
    
    # pivot의 왼쪽 부분 정렬
    quicksort(my_list, start, pivot -1)
   
    # pivot의 오른쪽 부분 정렬
    quicksort(my_list, pivot + 1, end)

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)

# 옵셔널 파라미터 : start와 end를 따로 설정하지 않았으니 기본값인 0과 None이 지정됨
# 퀵 정렬
def quicksort(my_list, start = 0, end = None):
    if end == None:
        end = len(my_list) - 1
    
    # base case
    if end - start < 1:
        return # return None과 같은 효과
    
    # pivot을 기준으로 작은 값과 큰 값 정렬하기
    pivot = partition(my_list, start, end)
    
    # pivot의 왼쪽 부분 정렬
    quicksort(my_list, start, pivot -1)
   
    # pivot의 오른쪽 부분 정렬
    quicksort(my_list, pivot + 1, end)

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)