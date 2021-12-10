# 1. 리스트와 문자열

# 리스트와 문자열은 구조적으로 비슷함
# 비슷한 점
# 인덱싱
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabet_list[0])     # 'A'
print(alphabet_list[1])     # 'B'
print(alphabet_list[4])     # 'E'
print(alphabet_list[-1])    # 'J'

alphabet_str = 'ABCDEFGHIJ'
print(alphabet_str[0])  # 'A'
print(alphabet_str[1])  # 'B'
print(alphabet_str[4])  # 'E'
print(alphabet_str[-1]) # 'J'

# for 반복문
# 알파벳 리스트의 반복문
alphabets_list = ['A', 'B', 'C', 'D', 'E', 'F']
for alphabet in alphabets_list:
    print(alphabet)

# 알파벳 문자열의 반복문
alphabets_string = 'ABCDEF'
for alphabet in alphabets_string:
    print(alphabet)

# 슬라이싱
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabet_list[0:5])   # ['A', 'B', 'C', 'D', 'E']
print(alphabet_list[4:])    # ['E', 'F', 'G', 'H', 'I', 'J']
print(alphabet_list[:4])    # ['A', 'B', 'C', 'D']

alphabet_str = 'ABCDEFGHIJ'
print(alphabet_str[0:5])    # 'ABCDE'
print(alphabet_str[4:])     # 'EFGHIJ'
print(alphabet_str[:4])     # 'ABCD'

# 덧셈 연산 : "연결"
str_1 = 'Hello'
str_2 = "World"
str_3 = str_1 + str_2
print(str_3)    # 'HelloWorld'

list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = list_1 + list_2
print(list_3)   # [1, 2, 3, 4, 5, 6, 7, 8]

# len
my_list = [2, 3, 5, 7, 11]
print(len(my_list)) # 5

my_str = 'Hello world!'
print(len(my_str))  # 12

# 차이점
# Mutable (수정 가능) vs. Immutable (수정 불가능)
numbers = [1, 2, 3, 4]
numbers[0] = 5
print(numbers)  # [5, 2, 3, 4]

# 문자열은 리스트와 달리 수정할 수 없음
# name = 'my_name'
# name[0] = 'M' # 오류 생김
# print(name)

# 실습과제
# 자릿수 합 구하기

# 함수 sum_digit은 파라미터로 정수형 num을 받고, num의 각 자릿수를 더한 값을 리턴
# 자리수 합 리턴
def sum_digit(num):
    str_num = str(num)
    sum = 0
    for i in str_num:
        sum += int(i)
    return sum

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
sum = 0
for i in range(1, 1001):
    sum += sum_digit(i)

print(sum)

# 실습과제
# 주민등록번호 가리기

# 마지막 네 글자가 '*'로 대체
def mask_security_number(security_number):
    return security_number[:-4] + '****'

# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))

# 실습과제
# 팰린드롬

# 거꾸로 읽어도 똑같은 단어인 팰린드롬 여부를 확인하는 함수 is_palindrome을 작성
# 마지막 네 글자가 '*'로 대체
# def is_palindrome(word):
#     return word == word[::-1]

def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))