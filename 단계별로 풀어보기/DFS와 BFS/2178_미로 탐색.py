# BFS의 특징은 각 정점을 최단경로로 방문한다는 것입니다. 이 점을 활용해 최단거리를 구해 봅시다.
# 문제
# N×M크기의 배열로 표현되는 미로가 있다.
#
# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
#
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
#
# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
#
# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
#
# 예제 입력 1
# 4 6
# 101111
# 101010
# 101011
# 111011
# 예제 출력 1
# 15
# 예제 입력 2
# 4 6
# 110110
# 110110
# 111111
# 111101
# 예제 출력 2
# 9
# 예제 입력 3
# 2 25
# 1011101110111011101110111
# 1110111011101110111011101
# 예제 출력 3
# 38
# 예제 입력 4
# 7 7
# 1011111
# 1110001
# 1000001
# 1000001
# 1000001
# 1000001
# 1111111
# 예제 출력 4
# 13
import sys

N, M = map(int, sys.stdin.readline()[:-1].split(' '))
graph = []
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline()[:-1]))))

stack = []
stack.append((0, 0))
visited[0][0] += 1

while stack:
    x, y = map(int, stack.pop())
    # print(x, y)
    sub_x = [1, -1, 0, 0]
    sub_y = [0, 0, 1, -1]

    for i in range(4):
        if 0 <= x + sub_x[i] < N and 0 <= y + sub_y[i] < M and graph[x + sub_x[i]][y + sub_y[i]] and ((visited[x][y] + 1 < visited[x + sub_x[i]][y + sub_y[i]]) or not visited[x + sub_x[i]][y + sub_y[i]]):
        # if 0 <= x + sub_x[i] < N and 0 <= y + sub_y[i] < M and graph[x + sub_x[i]][y + sub_y[i]] and (visited[x][y] + 1 < visited[x + sub_x[i]][y + sub_y[i]])
            visited[x + sub_x[i]][y + sub_y[i]] = visited[x][y] + 1
            # print((x + sub_x[i], y + sub_y[i]))
            stack.append((x + sub_x[i], y + sub_y[i]))

# for v in visited:
#     print(v)
print(visited[N - 1][M - 1])

# sys.setrecursionlimit(1000000)
# N, M = map(int, sys.stdin.readline()[:-1].split(' '))
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, list(sys.stdin.readline()[:-1]))))
# visited = [[0 for _ in range(M)] for _ in range(N)]
# cnt = 0
# result = []
#
# def dfs(graph, visited, start):
#     global cnt
#     # print(start)
#     x, y = map(int, start)
#     cnt += 1
#     if x == N - 1 and y == M - 1: print(cnt)
#     if graph[x][y] == 1:
#         if not visited[x][y]:
#             visited[x][y] += 1
#             result.append((x, y))
#         else:
#             cnt -= 1
#     flag = False
#     for i in range(2):
#         # print(x + (-1) ** (i + 1))
#         if (x + (-1) ** (i + 1) >= 0 and x + (-1) ** (i + 1) < N) and graph[x + (-1) ** (i + 1)][y] == 1 and not visited[x + (-1) ** (i + 1)][y]:
#             flag = True
#             dfs(graph, visited, (x + (-1) ** (i + 1), y))
#         if (y + (-1) ** (i + 1) >= 0 and y + (-1) ** (i + 1) < M) and graph[x][y + (-1) ** (i + 1)] == 1 and not visited[x][y + (-1) ** (i + 1)]:
#             flag = True
#             dfs(graph, visited, (x, y + (-1) ** (i + 1)))
#     if not flag: result.remove((x, y))
#     return cnt
#
#
# dfs(graph, visited, (0, 0))
# print(result)
# print(visited[N - 1][M - 1])

# stack = []
# stack.append((0, 0))
# result = []
# while stack:
#     x, y = map(int, stack.pop())
#     print(x, y)
#     if x == N - 1 and y == M - 1: break
#     if not visited[x][y]:
#         result.append((x, y))
#         visited[x][y] = True
#         cnt += 1
#     print('cnt: ', cnt)
#     flag = False
#     if x < N - 1 and graph[x + 1][y] == 1 and not visited[x + 1][y]:
#         stack.append((x + 1, y))
#         flag = True
#     if y < M - 1 and graph[x][y + 1] == 1 and not visited[x][y + 1]:
#         stack.append((x, y + 1))
#         flag = True
#     if x > 0 and graph[x - 1][y] == 1 and not visited[x - 1][y]:
#         stack.append((x - 1, y))
#         flag = True
#     if y > 0 and graph[x][y - 1] == 1 and not visited[x][y - 1]:
#         stack.append((x, y - 1))
#         flag = True
#     if not flag: cnt -= 1
# print(result)
# print(len(result))
# print(cnt)