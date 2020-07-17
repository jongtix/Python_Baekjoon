# 규칙을 만족하는 최단 거리를 구하는 문제
# 문제
# 방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다. 또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데, 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.
#
# 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다. 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라. 1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000) 둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데, a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000) 다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)
#
# 출력
# 첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
#
# 예제 입력 1
# 4 6
# 1 2 3
# 2 3 3
# 3 4 1
# 1 3 5
# 2 4 5
# 1 4 4
# 2 3
# 예제 출력 1
# 7
import sys, heapq, copy

N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
total_weight = 0
total_weight2 = 0
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, sys.stdin.readline().split())
list1 = [1, v1, v2, N]
list2 = [1, v2, v1, N]


# 틀렸습니다 실패
# def find_root(start: int, end: int):
#     que = []
#     dist = ['INF' for _ in range(N + 1)]
#     heapq.heappush(que, (0, start))
#     dist[start] = 0
#     while que:
#         weight, cur_point = heapq.heappop(que)
#         for value, next_point in graph[cur_point]:
#             if dist[next_point] == 'INF' or dist[next_point] > weight + value:
#                 heapq.heappush(que, (weight + value, next_point))
#                 dist[next_point] = weight + value
#
#     if dist[end] == 'INF':
#         return 0
#     else:
#         return dist[end]
#
#
# flag1 = False
# flag2 = False
# total_weight = 0
# for i in range(3):
#     result = find_root(list1[i], list1[i + 1])
#     # print(result)
#     if result:
#         total_weight += result
#     else:
#         flag1 = True
#         total_weight = sys.maxsize
#         break
# # print(total_weight)
# print(sys.maxsize + 1)
# total_weight2 = 0
# for i in range(3):
#     result = find_root(list2[i], list2[i + 1])
#     # print(result)
#     if result:
#         total_weight2 += result
#     else:
#         flag2 = True
#         break
# # print(total_weight2)
# print(graph)
# if flag1 and flag2:
#     print(-1)
# else:
#     print(min(total_weight, total_weight2))

# 성공
# flag = True
# flag2 = True
# que = []
# dist = ['INF' for _ in range(N + 1)]
# heapq.heappush(que, (0, 1))
# dist[1] = 0
# # print(used_graph)
# while que:
#     weight, cur_point = heapq.heappop(que)
#     for value, next_point in graph[cur_point]:
#         if dist[next_point] == 'INF' or dist[next_point] > weight + value:
#             heapq.heappush(que, (weight + value, next_point))
#             dist[next_point] = weight + value
#
# if dist[v1] == 'INF':
#     flag = False
# else:
#     total_weight += dist[v1]
#
# if dist[v2] == 'INF':
#     flag2 = False
# else:
#     total_weight2 += dist[v2]
#
# que = []
# dist = ['INF' for _ in range(N + 1)]
# heapq.heappush(que, (0, v1))
# dist[v1] = 0
# # print(used_graph)
# while que:
#     weight, cur_point = heapq.heappop(que)
#     for value, next_point in graph[cur_point]:
#         if dist[next_point] == 'INF' or dist[next_point] > weight + value:
#             heapq.heappush(que, (weight + value, next_point))
#             dist[next_point] = weight + value
#
# if dist[v2] == 'INF':
#     flag = False
# else:
#     total_weight += dist[v2]
#
# que = []
# dist = ['INF' for _ in range(N + 1)]
# heapq.heappush(que, (0, v2))
# dist[v2] = 0
# # print(used_graph)
# while que:
#     weight, cur_point = heapq.heappop(que)
#     for value, next_point in graph[cur_point]:
#         if dist[next_point] == 'INF' or dist[next_point] > weight + value:
#             heapq.heappush(que, (weight + value, next_point))
#             dist[next_point] = weight + value
#
# if dist[N] == 'INF':
#     flag = False
# else:
#     total_weight += dist[N]
#
# que = []
# dist = ['INF' for _ in range(N + 1)]
# heapq.heappush(que, (0, v2))
# dist[v2] = 0
# # print(used_graph)
# while que:
#     weight, cur_point = heapq.heappop(que)
#     for value, next_point in graph[cur_point]:
#         if dist[next_point] == 'INF' or dist[next_point] > weight + value:
#             heapq.heappush(que, (weight + value, next_point))
#             dist[next_point] = weight + value
#
# if dist[v1] == 'INF':
#     flag2 = False
# else:
#     total_weight2 += dist[v1]
#
# que = []
# dist = ['INF' for _ in range(N + 1)]
# heapq.heappush(que, (0, v1))
# dist[v1] = 0
# # print(used_graph)
# while que:
#     weight, cur_point = heapq.heappop(que)
#     for value, next_point in graph[cur_point]:
#         if dist[next_point] == 'INF' or dist[next_point] > weight + value:
#             heapq.heappush(que, (weight + value, next_point))
#             dist[next_point] = weight + value
#
# if dist[N] == 'INF':
#     flag2 = False
# else:
#     total_weight2 += dist[N]
#
# if not flag and not flag2:
#     print(-1)
# else:
#     print(min(total_weight, total_weight2))
