from itertools import combinations


def solution(orders, course):
    answer = []

    course_dict = {}
    max_size = 0
    for order in orders:
        for i in range(2, len(order) + 1):
            temp = list(order)
            temp.sort()
            order = ''.join(temp)
            for char in combinations(order, i):
                check = ''.join(char)
                if max_size < len(check): max_size = len(check)
                if check in course_dict: course_dict[check] += 1
                else: course_dict[check] = 1

    if max_size < max(course): max_size = max(course)

    course_list = [[] for _ in range(max_size + 1)]
    for key, value in course_dict.items():
        course_list[len(key)].append((key, value))

    for size in course:
        if len(course_list[size]) > 0:
            m = max(course_list[size], key=lambda x: x[1])[1]
            if m > 1:
                course_list[size].sort(key=lambda x: x[1], reverse=True)
                #print(course_list[size])
                idx = 0
                while True:
                    if idx >= len(course_list[size]) or course_list[size][idx][1] < m: break
                    answer.append(course_list[size][idx][0])
                    idx += 1
        answer.sort()

    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))