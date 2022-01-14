# Memoization
def max_profit_memo(price_list, count, cache):
    # Base Case
    if count < 2:
        cache[count] = price_list[count]
        return cache[count]
    
    # 이미 계산한 값이면 cache에 저장된 값을 리턴
    if count in cache:
        return cache[count]

    # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
    # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정
    # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0
    
    # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, i, cache)
                 + max_profit_memo(price_list, count - i, cache))
    
    # 계산된 최대 수익을 cache에 저장
    cache[count] = profit
    
    return profit

def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)

# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 25))

# Tabulation
def max_profit(price_list, count):
    # 개수별로 가능한 최대 수익을 저장하는 리스트
    # 새꼼달꼼 0개면 0원
    profit_table = [0]
    
    # 개수 1부터 count까지 계산하기 위해 반복문
    for i in range(1, count + 1):
        # profit은 count개를 팔아서 가능한 최대 수익을 저장하는 변수
        # 팔려고 하는 총개수에 대한 가격이 price_list에 없으면 일단 0으로 설정   
        profit = 0
    
        if i < len(price_list):
        # 팔려고 하는 총개수에 대한 가격이 price_list에 있으면 일단 그 가격으로 설정
            profit = price_list[i]
        
        # profit = price_list[i] if i < len(price_list) else 0
    
        # count개를 팔 수 있는 조합들을 비교해서, 가능한 최대 수익을 profit에 저장
        for j in range(1, i // 2 + 1):
            profit = max(profit, profit_table[j] + profit_table[i - j])
    
        profit_table.append(profit)
    
    return profit_table[count]

# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9)) 