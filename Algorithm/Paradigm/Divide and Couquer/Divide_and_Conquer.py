# Divide and Conquer : 분할 정복
# 재귀 개념에 대한 이해

# 기존 문제(f(x))를 부분 문제(x1, x2)로 나누어 해결
# Divide : f(x)를 x1, x2로 나눔
# Conquer : f(x1)과 f(x2)의 답 A, B를 찾음
# Combine : A, B를 이용하여 f(x)의 답 S를 찾음

# Conquer 단계, 즉 부분 문제가 크면 부분 문제를 다시 나누어 해결

# 1부터 100까지 더하기
# divide 단계 : 기존 문제를 부분 문제로 나누기
# 1부터 50의 합/51부터 100의 합
# Conquer 단계 : 부분 문제 해결하기
# 1275/3775
# Combine 단계 : 부분 문제의 답을 이용하여 기존 문제 해결하기
# 1275 + 3775 = 5050

# 두 개의 정수 인풋 start와 end를 받고, start부터 end까지의 합을 리턴
def consecutive_sum(start, end):
    # base case        
    if end == start:
        return start

    # 부분 문제를 반으로 나눠주기 위해서 문제의 정중앙을 정의(Divide)
    mid = (start + end) // 2

    # 각 부분 문제를 재귀적으로 풀고(Conquer), 부분 문제의 답을 서로 더함(Combine)
    return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)

# 테스트 코드
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))