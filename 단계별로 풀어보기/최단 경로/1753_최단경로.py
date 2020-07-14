# -*- coding: utf-8 -*-
# 다익스트라 알고리즘을 배우는 문제
# 문제
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
#
# 입력
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
#
# 출력
# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
#
# 예제 입력 1
# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6
# 예제 출력 1
# 0
# 2
# 3
# 7
# INF
import sys, heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
dist = ['INF' for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))
# print(graph)
# print(dist)
que = []
heapq.heappush(que, (0, K))
dist[K] = 0
while que:
    weight, cur_point = heapq.heappop(que)
    # print(cur_point, weight)
    for value, next_point in graph[cur_point]:
        if dist[next_point] == 'INF' or dist[next_point] > weight + value:
            heapq.heappush(que, (weight + value, next_point))
            dist[next_point] = weight + value

for i in range(V):
    print(dist[i + 1])

# 시간 초과 실패
# V, E = map(int, sys.stdin.readline().split())
# K = int(sys.stdin.readline())
# graph = [[] for _ in range(V + 1)]
# dist = ['INF' for _ in range(V + 1)]
# for _ in range(E):
#     u, v, w = map(int, sys.stdin.readline().split())
#     graph[u].append((v, w))
# # print(graph)
# # print(dist)
# que = []
# heapq.heappush(que, (K, 0))
# dist[K] = 0
# while que:
#     cur_point, weight = heapq.heappop(que)
#     for next_point, value in graph[cur_point]:
#         if dist[next_point] == 'INF' or dist[next_point] > weight + value:
#             heapq.heappush(que, (next_point, weight + value))
#             dist[next_point] = weight + value
#
# for i in range(V):
#     print(dist[i + 1])

# 메모리 초과 실패
# V, E = map(int, sys.stdin.readline().split())
# K = int(sys.stdin.readline())
# graph = [[] for _ in range(V + 1)]
# # print(graph)
# for _ in range(E):
#     u, v, w = map(int, sys.stdin.readline().split())
#     graph[u].append((v, w))
#     # heapq.heappush(graph[v][u], w)
# print(graph)
# # print(graph[K])
#
# que = deque()
# result = [-1 for _ in range(V + 1)]
# que.append((K, 0))
# result[K] = 0
# # print(result)
# while que:
#     cur_point, weight = que.popleft()
#     if result[cur_point] == -1 or result[cur_point] >= weight: result[cur_point] = weight
#     for idx, value in graph[cur_point]:
#         if result[idx] == -1 or result[idx] >= weight + value: que.append((idx, weight + value))
#     # print(result)
#
# for i in range(V):
#     if result[i + 1] != -1:
#         print(result[i + 1])
#     else:
#         print('INF')