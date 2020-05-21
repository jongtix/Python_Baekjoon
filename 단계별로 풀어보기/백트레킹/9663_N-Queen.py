# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
#
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
#
# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
#
# 예제 입력 1
# 8
# 예제 출력 1
# 92
import copy


### ############## ###
### 미해결 시간초과 ###
### ############## ###


def check_root(x, y, comp_list):
    temp = copy.deepcopy(comp_list)
    for i in range(N):
        temp[x][i] = True
        temp[i][y] = True
        if x + y - i >= 0 and x + y - i < N: temp[x + y - i][i] = True
        if x - y + i >= 0 and x - y + i < N: temp[x - y + i][i] = True
    return temp


def solution(N):
    count = 0
    for start in range(N):
        row = 0
        stack = []
        queen = 0
        v = [[False for _ in range(N)] for _ in range(N)]
        stack.append(((row, start, queen + 1), check_root(row, start, copy.deepcopy(v))))
        while stack:
            idx, exist_list = stack.pop()
            if idx[0] >= N - 1:
                if idx[2] == N: count += 1
                continue
            for col in range(N):
                if not exist_list[idx[0] + 1][col]:
                    stack.append(((idx[0] + 1, col, idx[2] + 1), check_root(idx[0] + 1, col, copy.deepcopy(exist_list))))
    return count


N = int(input())
stack = []
v = []
print(solution(N))














### ###### ###
### 미해결 ###
### ###### ###

# def check_root(x, y):
#     for i in range(N):
#         v[x][i] = True
#         v[i][y] = True
#         if x + y - i >= 0 and x + y - i < N: v[x + y - i][i] = True
#         if x - y + i >= 0 and x - y + i < N: v[x - y + i][i] = True
#
#
# N = int(input())
#
# count = 0
# for start_y in range(N):
#     v = [[False for _ in range(N)] for _ in range(N)]
#     check_root(0, start_y)
#     queen = 1
#     for x in range(1, N):
#         for y in range(N):
#             if not v[x][y]:
#                 check_root(x, y)
#                 queen += 1
#                 break
#     if queen == N: count += 1
# for start in range(N):
#     v = [[False for _ in range(N)] for _ in range(N)]
#     start_x = start // N
#     start_y = start % N
#     check_root(start_x, start_y)
#     queen = 1
#     for i in range(N):
#         for j in range(N):
#             if not v[i][j]:
#                 check_root(i, j)
#                 queen += 1
#     if queen == N: count += 1
    # print('start_x:', start_x, '| start_y:', start_y)
    # for x in range(N):
    #     v[start_x][x] = True
    #     v[x][start_y] = True
    #     v[(start_x + x) % N][(start_y + x) % N] = True
    #     v[(start_x + x) % N][(start_y + x) % N] = True
    # queen = 1
    # for i in range(N):
    #     if v: break
    #     for j in range(N):
    #         if not v[i][j]:
    #             for x in range(N):
    #                 v[i][x] = True
    #                 v[x][j] = True
    #                 v[(i + x) % N][(j + x) % N] = True
    #                 v[(i + x) % N][(j - x) % N] = True
    #         queen += 1
    # if queen == N: count += 1
# print(count)