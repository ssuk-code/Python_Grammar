# 1. 사전(Dictionary)

# Key-Value(키-값)가 한 쌍을 이룸
my_dictionary = {
    5 : 25,
    2 : 4,
    3 : 9
}

print(type(my_dictionary))  # <class 'dict>
print(my_dictionary[5])     # 딕셔너리[키] = 값, 25 출력
my_dictionary[9] = 81       # 기존 딕셔너리에 추가됨
# key의 타입은 int뿐만 아니라 str 가능
my_family = {
    '엄마' : '김자옥',
    '아빠' : '이석진',
    '아들' : '이동민',
    '딸' : '이지영'
}
print(my_family['아빠'])    # '이석진' 출력

# 2. 사전 활용

my_family = {
    '엄마' : '김자옥',
    '아빠' : '이석진',
    '아들' : '이동민',
    '딸' : '이지영'
}
# values : 값들의 리스트를 반환
print(my_family.values())               # ['김자옥', '이석진', '이동민', '이지영']
# 값이 존재하는지 판별하기
print('이지영' in my_family.values())   # True
print('성태호' in my_family.values())   # False
# 값 하나씩 출력하기
for value in my_family.values():
    print(value)
# keys : 값들의 리스트를 반환
print(my_family.keys())                 # ['엄마', '아빠', '아들', '딸']
# 카가 존재하는지 판별하기
print('아빠' in my_family.keys())       # True
print('성태호' in my_family.keys())     # False
# 키 하나씩 출력하기
for key in my_family.keys():
    print(key)
# 키와 값 출력하기
for key in my_family.keys():
    print(key, my_family[key])
for key, value in my_family.items():
    print(key, value)

# 실습과제
# 영어 단어장

# 1. 단어장 만들기
vocab = {
    'sanitizer' : '살균제'
    'ambition' : '야망'
    'conscience' : '양심'
    'civilization' : '문명'
}
print(vocab)

# 2. 새로운 단어들 추가
vocab['privilege'], vocab['principle'] = '특권', '원칙'
print(vocab)

# 실습과제
# 사전 뒤집기

# 사전의 key와 value를 뒤집어 주는 함수 reverse_dict를 작성
# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(dict):
    new_dict = {}  # 새로운 사전
    
    # dict의 key와 value를 뒤집어서 new_dict에 저장
    for key, value in dict.items():
        new_dict[value] = key
    
    return new_dict  # 변환한 새로운 사전 리턴

# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))

# 실습과제
# 투표 집계하기

# 리스트 votes의 정보를 토대로, 사전 vote_counter에 후보별 득표수를 정리하기
# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    if name not in vote_counter:
        vote_counter[name] = 1
    else:
        vote_counter[name] += 1

# 후보별 득표수 출력
print(vote_counter)