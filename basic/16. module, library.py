# 1. module : 기능들을 정리해 둔 파이썬 프로그램

# 다른 파일에 있는 함수를 호출할 수 있음
# import 파일명(확장자 .py는 생략)
# import calculator                 # calculator.py의 함수 호출
# print(calculator.add(1, 4))

# import calculator as cal          # 가지고온 파일명을 별명으로 사용(함수 호출시 cal.add)
# print(cal.add(1, 4))

# from calculator import add, devide  # 원하는 함수(add, divide)만 가져오기
# print(add(1, 3))

# from calculator import *          # 모든 함수 가져오기
# print(add(1, 3))
# print(subtract(1, 3))
# print(multifly(1, 3))
# print(divide(1, 3))

# 2. standard library(표준 라이브러리) : python 다운로드시 기본으로 깔려있는 라이브러리

import math
print(math.log10(100))
print(math.cos(0))
print(math.pi)

import random
# random : 0.0 ≤ N ≤ 1.0를 만족하는 소수를 리턴
print(random.random())
# randint : randint(a, b)를 하면, a ≤ N ≤ b를 만족하는 어떤 랜덤한 정수 N을 리턴
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
print(random.randint(1, 20))
# uniform : 두 수 사이의 랜덤한 소수를 리턴하는 함수 randint와 다르게 소수를 리턴
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))
print(random.uniform(0, 1))

import os
# getlogin : 현재 로그인 되어있는 계정 확인
print(os.getlogin())
# getcwd : 현재 파일의 경로 확인
print(os.getcwd())

import datetime
# datetime : 날짜 표현하기
pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)       # 2020-03-14 00:00:00
print(type(pi_day)) # <class 'datetime.datetime'>
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)       # 2020-03-14 13:06:15
print(type(pi_day)) # <class 'datetime.datetime'>
# timedelta : 두 datetime 값 사이의 기간
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)       # 22 days, 4:42:57.360266
print(type(today - pi_day)) # <class 'datetime.timedelta'>
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)
print(today)                # 2020-04-05 17:54:24.221660
print(today + my_timedelta) # 2020-04-10 21:05:14.221660
# datetime 해부하기
today = datetime.datetime.now()
print(today)
print(today.year)           # 연도
print(today.month)          # 월
print(today.day)            # 일
print(today.hour)           # 시
print(today.minute)         # 분
print(today.second)         # 초
print(today.microsecond)    # 마이크로초
# datetime 포맷팅
# strftime : 포맷코드를 통해 포맷팅 기능
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
today = datetime.datetime.now()
print(today)                            # 2020-04-05 18:09:55.233501
print(today.strftime("%A, %B %dth %Y")) # Sunday, April 05th 2020