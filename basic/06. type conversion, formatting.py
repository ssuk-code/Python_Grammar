# 1. 형 변환(Type Conversion, Type Casting)

# 값을 한 자료형에서 다른 자료형으로 바꾸는 것
# 정수 -> 소수, 문자열 -> 정수
# print(int(3.8)) -> 3
# print(float(3)) -> 3.0
# print(int("2") + int("5")) -> 7
# print(float("1.1") + float("2.5")) -> 3.6
# print(str(2) + str(5)) -> "25"
'''
age = 25
print("제 나이는 " + str(age) + "살입니다.")
'''
# print(int("Hello world!")) -> 문법 오류

# 2. 문자열 포맷팅(String Formatting)

# 오늘은 2019년 10월 29일입니다. 출력하기
year = 2019
month = 10
day = 29

print("오늘은 " + str(2019) + "년 " + str(10) + "월 " + str(29) + "일입니다.")

print("오늘은 %d년 %d월 %d일입니다.".format(year, month, day))

print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))

print(f"오늘은 {year}년 {month}월 {day}일입니다.")

# 실습과제
# 문자열 포맷팅 연습

wage = 5                  # 시급 (1시간에 5달러)
exchange_rate = 1142.16   # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("{}시간에 {}{} 벌었습니다.".format(5, wage * 5, "달러"))

# "1시간에 5710.8원 벌었습니다." 출력
print("{}시간에 {:.1f}{} 벌었습니다.".format(1, wage * 1 * exchange_rate, "원"))
print("%d시간에 %.1f%s 벌었습니다." % (1, wage * 1 * exchange_rate, "원"))
print(f"{1}시간에 {wage * 1 * exchange_rate:.1f}{'원'} 벌었습니다.")

# "5시간에 28554.0원 벌었습니다." 출력
print("{}시간에 {:.1f}{} 벌었습니다.".format(5, wage * 5 * exchange_rate, "원"))
print("%d시간에 %.1f%s 벌었습니다." % (5, wage * 5 * exchange_rate, "원"))
print(f"{15}시간에 {wage * 5 * exchange_rate:.1f}{'원'} 벌었습니다.")