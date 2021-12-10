# 1. 리스트(list)

# 여러 개의 값을 한 변수 안에 저장
# 리스트 = [요소0, 요소1, 요소2, ...]
numbers = [2, 3, 5, 7, 11, 13]
names = ['윤수', '혜린', '태호', '영훈']

# 인덱싱(indexing) : 요소의 위치를 인덱스라 부르고 인덱스를 통해 요소를 불러오는 것은 인덱싱
# 인덱스는 0번부터 (리스트의 길이-1)번의 범위로 존재
# 범위를 벗어나는 인덱스를 출력할 경우 에러 발생
# 인덱스를 끝에서부터 나타내는 -로 표현 가능
# [[0],  [1],  [2],  [3],  [4]]
# [[-5], [-4], [-3], [-2], [-1]]
print(names[1])                 # names 리스트의 인덱스 1번 요소 출력
print(numbers[1] + numbers[3])  # numbers 리스트의 인덱스 1번 요소와 3번 요소 더하여 출력
# print(names[7])               # 리스트 범위를 벗어나는 인덱스는 에러 발생
print(names[-1])                # names 리스트의 마지막 요소 출력

# 리스트 슬라이싱(list slicing) : 리스트의 일부를 가져오는 것
# 리스트[처음 인덱스:마지막 인덱스-1]
print(numbers[0:4])     # numbers 리스트의 인덱스 0부터 3까지 출력
print(numbers[:3])      # numbers 리스트의 인덱스 처음부터 2까지 출력
new_list =numbers[2:5]  # 슬라이싱한 리스트를 새로운 변수로 저장 가능

# 인덱싱으로 리스트값 변경하기
numbers[0] = 7              # numbers리스트는 [7, 3, 5, 7, 11, 13]로 바뀜
numbers[0] += numbers[1]    # numbers리스트는 [10, 3, 5, 7, 11, 13]로 바뀜

# 2. 리스트 함수

numbers = [1, 3, 5, 7]
# len : 리스트의 요소 개수를 나타내는 함수
print(len(numbers)) # numbers의 요소 개수인 4 출력

# append : 리스트 마지막 인덱스에 요소를 추가해주는 함수
numbers.append(5)
print(numbers)      # numbers는 [1, 3, 5, 7, 5]로 변경

# del : 리스트 요소를 삭제해주는 함수
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
del numbers[3]      # numbers의 3번 인덱스인 7 삭제 numbers는 [2, 3, 5, 11, 13, 17, 19]로 변경

# insert(인덱스, 값) : 값을 원하는 인덱스에 삽입해주는 함수
numbers = [2, 3, 5, 7, 11, 13, 17, 19]
numbers.insert(4, 37)   # numbers는 [2, 3, 5, 7, 37, 11, 13, 17, 19]로 변경

# reverse : 리스트의 요소들을 뒤집어진 순서로 배치해주는 함수
numbers = [5, 3, 7, 1]
numbers.reverse()
print(numbers)          # [1, 7, 3, 5]

# index : 값을 갖고 있는 원소의 인덱스를 리턴
members = ["영훈", "윤수", "태호", "혜린"]
print(members.index("윤수"))    # 1
print(members.index("태호"))    # 2

# remove : 첫 번째로 값을 갖고 있는 원소를 삭제
fruits = ["딸기", "당근", "파인애플", "수박", "참외", "메론", "파인애플"]
fruits.remove("파인애플")
print(fruits)       # ['딸기', '당근', '수박', '참외', '메론', '파인애플']

# 3. 리스트 정렬

numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# sorted : 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
# 기존 리스트에 영향을 주지 않기 때문에 새로운 변수로 저장하여 사용
new_list = sorted(numbers)
print(numbers)          # 기존 리스트에 영향을 주지 않기 때문에 [19, 13, 2, 5, 3, 11, 7, 17] 출력
print(sorted(numbers))  # 오름차순으로 정렬된 [2, 3, 5, 7, 11, 13, 17, 19] 출력
print(new_list)         # 오름차순으로 정렬된 [2, 3, 5, 7, 11, 13, 17, 19] 출력
# reverse=True 옵션을 줘 내림차순으로 정렬할 수 있음
new_list = sorted(numbers, reverse=True)
print(new_list)         # 내림차순으로 정렬된 [19, 17, 13, 11, 7, 5, 3, 2] 출력

# sort : 아무것도 리턴하지 않고, 기존 리스트를 정렬
numbers.sort()
print(numbers.sort())   # 아무것도 리턴하지 않기 때문에 None 출력
print(numbers)          # 오름차순으로 정렬된 [2, 3, 5, 7, 11, 13, 17, 19] 출력
# reverse=True 옵션을 줘 내림차순으로 정렬할 수 있음
numbers.sort(reverse=True)
print(numbers)          # 내림차순으로 정렬된 [19, 17, 13, 11, 7, 5, 3, 2] 출력

# 4. 리스트에서 값의 존재 확인하기

# value가 some_list의 요소인지 확인
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        # some_list에서 value를 찾으면 True를 리턴
        if some_list[i] == value:
            return True
        i = i + 1

    # 만약 some_list에서 value를 발견하지 못했으면 False를 리턴
    return False

# 테스트
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))   # True
print(in_list(primes, 12))  # False

# 내장함수 in을 써서 판별 가능
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 in primes)  # True
print(12 in primes) # False

# 값이 없는 걸 확인하려면 not in 사용
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(7 not in primes)  # False
print(12 not in primes) # True

# 5. 리스트 안의 리스트 (Nested List)

# 세 번의 시험을 보는 수업
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]

# 첫 번째 학생의 성적
print(grades[0])    # [62, 75, 77]

# 세 번째 학생의 성적
print(grades[2])    # [85, 91, 89]

# 첫 번째 학생의 첫 번째 시험 성적
print(grades[0][0]) # 62

# 세 번째 학생의 두 번째 시험 성적
print(grades[2][1]) # 91

# 첫 번째 시험의 평균
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3) # 75.0

# 실습과제
# 리스트 인덱싱 연습

# while문과 greetings 리스트의 원소를 모두 출력하는 프로그램 작성
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

i = 0

while i < len(greetings):
    print(greetings[i])
    i += 1

# 실습과제
# 온도 단위 바꾸기

# 화씨 온도를 섭씨 온도로 변환해 주는 함수 fahrenheit_to_celsius 만들기
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: {}".format(temperature_list))  # 화씨 온도 출력

i = 0
while i < len(temperature_list):
    temperature_list[i] = round(fahrenheit_to_celsius(temperature_list[i]), 1)
    i += 1

print("섭씨 온도 리스트: {}".format(temperature_list))  # 섭씨 온도 출력

# 리스트를 반환하는 함수 fahrenheit_to_celsius 만들기
def fahrenheit_to_celsius(fahrenheit):
    celsius = []
    i = 0
    while i < len(fahrenheit):
        celsius.append(round((fahrenheit[i] - 32) * 5 / 9, 1))
        i += 1
    return celsius

temperature_list = [40, 15, 32, 64, -4, 11]
print(f"화씨 온도 리스트: {temperature_list}")  # 화씨 온도 출력
print(f"섭씨 온도 리스트: {fahrenheit_to_celsius(temperature_list)}")  # 섭씨 온도 출력

# 실습과제
# 환전 서비스

# 한국 원화를 미국 달러로 변환해 주는 krw_to_usd 함수, 미국 달러를 일본 엔화로 변환해 주는 usd_to_jpy 함수 만들기
def krw_to_usd(krw):
    usd = round(krw / 1000, 1)
    return usd

def usd_to_jpy(usd):
    jpy = usd / 8 * 1000
    return jpy

prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(prices))
 
i = 0
while i < len(prices):
    prices[i] = krw_to_usd(prices[i])
    i += 1

print("미국 화폐: " + str(prices))

i = 0
while i < len(prices):
    prices[i] = usd_to_jpy(prices[i])
    i += 1

print("일본 화폐: " + str(prices))

# 리스트를 반환하는 함수 krw_to_usd, usd_to_jpy 만들기
def krw_to_usd(krw):
    usd_prices = []
    i = 0
    while i < len(krw):
        usd_prices.append(round(krw[i] / 1000, 1))
        i += 1
    return usd_prices

def usd_to_jpy(usd):
    jpy_prices = []
    i = 0
    while i < len(usd):
        jpy_prices.append(round(usd[i] / 8 * 1000))
        i += 1
    return jpy_prices

prices = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]

print("한국 화폐: " + str(prices))

print("미국 화폐: " + str(krw_to_usd(prices)))

print("일본 화폐: " + str(usd_to_jpy(krw_to_usd(prices))))

# 실습과제
# 리스트 함수 활용하기

# numbers라는 빈 리스트를 만들고 리스트를 출력한다.
# append를 이용해서 numbers에 1, 7, 3, 6, 5, 2, 13, 14를 순서대로 추가한다. 그 후 리스트를 출력한다.
# numbers 리스트의 원소들 중 홀수는 모두 제거한다. 그 후 다시 리스트를 출력한다.
# numbers 리스트의 인덱스 0 자리에 20이라는 수를 삽입한 후 출력한다.
# numbers 리스트를 정렬한 후 출력한다.

# 빈 리스트 만들기
numbers = []
print(numbers)

# numbers에 값들 추가
numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
# numbers.extend([1, 7, 3, 6, 5, 2, 13, 14]) append 대신 extend로 한꺼번에 추가 가능
print(numbers)

# numbers에서 홀수 제거
i = len(numbers) - 1
while i >= 0:
    if numbers[i] % 2 != 0:
        del numbers[i]
    i -= 1
print(numbers)
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 1:
#         del numbers[i]
#     else:
#         i += 1
# print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
numbers.insert(0, 20)
print(numbers)

# numbers를 정렬해서 출력
numbers.sort()
print(numbers)