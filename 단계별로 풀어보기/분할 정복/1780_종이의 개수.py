# 쿼드트리와 비슷한데 4개 대신 9개로 나누는 문제
# 문제
# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다. 우리는 이 행렬을 적절한 크기로 자르려고 하는데, 이때 다음의 규칙에 따라 자르려고 한다.
#
# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1≤N≤3^7, N은 3^k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.
#
# 출력
# 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.
#
# 예제 입력 1
# 9
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 0 1 -1 0 1 -1 0 1 -1
# 0 -1 1 0 1 -1 0 1 -1
# 0 1 -1 1 0 -1 0 1 -1
# 예제 출력 1
# 10
# 12
# 11
import sys

# 시간 초과 실패
# N = int(sys.stdin.readline())
# cnt_zero = 0
# cnt_one = 0
# cnt_minus = 0
#
#
# def cut(start_x, end_x, start_y, end_y, s):
#     global org_list, cnt_zero, cnt_one, cnt_minus
#
#     size = len([x[start_y:end_y] for x in org_list[start_x:end_x]]) // 3
#
#     if size == 0:
#         if org_list[start_x][start_y] == 0:
#             cnt_zero += 1
#         elif org_list[start_x][start_y] == 1:
#             cnt_one += 1
#         elif org_list[start_x][start_y] == -1:
#             cnt_minus += 1
#         return s + str(org_list[start_x][start_y])
#
#     new_list_1 = [x[start_y:start_y + size] for x in org_list[start_x:start_x + size]]
#     new_list_2 = [x[start_y + size:start_y + size * 2] for x in org_list[start_x:start_x + size]]
#     new_list_3 = [x[start_y + size * 2:start_y + size * 3] for x in org_list[start_x:start_x + size]]
#     new_list_4 = [x[start_y:start_y + size] for x in org_list[start_x + size:start_x + size * 2]]
#     new_list_5 = [x[start_y + size:start_y + size * 2] for x in org_list[start_x + size:start_x + size * 2]]
#     new_list_6 = [x[start_y + size * 2:start_y + size * 3] for x in org_list[start_x + size:start_x + size * 2]]
#     new_list_7 = [x[start_y:start_y + size] for x in org_list[start_x + size * 2:start_x + size * 3]]
#     new_list_8 = [x[start_y + size:start_y + size * 2] for x in org_list[start_x + size * 2:start_x + size * 3]]
#     new_list_9 = [x[start_y + size * 2:start_y + size * 3] for x in org_list[start_x + size * 2:start_x + size * 3]]
#
#     if new_list_1 == new_list_2 == new_list_3 == new_list_4 == new_list_5 == new_list_6 == new_list_7 == new_list_8 == new_list_9:
#         if new_list_1 == [[0 for _ in range(size)] for _ in range(size)]:
#             cnt_zero += 1
#             return s + '0'
#         elif new_list_1 == [[1 for _ in range(size)] for _ in range(size)]:
#             cnt_one += 1
#             return s + '1'
#         elif new_list_1 == [[-1 for _ in range(size)] for _ in range(size)]:
#             cnt_minus += 1
#             return s + '-1'
#         else:
#             for temp in new_list_1:
#                 s += ''.join(list(map(str, temp)))
#             return s
#
#     else:
#         s += '('
#         s = cut(start_x, start_x + size, start_y, start_y + size, s)
#         s = cut(start_x, start_x + size, start_y + size, start_y + size * 2, s)
#         s = cut(start_x, start_x + size, start_y + size * 2, start_y + size * 3, s)
#         s = cut(start_x + size, start_x + size * 2, start_y, start_y + size, s)
#         s = cut(start_x + size, start_x + size * 2, start_y + size, start_y + size * 2, s)
#         s = cut(start_x + size, start_x + size * 2, start_y + size * 2, start_y + size * 3, s)
#         s = cut(start_x + size * 2, start_x + size * 3, start_y, start_y + size, s)
#         s = cut(start_x + size * 2, start_x + size * 3, start_y + size, start_y + size * 2, s)
#         s = cut(start_x + size * 2, start_x + size * 3, start_y + size * 2, start_y + size * 3, s)
#         s += ')'
#         return s
#
#
# org_list = []
# for _ in range(N):
#     org_list.append(list(map(int, sys.stdin.readline()[:-1].split())))
# cut(0, N, 0, N, '')
# print(cnt_minus)
# print(cnt_zero)
# print(cnt_one)

# 시간 초과 실패
# N = int(sys.stdin.readline())
# cnt_zero = 0
# cnt_one = 0
# cnt_minus = 0
#
#
# def cut(org_list, s):
#     global cnt_zero, cnt_one, cnt_minus
#
#     size = len(org_list) // 3
#
#     if size == 0:
#         if org_list[0][0] == 0:
#             cnt_zero += 1
#         elif org_list[0][0] == 1:
#             cnt_one += 1
#         elif org_list[0][0] == -1:
#             cnt_minus += 1
#         return s + str(org_list[0][0])
#
#     new_list_1 = [x[:size] for x in org_list[:size]]
#     new_list_2 = [x[size:size * 2] for x in org_list[:size]]
#     new_list_3 = [x[size * 2:size * 3] for x in org_list[:size]]
#     new_list_4 = [x[:size] for x in org_list[size:size * 2]]
#     new_list_5 = [x[size:size * 2] for x in org_list[size:size * 2]]
#     new_list_6 = [x[size * 2:size * 3] for x in org_list[size:size * 2]]
#     new_list_7 = [x[:size] for x in org_list[size * 2:size * 3]]
#     new_list_8 = [x[size:size * 2] for x in org_list[size * 2:size * 3]]
#     new_list_9 = [x[size * 2:size * 3] for x in org_list[size * 2:size * 3]]
#
#     if new_list_1 == new_list_2 == new_list_3 == new_list_4 == new_list_5 == new_list_6 == new_list_7 == new_list_8 == new_list_9:
#         if new_list_1 == [[0 for _ in range(size)] for _ in range(size)]:
#             cnt_zero += 1
#             return s + '0'
#         elif new_list_1 == [[1 for _ in range(size)] for _ in range(size)]:
#             cnt_one += 1
#             return s + '1'
#         elif new_list_1 == [[-1 for _ in range(size)] for _ in range(size)]:
#             cnt_minus += 1
#             return s + '-1'
#         else:
#             for temp in new_list_1:
#                 s += ''.join(list(map(str, temp)))
#             return s
#
#     else:
#         s += '('
#         s = cut(new_list_1, s)
#         s = cut(new_list_2, s)
#         s = cut(new_list_3, s)
#         s = cut(new_list_4, s)
#         s = cut(new_list_5, s)
#         s = cut(new_list_6, s)
#         s = cut(new_list_7, s)
#         s = cut(new_list_8, s)
#         s = cut(new_list_9, s)
#         s += ')'
#         return s
#
#
# org_list = []
# for _ in range(N):
#     org_list.append(list(map(int, sys.stdin.readline()[:-1].split())))
# cut(org_list, '')
# print(cnt_minus)
# print(cnt_zero)
# print(cnt_one)


# 런타임 에러 실패
# def cut(org_list: list, s: str):
#     global cnt_one, cnt_minus, cnt_zero
#
#     size = len(org_list)
#     if org_list == [[0 for _ in range(size)] for _ in range(size)]:
#         cnt_zero += 1
#         return '0'
#     elif org_list == [[1 for _ in range(size)] for _ in range(size)]:
#         cnt_one += 1
#         return '1'
#     elif org_list == [[-1 for _ in range(size)] for _ in range(size)]:
#         cnt_minus += 1
#         return '-1'
#     else:
#         s += '('
#         s += cut([[org_list[i][j] for i in range(0, size // 3)] for j in range(0, size // 3)], '')
#         s += cut([[org_list[i][j] for i in range(0, size // 3)] for j in range(size // 3, (size // 3) * 2)], '')
#         s += cut([[org_list[i][j] for i in range(0, size // 3)] for j in range((size // 3) * 2, (size // 3) * 3)], '')
#         s += cut([[org_list[i][j] for i in range(size // 3, (size // 3) * 2)] for j in range(0, size // 3)], '')
#         s += cut([[org_list[i][j] for i in range(size // 3, (size // 3) * 2)] for j in range(size // 3, (size // 3) * 2)], '')
#         s += cut([[org_list[i][j] for i in range(size // 3, (size // 3) * 2)] for j in range((size // 3) * 2, (size // 3) * 3)], '')
#         s += cut([[org_list[i][j] for i in range((size // 3) * 2, (size // 3) * 3)] for j in range(0, size // 3)], '')
#         s += cut([[org_list[i][j] for i in range((size // 3) * 2, (size // 3) * 3)] for j in range(size // 3, (size // 3) * 2)], '')
#         s += cut([[org_list[i][j] for i in range((size // 3) * 2, (size // 3) * 3)] for j in range((size // 3) * 2, (size // 3) * 3)], '')
#         s += ')'
#         return s
#
#
# N = int(sys.stdin.readline())
# cnt_minus = 0
# cnt_zero = 0
# cnt_one = 0
# org_list = []
# for _ in range(N):
#     org_list.append(list(map(int, list(sys.stdin.readline()[:-1].split(' ')))))
# cut(org_list, '')
# print(cnt_minus, cnt_zero, cnt_one, sep='\n')