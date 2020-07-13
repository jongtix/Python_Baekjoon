# "현재 상태"를 정점으로 표현하여 그래프를 만들고 최단거리를 구하는 문제
# 문제
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
#
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
#
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.
#
# 출력
# 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
#
# 예제 입력 1
# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000
# 예제 출력 1
# 15
# 예제 입력 2
# 4 4
# 0111
# 1111
# 1111
# 1110
# 예제 출력 2
# -1
import sys, copy

# N, M = map(int, sys.stdin.readline().split())
# graph = []
# visited = [[0 for _ in range(M)] for _ in range(N)]
# for _ in range(N):
#     graph.append(list(map(int, list(sys.stdin.readline()))))
#
# sub_x = [1, -1, 0, 0]
# sub_y = [0, 0, 1, -1]
#
#
# def bfs(graph, visited, position, move_cnt, broken_wall):
#     if position == (N - 1, M - 1): return
#     for i in range(4):
#         if 0 <= cur_x + sub_x[i] < N and 0 <= cur_y + sub_y[i] < M:
#             if broken_wall < 1:
#                 temp_graph = copy.copy(graph)
#
#
# stack = []
# stack.append((0, 0, 0, 0))
# if not N - 1 == 0 and not M - 1 == 0:
#     while stack:
#         cur_x, cur_y, move_cnt, broken_wall = map(int, stack.pop())
#         for i in range(4):
#             if 0 <= cur_x + sub_x[i] < N and 0 <= cur_y + sub_y[i] < M:
#                 if broken_wall < 1:
#                     graph
#
#                 graph[cur_x + sub_x[i]][cur_y + sub_y[i]] == 0 and (not visited[cur_x + sub_x[i]][cur_y + sub_y[i]] or visited[cur_x + sub_x[i]][cur_y + sub_y[i]] > move_cnt + 1):
#                 stack.append((cur_x + sub_x[i], cur_y + sub_y[i], move_cnt + 1, broken_wall))
#     print(visited[N - 1][M - 1])
# else:
#     print(0)