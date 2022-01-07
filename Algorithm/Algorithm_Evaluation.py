# 시간 : 시간을 적게 쓰는 프로그램(문제를 빨리 해결하는 프로그램)
# 컴퓨터 사양, 프로그래밍 언어에 따라 문제 해결 시간이 다르기 때문에
# 프로그램이 돌아가는 시간으로 알고리즘 비교하는 것은 비합리적

# 시간 복잡도(Time Complexity) : 인풋 크기에 비례하는 알고리즘의 실행 시간
# 시간 복잡도가 작을수록 더 빠른 알고리즘

# 거듭제곱과 로그 알아두기
# 거듭제곱
# a^b = c
# 로그
# loga(c) = b

# 1부터 n까지의 값
# T = 1 + 2 + 3 + ... + n
# T = n + ... + 3 + 2 + 1
# 2T = n * (n + 1)
# T = n * (n + 1) / 2

# 점근 표기법(Big-O Notation)
# 소요시간에서 n의 영향력이 가장 큰 항만 O에 넘겨줌
# 절대적인 시간이 아닌 성장성을 봄
# 알고리즘 소요시간 -> 점근 표기법
# 20n + 40          -> O(n)
# 2n^2 + 8n +157    -> O(n^2)
# 5n^3 + 100n^2 + 75-> O(n^3)
# 20lg n + 60       -> O(lg n)
# n이 별로 크지 않으면, 알고리즘에 영향을 크게 받지 않음
# n이 엄청 큰 경우, 알고리즘이 중요해짐

# 점근 표기법의 의미
# O(1) : 인풋 데이터의 상관 없이 시간이 일정함(알고리즘 소요시간이 상수인 경우)
# O(n) : 인풋 데이터의 수가 늘어난 만큼 소요시간이 증가. 100 -> 1초 1000 -> 10초
# O(n^2) : 인풋 데이터의 수가 늘어난 제곱배만큼 소요시간 증가. 100개 -> 1초 1000개(10배 증가) -> 100초(10의 제곱)
# O(n^3) : 인풋 데이터의 수가 늘어난 세제곱배만큼 소요시간 증가. 100개 -> 1초 1000개(10배 증가) -> 1000초(10의 세제곱)

# 탐색 알고리즘 평가하기
# 보수적인 방법에 따라 최악의 경우로 시간복잡도 평가

# 선형 알고리즘의 시간복잡도 : O(n)
# 최고의 경우(한 번에 찾기) : O(1) + O(1) + O(1) + O(1) = O(4) => O(1)
# 최악의 경우(리스트 모두 탐색) : O(1) + O(1) + O(n) + O(1) = O(n + 3) => O(n)
def linear_search(element, some_list):
    i = 0                   # O(1)
    n = len(some_list)      # O(1)
    
    # 반복 횟수(n) -> O(n)
    while i < n:
        if some_list[i] == element:
            return i
        i += 1 

    return -1               # O(1)

# 이진 탐색 알고리즘의 시간복잡도 : O(lg n)
# 최고의 경우(한 번에 찾기) : O(1) + O(1) + O(1) + O(1) = O(4) => O(1)
# 최악의 경우(리스트 모두 탐색) : O(1) + O(1) + O(lg n) + O(1) = O(lg n + 3) => O(lg n)
def binary_search(element, some_list):
    start_index = 0                                     # O(1)
    end_index = len(some_list) - 1                      # O(1)
    
    # 반복하면 반으로 줄음 -> O(lg n)
    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        if some_list[middle_index] == element:
            return middle_index
        elif element < some_list[middle_index]:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1
    
    return None                                         # O(1)

# 점근 표기법에서의 n
# 리스트와 같은 선형적인 인풋 크기를 나타내는 문자

# 그래프가 인풋될 때의 BFS 알고리즘의 시간 복잡도
# 꼭짓점('V'ertex)의 개수와 변('E'dge)의 개수를 사용하여 O(V+E)로 표현

# List Operations
# 리스트의 길이가 n일 때
# Operation             Code                            Average Case
# ---------------------------------------------------------------
# 인덱싱                my_list[index]                  O(1)
# ---------------------------------------------------------------
# 정렬                  my_list.sort()                  O(n lg n)
#                       sorted(my_list)
# ---------------------------------------------------------------
# 뒤집기                my_list.reverse()               O(n)
# ---------------------------------------------------------------
# 탐색                  element in my_list	            O(n)
# ---------------------------------------------------------------
# 끝에 요소 추가        my_list.append(element)	        O(1)
# ---------------------------------------------------------------
# 중간에 요소 추가      my_list.insert(index, element)  O(n)
# ---------------------------------------------------------------
# 삭제                  del my_list[index]	            O(n)
# ---------------------------------------------------------------
# 최솟값, 최댓값 찾기   min(my_list)                    O(n)
#                       max(my_list)
# ---------------------------------------------------------------
# 길이 구하기           len(my_list)	                O(1)
# ---------------------------------------------------------------
# 슬라이싱              my_list[a:b]                    O(b - a)

# Dictionary Operations
# Operation             Cod                     Average Case
# ---------------------------------------------------------------
# 값 찾기               my_dict[key]            O(1)
# ---------------------------------------------------------------
# 값 넣어주기/덮어쓰기  my_dict[key] = value    O(1)
# ---------------------------------------------------------------
# 값 삭제               del my_list[key]        O(1)

# 주요 시간 복잡도 총정리

# 알고리즘의 시간 복잡도
# O(1), O(lg n), O(n), O(n lg n), O(n^2), O(n^3), O(n^4), O(2^n), O(n!)
# O(1), O(lg n), O(n), O(n lg n), O(n^2), O(n^3)가 많이 사용됨

# O(1) : 인풋의 크기가 소요 시간에 영향이 없음
# O(1)함수
def print_first(my_list):
    print(my_list[0]) 

print_first([2, 3])
print_first([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53])
# 반복문이 없으면 대체로 O(1)

# O(n) : 일반적으로 반복문이 있고, 반복되는 횟수가 인풋의 크기와 비례
# O(n) 함수
def print_each(my_list):
    for i in range(len(my_list)):
        print(my_list[i])
# n/2번 반복 : O(1/2n) -> O(n)
def print_half(my_list):
    for i in range(len(my_list) // 2):
        print(my_list[i])
# O(3n) -> O(n)
def print_three_times(my_list):
    for i in range(len(my_list)):
        print(my_list[i])

    for i in range(len(my_list)):
        print(my_list[i])

    for i in range(len(my_list)):
        print(my_list[i])

# O(n^2) : 인풋의 크기에 비례하는 반복문 안에 반복문이 있는 경우
# O(n^2) 함수
def print_pairs(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            print(my_list[i], my_list[j])

# O(n^3) : 인풋의 크기에 비례하는 반복문이 세 번 중첩
# O(n^3) 함수
def print_triplets(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            for k in range(len(my_list)):
                print(my_list[i], my_list[j], my_list[k])

# O(lg n) : 문제를 해결하는데 필요한 단계들이 연산마다 특정 요인에 의해 줄어듦
# O(lg n) 함수
# 2의 거듭제곱을 출력하는 함수
# (이번에는 인풋이 리스트가 아니라 정수)
# 인풋 n이 128이면 i가 1일 때부터 2, 4, 8, 16, 32, 64까지 총 7번 실행(lg128 = 7)
def print_powers_of_two(n):
    i = 1
    while i < n:
        print(i)
        i = i * 2
# n가 128일 때부터 64, 32, 16, 8, 4, 2까지 반복문이 7번 실행(lg128 = 7)
def print_powers_of_two(n):
    i = n
    while i > 1:
        print(i)
        i = i / 2

# O(n lg n) : O(n)과 O(lg n)이 겹쳐진 것
# 데이터의 수가 2배로 늘 때, 연산횟수는 2배 조금 넘게 증가
def print_powers_of_two_repeatedly(n):
    for i in range(n):      # 반복횟수: n에 비례
        j = 1
        while j < n:        # 반복횟수: lg n에 비례
            print(i, j)
            j = j * 2
def print_powers_of_two_repeatedly(n):
    i = 1
    while i < n:            # 반복횟수: lg n에 비례
        for j in range(n):  # 반복횟수: n에 비례
            print(i, j)
        i = i * 2

# 유용한 파이썬 기능의 시간 복잡도
# type : O(1)
print(type([7, 5, 2, 3, 6])) # => <class 'list'>
print(type(5))               # => <class 'int'>
print(type(3.14))            # => <class 'float'>
print(type(True))            # => <class 'bool'>
print(type("True"))          # => <class 'str'>
# max, min : O(n)
print(max(2, 5))             # => 5
print(max(2, 7, 5))          # => 7
print(min(2, 5))             # => 2
print(min(2, 7, 5, 11, 6))   # => 2
# str : O(lg n) -> 파라미터가 n, O(d) -> 파라미터가 n이고 자리수가 d
my_str = str(257138)
print(my_str)                # => 257138
print(type(my_str))          # => <class 'str'>
# append : O(1)
# insert, del, index, reverse : O(n)
my_list = [7, 5, 2, 3, 6]

my_list.append(9)            # 끝에 9 추가
print(my_list)               # => [7, 5, 2, 3, 6, 9]

my_list.insert(2, 11)        # 2번 인덱스에 11 추가
print(my_list)               # => [7, 5, 11, 2, 3, 6, 9]

del my_list[2]               # 2번 인덱스 값 삭제
print(my_list)               # => [7, 5, 2, 3, 6, 9]

my_index = my_list.index(9)  # 리스트에서 9의 인덱스
print(my_index)              # => 5

my_list.reverse()            # 리스트 뒤집기
print(my_list)               # => [9, 6, 3, 2, 5, 7]
# sort, sorted : O(n lg n)
my_list = [7, 5, 2, 3, 6]

print(sorted(my_list))       # => [2, 3, 5, 6, 7]
print(my_list)               # => [7, 5, 2, 3, 6]

my_list.sort()
print(my_list)               # => [2, 3, 5, 6, 7]
# slicing : O(b - a)
my_list = [7, 5, 2, 3, 6]

print(my_list[1:4])          # => [5, 2, 3]
print(my_list[:4])           # => [7, 5, 2, 3]
print(my_list[1:])           # => [5, 2, 3, 6]
print(my_list[:])            # => [7, 5, 2, 3, 6]
print(my_list[::2])          # => [7, 2, 6]
# len : O(1)
my_list = [7, 5, 2, 3, 6]
my_dict = {'a': 2, 'b': 3, 'c': 5, 'd': 7}
my_string = 'hello world'

print(len(my_list))          # => 5
print(len(my_dict))          # => 4
print(len(my_string))        # => 11

# 공간(컴퓨터의 저장공간, 메모리) : 메모리를 적게 쓰는 프로그램
# 공간 복잡도(Space Complexity) : 인풋 크기에 비례해서 알고리즘이 사용하는 메모리 공간
# 공간 복잡도도 점근 표기법으로 표현할 수 있기 때문에 간편하게 Big-O 표기법을 사용

# O(1)
# result가 차지하는 메모리 공간은 인풋과 무관
def product(a, b, c):
    result = a * b * c
    return result

# O(n)
# every_other가 차지하는 공간에 n/2번개의 값이 들어감 : O(1/2n) -> O(n)
def get_every_other(my_list):
    every_other = my_list[::2]
    return every_other

# O(n^2)
# products에는 my_list에서 가능한 모든 조합의 곱(n^2)이 들어감 -> O(n^2)
def largest_product(my_list):
    products = []
    for a in my_list:
        for b in my_list:
            products.append(a * b)
    
    return max(products)