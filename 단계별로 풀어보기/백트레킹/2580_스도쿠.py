# 문제
# 스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다. 이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데, 게임 시작 전 몇 몇 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.
#
#
#
# 나머지 빈 칸을 채우는 방식은 다음과 같다.
#
# 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
# 위의 예의 경우, 첫째 줄에는 1을 제외한 나머지 2부터 9까지의 숫자들이 이미 나타나 있으므로 첫째 줄 빈칸에는 1이 들어가야 한다.
#
#
#
# 또한 위쪽 가운데 위치한 3x3 정사각형의 경우에는 3을 제외한 나머지 숫자들이 이미 쓰여있으므로 가운데 빈 칸에는 3이 들어가야 한다.
#
#
#
# 이와 같이 빈 칸을 차례로 채워 가면 다음과 같은 최종 결과를 얻을 수 있다.
#
#
#
# 게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.
#
# 입력
# 아홉 줄에 걸쳐 한 줄에 9개씩 게임 시작 전 스도쿠판 각 줄에 쓰여 있는 숫자가 한 칸씩 띄워서 차례로 주어진다. 스도쿠 판의 빈 칸의 경우에는 0이 주어진다. 스도쿠 판을 규칙대로 채울 수 없는 경우의 입력은 주어지지 않는다.
#
# 출력
# 모든 빈 칸이 채워진 스도쿠 판의 최종 모습을 아홉줄에 걸쳐 한 줄에 9개씩 한 칸씩 띄워서 출력한다.
#
# 스도쿠 판을 채우는 방법이 여럿인 경우는 그 중 하나만을 출력한다.
#
# 예제 입력 1
# 0 3 5 4 6 9 2 7 8
# 7 8 2 1 0 5 6 0 9
# 0 6 0 2 7 8 1 3 5
# 3 2 1 0 4 6 8 9 7
# 8 0 4 9 1 3 5 0 6
# 5 9 6 8 2 0 4 1 3
# 9 1 7 6 5 2 0 8 0
# 6 0 3 7 0 1 9 5 2
# 2 5 8 3 9 4 7 6 0
# 예제 출력 1
# 1 3 5 4 6 9 2 7 8
# 7 8 2 1 3 5 6 4 9
# 4 6 9 2 7 8 1 3 5
# 3 2 1 5 4 6 8 9 7
# 8 7 4 9 1 3 5 2 6
# 5 9 6 8 2 7 4 1 3
# 9 1 7 6 5 2 3 8 4
# 6 4 3 7 8 1 9 5 2
# 2 5 8 3 9 4 7 6 1
import copy


def check_squ(x, y, n):
    for i in range(3):
        for j in range(3):
            if n == v[3 * (x // 3) + i][3 * (y // 3) + j]: return False
    return True


def dfs(idx, idy, i):
    if i in v[idx]: return
    if i in (lambda y: v[y] for y in range(9)): return
    if not check_squ(idx, idy, i): return

    for ii in range(1, 10):
        dfs(idx, idy, ii)

v = [list(map(int, input().split())) for _ in range(9)]
chk_list = []
stack = []
for idx, v_x in enumerate(v):
    for idy, value in enumerate(v_x):
        if value == 0:
            for i in range(1, 10):
                dfs(idx, idy, i)
            chk_list.append((idx, idy))

# for chk_point in chk_list:

for v_x in v:
    print(' '.join(map(str, v_x)))

### ############## ###
### 미해결 시간초과 ###
### ############## ###


# def check_row(x, n):
#     if n not in v[x]: return True
#     else: return False
#
#
# def check_col(y, n):
#     for i in range(9):
#         if n == v[i][y]: return False
#     return True
#
#
# def check_squ(x, y, n):
#     for i in range(3):
#         for j in range(3):
#             if n == v[3 * (x // 3) + i][3 * (y // 3) + j]: return False
#     return True
#
#
# def check(x, y):
#     result = []
#     for n in range(1, 10):
#         if check_row(x, n) and check_col(y, n) and check_squ(x, y, n): result.append(n)
#     if len(result) == 1: return result[0]
#     else: return 0
#
#
# v = [list(map(int, input().split())) for _ in range(9)]
# n = 0
# while True:
#     cnt = 0
#     for v_x in v:
#         cnt += v_x.count(0)
#     if cnt == 0: break
#     x = n // 9
#     y = n % 9
#     if not v[x][y]:
#         change = check(x, y)
#         print(x, y, change)
#         v[x][y] = change
#     n += 1
#     n %= 81
# # print()
# for v_x in v:
#     print(' '.join(map(str, v_x)))