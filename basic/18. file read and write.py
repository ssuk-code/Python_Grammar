# 1. 파일 읽고 쓰기

# with open('파일경로', '모드', '인코딩')
with open(r'C:\Users\dlstn\Documents\Python_grammar\basic\chicken.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.strip()) # 맨 앞과 맨 뒤의 공백(\t, \n 포함)를 제거

# 화이트 스페이스 : ' ', '\t', '\n'
# strip() : 문자열 양 끝 화이트 스페이스 제거
# lstrip() : 선행문자만 지울 때 사용함
# rstrip() : 후행문자만 지울 때 사용함

# split : 원하는 문자열로 자른 뒤 리스트로 리턴
numbers = '1, 2, 3, 4, 5, 6'
numbers_to_int= [int(number) for number in numbers.split(', ')]
print(numbers_to_int)

# 실습과제
# 코딩에 빠진 닭

# 한 달의 평균 매출을 출력
with open('data/chicken.txt', 'r') as f:
    total_revenue = 0
    total_days = 0
    
    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출

        total_revenue += revenue
        total_days += 1

    print(total_revenue / total_days)

# 파일 쓰기
# 파일이 없는 경우 'w'모드로 만들기, 있는 경우엔 'a'모드로 수정
# with open('new_file.txt', 'w') as f:
#     f.write('Helloworld!\n')
#     f.write('My name is ssuk.\n')

# 실습과제
# 단어장 만들기

# 콘솔로 영어 단어와 한국어 뜻을 받고, vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리
with open('vocabulary.txt', 'w') as f:
    while True:
        english_word = input('영어 단어를 입력하세요: ')    
        if english_word == 'q':
            break
        
        korean_word = input('한국어 뜻을 입력하세요: ')
        if korean_word == 'q':
            break
        
        f.write('{}: {}\n'.format(english_word, korean_word))

# 실습과제
# 단어 퀴즈

# vocabulary.txt 파일의 단어들을 가지고 학생들에게 문제를 내 주는 프로그램
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        
        # 유저 입력값 받기
        guess = input("{}: ".format(korean_word))
        
        # 정답 확인하기
        if guess == english_word:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))

# 실습과제
# 고급 단어장

# random 모듈과 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 내도록 하는 프로그램
# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    
    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))
    
    # 프로그램 끝내기
    if guess == 'q':
        break
    
    # 정답 확인하기
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))