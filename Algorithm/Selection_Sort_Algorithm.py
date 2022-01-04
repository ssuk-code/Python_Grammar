# 선택 정렬을 위한 파이썬 프로그램

# 정렬 : 원소들을 특정 순서로 정리하는 것
# 선택 정렬(Selection Sort) 알고리즘
# 가장 먼저 생각이 날 수 있는 자연스러운 정렬 알고리즘
# 모든 요소들을 비교하면서 제일 작은 값부터 정렬시키기

# 선택 정렬을 수행하는 함수
def selectionSort(Arr):
    # 모든 리스트 요소 탐색
    for i in range(len(Arr)):
        
        # 남아있는 제일 작은 요소 찾기
        min_idx = i
        for j in range(i + 1, len(Arr)):
            if Arr[min_idx] > Arr [j]:
                min_idx = j
            
        #발견된 제일 작은 요소와 위치 바꿔주기
        Arr[i], Arr[min_idx] = Arr[min_idx], Arr[i]
        
    return Arr
        
# 테스트 코드
print ("Sorted array")
print(selectionSort([6, 2, 5, 20, 1]))