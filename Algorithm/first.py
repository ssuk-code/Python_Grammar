# 알고리즘 전 기본적인 파이썬 지식 테스트
# 필란드롬 : "토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어
# *for문을 사용할 것
# *append,  insert 메소드와 del 함수 사용하지 말것

# 필란드롬인지 확인해주는 함수 
def is_palindrome(word):
    # for i in range(len(word)):
    #     if word[::-1] == word:
    #         return True
    #     else:
    #         return False

    # for left in range(len(word) // 2):
    #     # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
    #     right = len(word) - left - 1
    #     if word[left] != word[right]:
    #         return False

    # # for문에서 나왔다면 모든 쌍이 일치
    # return True
    
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
            
    return True
        

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))