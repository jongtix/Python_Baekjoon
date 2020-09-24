import string


def solution(num):
    str_list = [''] + list(string.ascii_uppercase)

    row = num // 702 + 1
    col = num % 702
    if col == 0:
        row -= 1
        col = 702

    first = col // 26
    second = col % 26
    if second == 0:
        first -= 1
        second = 26

    return str(row) + str_list[first] + str_list[second]


print(solution(1))
print(solution(26))
print(solution(27))
print(solution(702))
print(solution(703))
print(solution(1404))
print(solution(1405))