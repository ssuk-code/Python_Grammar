# 모듈 : 여러가지 기능을 정리해 둔 파이썬 파일
# 스탠다드 라이브러리
# - int, float, string 같은 자료형
# - print, dir 같은 내장 함수
# - 유용한 기능을 제공하는 모듈들(스탠다드 모듈)

# math : 기본적인 수학 모듈
import math

# 로그 함수
print(math.log10(100))
# 코사인 함수 (모든 삼각함수는 라디안을 사용)
print(math.cos(0))

# random : 랜덤한 숫자를 생성하기 위한 다양한 함수들을 제공
import random

# 랜덤한 정수 1 <= N <= 20 
print(random.randint(1, 20))

# 랜덤한 소수 0 <= x <= 1
print(random.uniform(0, 1))

# datetime : 날짜와 시간을 다루기 위한 다양한 '클래스'
import datetime 

# 현재 시간과 날짜
today = datetime.datetime.now()
print(today)

# 출력값을 "요일, 월 일 연도"로 포매팅
print(today.strftime("%A, %B %dth %Y"))

# 특정 시간과 날짜
pi_day = datetime.datetime(2020, 1, 1, 0, 0, 0)
print(pi_day)

# 두 datetime의 차이
print(today - pi_day)

# os : Operating System
# os 모듈을 통해서 파이썬으로 운영체제를 조작하거나 운영체제에 대한 정보를 가져옴
import os

# 현재 어떤 계정으로 로그인 돼있는지 확인
print(os.getlogin())

# 현재 파일의 디렉토리 확인 
print(os.getcwd())

# 현재 프로세스 ID 확인 
print(os.getpid())

# os.path : 모든 파일 경로를 다룰 때
import os.path

# 프로젝트 디렉토리 경로 '/Users/dlstn/PycharmProjects/standard_modules'
# 현재 파일 경로 '/Users/dlstn/PycharmProjects/standard_modules/main.py'

# 주어진 경로를 절대 경로로
print(os.path.abspath('..'))

# 주어진 경로를 현재 디렉토리를 기준으로 한 상대 경로로
print(os.path.relpath('/Users/dlstn/PycharmProjects'))

# 주어진 경로들을 병합
print(os.path.join('/Users/dlstn/PycharmProjects', 'standard_modules'))

# re : Regular Expression(RegEx, re, 정규 표현식)
# 특정한 규칙/패턴을 가진 문자열을 표현하는 데 사용
import re 

# 알파벳으로 구성된 단어들만 매칭
pattern = re.compile('^[A-Za-z]+$')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))

print()

# 숫자가 포함된 단어들만 매칭
pattern = re.compile('.*\d+')
print(pattern.match('I'))
print(pattern.match('love'))
print(pattern.match('python3'))

# pickle : 파이썬 오브젝트(객체)를 바이트(byte) 형식으로 바꿔서 파일에 저장 가능, 저장된 오브젝트를 읽어올 수 있음
import pickle

# 딕셔너리 오브젝트
obj = {'my': 'dictionary'}  

# obj를 filename.pickle 파일에 저장
with open('filename.pickle', 'wb') as f:
    pickle.dump(obj, f)

# filename.pickle에 있는 오브젝트를 읽어옴 
with open('filename.pickle', 'rb') as f:
    obj = pickle.load(f)

print(obj)

# json : pickle과 비슷하지만 오브젝트를 JSON 형식 바꿔줌
# JSON 형식에 맞는 데이터 (기본 데이터 타입들, 리스트, 딕셔너리)만 바꿀 수 있음
import json

# 딕셔너리 오브젝트
obj = {'my': 'dictionary'}  

# obj를 filename.json 파일에 저장
with open('filename.json', 'w') as f:
    json.dump(obj, f)

# filename.json에 있는 오브젝트를 읽어옴 
with open('filename.json', 'r') as f:
    obj = json.load(f)

print(obj)

# copy : 파이썬 오브젝트를 복사할 때
import copy

# '=' 연산자는 실제로 리스트를 복사하지 않음
# 리스트를 복사하려면 슬라이싱을 사용하거나 copy.copy() 함수를 사용해야 함
a = [1, 2, 3] 
b = a
c = a[:]
d = copy.copy(a)
a[0] = 4
print(a, b, c, d)

# 하지만 오브젝트 안에 오브젝트가 있는 경우 copy.copy() 함수는 가장 바깥에 있는 오브젝트만 복사함 
# 오브젝트를 재귀적으로 복사하려면 copy.deepcopy() 함수를 사용해야 함
a = [[1,2,3], [4,5,6], [7,8,9]]
b = copy.copy(a)
c = copy.deepcopy(a)
a[0][0] = 4
print(a, b, c)

# sqlite3 : 파이썬에서 SQLite 데이터베이스를 사용
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('example.db')

# SQL 문 실행 
c = conn.cursor()
c.execute('''SELECT ... FROM ... WHERE ... ''')

# 가져온 데이터를 파이썬에서 사용
rows = c.fetchall()
for row in rows:
    print(row)

# 연결 종료
conn.close()