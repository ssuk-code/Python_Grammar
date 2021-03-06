# 1. aliasing

# 가변형 : dict, list
# 불변형 : tuple, str, int, bool, float
x = 5
y = x
y = 3
print(x)    # 5
print(y)    # 3

# 리스트에서 리스트 A = 리스트 B 라고 할당하면,
# 참조가 되어 값을 한곳에서 변경을해도 똑같이 변경
x = [2, 3, 5, 7, 11]
y = x
y[2] = 4
print(x)    # [2, 3, 4, 7, 11]
print(y)    # [2, 3, 4, 7, 11]

# list()를 이용하면 다른 객체에 영향을 끼치지 않음
x = [2, 3, 5, 7, 11]
y = list(x)
y[2] = 4
print(x)    # [2, 3, 5, 7, 11]
print(y)    # [2, 3, 4, 7, 11]

# 새로운 리스트를 부여해도 다른 객체에 영향을 끼치지 않음
x = [2, 3, 5, 7, 11]
y = x
y = [2, 3]
print(x)    # [2, 3, 5, 7, 11]
print(y)    # [2, 3]