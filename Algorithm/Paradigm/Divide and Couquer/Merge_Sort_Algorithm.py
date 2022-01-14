# 합병 정렬(Merge Sort) 알고리즘
# Divide and Divide 방식으로 수행
# Combine 단계가 복잡함

# Divide : 리스트를 반으로 나눔
# Divide : 왼쪽 리스트와 오른쪽 리스트를 각각 정렬
# Combine : 정렬된 두 리스트를 하나의 정렬된 리스트로 합병

def merge(list1, list2):
    # 정렬된 항목들을 담을 리스트
    sorted_list = []
    
    i = 0
    j = 0
    
    # list1과 list2를 돌면서 sorted_list에 추가
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            sorted_list.append(list2[j])
            j += 1
        else:
            sorted_list.append(list1[i])
            i += 1
    
    # list1과 list2에 남은 항목이 있으면 정렬 리스트에 추가
    # list1[i:]와 list2[j:] 둘 중 하나는 빈 리스트임
    sorted_list += list1[i:] + list2[j:]
                
    return sorted_list

    # list2에 남은 항목이 있으면 정렬 리스트에 추가
    # if i == len(list1):
    #     sorted_list += list2[j:]

    # list1에 남은 항목이 있으면 정렬 리스트에 추가
    # elif j == len(list2):
    #     sorted_list += list1[i:]

    # return sorted_list
    
def merge_sort(my_list):
    # base case
    if len(my_list) < 2:
        return my_list
    
    # my_list를 반씩 나눔(divide)
    mid_idx = len(my_list) // 2
    left_list = my_list[:mid_idx]
    right_list = my_list[mid_idx:]
    
    # merge_sort 함수를 재귀적으로 호출하여 부분 문제 해결(conquer)하고,
    # merge 함수로 정렬된 두 리스트를 합쳐(combine)줌
    return  merge(merge_sort(left_list), merge_sort(right_list))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))