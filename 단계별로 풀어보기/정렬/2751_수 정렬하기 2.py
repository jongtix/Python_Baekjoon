# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
#
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
#
# 예제 입력 1
# 5
# 5
# 4
# 3
# 2
# 1
# 예제 출력 1
# 1
# 2
# 3
# 4
# 5


###############################################################################################################################################################
###미해결###
###############################################################################################################################################################

# def divide_list(l):
#     if len(l) == 1: return l
#     mid = len(l) // 2
#     left_list = l[:mid]
#     right_list = l[mid:]
#     result = list()
#     compare(divide_list(left_list), divide_list(right_list))
#
#     return result
#
#
# def merge_list(l):
#     if len(l) == 1: return l
#     return
#
# number_list = [int(input()) for _ in range(int(input()))]
# print(divide_list(number_list))
# print('\n'.join(map(str, result)))
#
number_list = [int(input()) for _ in range(int(input()))]
temp = [number_list]

while True:
    # print(temp)
    t = []
    for temp_list in temp:
        if len(temp_list) != 1:
            t.append(temp_list[:len(temp_list) // 2])
            t.append(temp_list[len(temp_list) // 2:])
        else:
            t.append(temp_list)
    temp = t
    if len(temp) == len(number_list): break
# print(temp)

idx = 0
while True:
    t = []
    for comp in range(0, len(temp), 2):
        r = []
        if comp + 1 != len(temp):
            while temp[comp] and temp[comp + 1]:
                if temp[comp][0] > temp[comp + 1][0]:
                    r.append(temp[comp + 1].pop(0))
                if not temp[comp]:
                    for ins in temp[comp + 1]:
                        r.append(ins)
                    break
                if not temp[comp + 1]:
                    for ins in temp[comp]:
                        r.append(ins)
                    break
        else:
            r.append(temp[comp][0])
        t.append(r)
    temp = t
    if len(temp) == 1:
        result = temp[0]
        break
print('\n'.join(map(str, result)))
