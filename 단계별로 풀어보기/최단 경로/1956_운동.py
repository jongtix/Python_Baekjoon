# -*- coding: utf-8 -*-
# 최단 거리 알고리즘을 응용하여 최단 사이클을 찾는 문제
# 문제
# V개의 마을와 E개의 도로로 구성되어 있는 도시가 있다. 도로는 마을과 마을 사이에 놓여 있으며, 일방 통행 도로이다. 마을에는 편의상 1번부터 V번까지 번호가 매겨져 있다고 하자.
#
# 당신은 도로를 따라 운동을 하기 위한 경로를 찾으려고 한다. 운동을 한 후에는 다시 시작점으로 돌아오는 것이 좋기 때문에, 우리는 사이클을 찾기를 원한다. 단, 당신은 운동을 매우 귀찮아하므로, 사이클을 이루는 도로의 길이의 합이 최소가 되도록 찾으려고 한다.
#
# 도로의 정보가 주어졌을 때, 도로의 길이의 합이 가장 작은 사이클을 찾는 프로그램을 작성하시오. 두 마을을 왕복하는 경우도 사이클에 포함됨에 주의한다.
#
# 입력
# 첫째 줄에 V와 E가 빈칸을 사이에 두고 주어진다. (2<=V<=400, 0<=E<=V*(V-1)) 다음 E개의 줄에는 각각 세 개의 정수 a, b, c가 주어진다. a번 마을에서 b번 마을로 가는 거리가 c인 도로가 있다는 의미이다. (a->b임에 주의) 거리는 10,000 이하의 자연수이다.
#
# 출력
# 첫째 줄에 최소 사이클의 도로 길이의 합을 출력한다. 운동 경로를 찾는 것이 불가능한 경우에는 -1을 출력한다.
#
# 예제 입력 1
# 3 4
# 1 2 1
# 3 2 1
# 1 3 5
# 2 3 2
# 예제 출력 1
# 3
import sys, heapq, math

# 틀렸습니다 실패
# V, E = map(int, sys.stdin.readline()[:-1].split())
# graph = [[] for _ in range(V + 1)]
# cost = [[math.inf for _ in range(V + 1)] for _ in range(V + 1)]
# visited = [['' for _ in range(V + 1)] for _ in range(V + 1)]
# for _ in range(E):
#     a, b, c = map(int, sys.stdin.readline()[:-1].split())
#     graph[a].append((c, b))
#
# for start in range(1, V + 1):
#     que = [(0, start)]
#     cost[start][start] = 0
#     visited[start][start] += str(start)
#     while que:
#         cur_cost, cur_point = heapq.heappop(que)
#         for (next_cost, next_point) in graph[cur_point]:
#             if cost[start][next_point] > cur_cost + next_cost:
#                 heapq.heappush(que, (cur_cost + next_cost, next_point))
#                 cost[start][next_point] = cur_cost + next_cost
#                 visited[start][next_point] += str(cur_point)
# # for c in cost[1:]:
# #     print('\t'.join(map(str, c[1:])))
# # print()
# # for v in visited[1:]:
# #     print('\t'.join(v[1:]))
#
# min_cost = math.inf
# for idx, row_cost in enumerate(cost):
#     for jdx, cost_val in enumerate(row_cost):
#         if 0 < cost[idx][jdx] < math.inf:
#             for end in visited[idx][jdx]:
#                 end = int(end)
#                 if 0 < cost[jdx][end] < math.inf and min_cost > cost[idx][jdx] + cost[jdx][end]:
#                     min_cost = cost[idx][jdx] + cost[jdx][end]
# if min_cost == math.inf:
#     print(-1)
# else:
#     print(min_cost)