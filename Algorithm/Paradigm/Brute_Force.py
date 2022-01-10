# Brute Force Attack : 무차별 대입 공격
# 가장 순진한 알고리즘 접근법
# 직관적이고 명확함
# 답을 확실하게 찾을 수 있음
# 비효율적인 알고리즘임 -> 인풋이 크면 사용할 수 없음
# Brute Force를 쓰는 이유는 알고리즘의 첫 시작임

# 카드 뭉치 최대 조합
# 시간 복잡도 -> O(mn) 들어오는 카드의 수가 다를 수 있어 n^2 대신 mn을 씀
# max_product는 left_cards에서 카드 하나와 right_cards에서 카드 하나를 뽑아서 곱했을 때 그 값이 최대가 되는 값을 리턴
def max_product(left_cards, right_cards):
    # 현재까지 최댓값을 담기 위한 변수
    # 처음에는 임시로 각 리스트의 첫 번째 요소의 곱으로 설정
    max_combi = left_cards[0] * right_cards[0]

    # 가능한 모든 조합을 보기 위한 중첩 반복문
    for left in left_cards:
        for right in right_cards:
            # 현재까지의 최댓값 값과 지금 보고 있는 곱을 비교해서 더 큰 값을 최댓값 변수에 저장
            max_combi = max(max_combi, left * right)

    # 찾은 최댓값을 리턴한다  
    return max_combi

# 테스트 코드
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))

# 가까운 매장 찾기
# 시간 복잡도 -> O(n^2)
# 두 매장의 직선 거리를 계산해 주는 함수
# 피타고라스 공식을 이용한 거리 구하기
def distance(tup1, tup2):
    x_distance = tup2[0] - tup1[0]
    y_distance = tup2[1] - tup1[1]
    
    # # 제곱근 사용을 위한 sqrt 함수 불러오기
    # from math import sqrt
    # return sqrt((x_distance) ** 2 + (y_distance) ** 2)
    
    # 제곱근 반환(n제곱근은 ** (1/n))
    return ((x_distance) ** 2 + (y_distance) ** 2) ** (1/2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(test_coordinates):
    # 현재까지 본 가장 가까운 두 매장
    closest = [test_coordinates[0], test_coordinates[1]]
    
    for i in range(len(test_coordinates) - 1):
        for j in range(i + 1, len(test_coordinates)):
            store1, store2 = test_coordinates[i], test_coordinates[j]
            
            # 더 가까운 두 매장을 찾으면 closest 업데이트
            if distance(closest[0], closest[1]) > distance(store1, store2):
                closest = [store1, store2]

    return closest

# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))

# 강남역 폭우
# 시간 복잡도 -> O(n^2)
def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    count = 0
    
    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치
        max_left = max(buildings[:i])
        max_rigth = max(buildings[i:])
        
        # 현재 인덱스에 빗물이 담길 수 있는 높이
        higher = min(max_left, max_rigth)
        
        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 higher가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        count += max(0, higher - buildings[i])
            
    return count

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))