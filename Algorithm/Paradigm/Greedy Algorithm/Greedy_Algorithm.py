# Greedy Algorithm
# 장점 : 간단하고 빠름
# 단점 : 완벽한 정답이 보장되지 않음
# 다른 알고리즘의 속도가 너무 느린 경우 사용
# 최적의 답이 필요없을 때 사용

# 최적의 답을 구해주는 경우의 Greedy Algorithm
# 1. 최적 부분 구조(Optimal Substructure)
# 부분 문제들의 최적의 답을 이용해서 기존 문제의 최적의 답을 구할 수 있다는 것
# 2. 탐욕적 선택 속성(Greedy Choice Property)
# 각 단계에서의 탐욕스런 선택이 최종 답을 구하기 위한 최적의 선택

# 최적 부분 구조가 있고, 탐욕적 선택 속성이 있다면
# Greedy Algorithm이 최적의 솔루션 보장

# 최소 동전으로 돈을 거슬러 주는 함수를 Greedy Algorithm으로 구현
def min_coin_count(value, coin_list):
    # coin_list.sort(reverse=True)
    # coin = 0
    # for i in range(len(coin_list)):
    #     if value // coin_list[i] != 0:
    #         coin += value // coin_list[i]
    #         value -= value // coin_list[i] * coin_list[i]
    # return coin
    
    # 누적 동전 개수
    count = 0
    
    # coin_list의 값들을 큰 순서대로 보기
    for coin in sorted(coin_list, reverse=True):
        # 현재 동전으로 몇 개 거슬러 줄 수 있는지 확인
        count += (value // coin)
        
        # 잔액 계산
        value %= coin
        
    return count

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))