# 문제
# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
#
# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
#
# ***
# * *
# ***
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.


def print_stars_retry(N, i, j):
    if N == 1:
        answer[i][j] = '*'
        return
    if (i // int(N / 3)) % 3 == 1 and (j // int(N / 3)) % 3 == 1:
        answer[i][j] = ' '
        return

    print_stars_retry(int(N/3), i, j)


N = int(input())
# print(1 in range(3 ** (int(N ** (1/3)) - 1), 2 * (3 ** (int(N ** (1/3)) - 1)) + 1))
# print(range(3 ** (int(N ** (1/3)) - 1), 2 * (3 ** (int(N ** (1/3)) - 1))))
answer = [[' ' for x in range(N)] for y in range(N)]
for i in range(N):
    for j in range(N):
        # breakpoint()
        print_stars_retry(N, i, j)
for i in answer:
    for j in i:
        print(j, end='')
    print()


# def print_stars_retry(N, i, j):
#     if N == 1: answer[i][j] = '*'
#     else:
#         if (i - N * (i // N)) in range(3 ** (int(N ** (1/3)) - 1), 2 * (3 ** (int(N ** (1/3)) - 1))) and (j - N * (j // N)) in range(3 ** (int(N ** (1/3)) - 1), 2 * (3 ** (int(N ** (1/3)) - 1))): answer[i][j] = ' '
#         else: print_stars_retry(int(N/3), i, j)
#
#
# N = int(input())
# # print(1 in range(3 ** (int(N ** (1/3)) - 1), 2 * (3 ** (int(N ** (1/3)) - 1)) + 1))
# # print(range(3 ** (int(N ** (1/3)) - 1), 2 * (3 ** (int(N ** (1/3)) - 1))))
# answer = [[None for x in range(N)] for y in range(N)]
# for i in range(N):
#     for j in range(N):
#         # breakpoint()
#         print_stars_retry(N, i, j)
# for i in answer:
#     for j in i:
#         print(j, end='')
#     print()


# def print_stars(N, i, j):
#     if N == 1: return
#     else:
#         comp_i = i
#         comp_j = j
#         if i >= N:
#             comp_i = i - N * (i // N)
#         if j >= N:
#             comp_j = j - N * (j // N)
#         if ((comp_i >= int(N / 3)) and (comp_j >= int(N / 3))) and ((comp_i < 2 * int(N / 3)) and (comp_j < 2 * int(N / 3))):
#             answer[i][j] = ' '
#         else:
#             print_stars(int(N/3), i, j)
#
# N = int(input())
# answer = [['*' for x in range(N)] for y in range(N)]
# for i in range(N):
#     for j in range(N):
#         # breakpoint()
#         print_stars(N, i, j)
# for i in answer:
#     for j in i:
#         print(j, end='')
#     print()
# print(answer)