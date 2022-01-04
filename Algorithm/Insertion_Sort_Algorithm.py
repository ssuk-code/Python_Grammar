# 삽입 정렬을 위한 파이썬 프로그램

# 삽입 정렬(Insertion Sort) 알고리즘
# 각 값이 어디 들어갈지 찾는 알고리즘
# 값끼리 비교하여 위치에 넣기

# 삽입 정렬을 수행하는 함수
def insertionSort(arr):
    for i in range(1, len(arr)):
        
        key = arr[i]
        
        # key보다 큰 arr[j]의 위치를 arr[j+1]로 옮기기
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
    return arr
        
# 테스트 코드
print ("Sorted array")
print(insertionSort([6, 2, 5, 20, 1]))