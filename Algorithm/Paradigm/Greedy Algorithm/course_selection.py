def course_selection(course_list):
    # 먼저 시작하는 순으로 정렬
    # sorted_list = sorted(course_list, key=lambda x: x[0])

    # 먼저 끝나는 순으로 정렬
    # sorted_list = sorted(course_list, key=lambda x: x[1])

    # 짧은 순으로 정렬
    # sorted_list = sorted(course_list, key=lambda x: x[1] - x[0])
    
    # 수업을 먼저 끝나는 순으로 정렬
    course_list.sort(key=lambda x:x[1])
    
    # 수업을 담을 리스트
    my_selection = []
    
    # 이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업 고르기
    for course in course_list:
        # 제일 일찍 끝나는 수업은 무조건 듣기
        if not my_selection:
            my_selection.append(course)
        # 마지막 수업이 끝나기 전에 새 수업이 시작하면 겹침
        elif my_selection[-1][1] < course[0]:
            my_selection.append(course)
    
    # 수업을 끝나는 순서로 정렬한다
    # sorted_list = sorted(course_list, key=lambda x: x[1])

    # 가장 먼저 끝나는 수업은 무조건 듣는다
    # my_selection = [sorted_list[0]]

    # 이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업을 고른다
    # for course in sorted_list:
        # 마지막 수업이 끝나기 전에 새 수업이 시작하면 겹친다
        # if course[0] > my_selection[-1][1]:
        #     my_selection.append(course)    
    
    return my_selection


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))