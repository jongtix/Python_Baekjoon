# DFS와 BFS를 다루는 문제
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
import sys
from collections import deque


N, M, V = map(int, sys.stdin.readline().split(' '))

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split(' '))
    graph[n1].append(n2)
    graph[n2].append(n1)
# print(graph)


bfs_result = []
visit = [False for _ in range(N + 1)]


def bfs(start, graph):
    que = deque()
    que.append(start)
    while que:
        stand = que.popleft()
        if not visit[stand]:
            bfs_result.append(stand)
            visit[stand] = True
        graph[stand].sort()
        # print(stand, graph[stand])
        for i in graph[stand]:
            if not visit[i]:
                que.append(i)


bfs(V, graph)

dfs_result = []


def dfs(start, graph):
    stack = deque()
    stack.append(start)
    while stack:
        stand = stack.pop()
        if not visit[stand]:
            dfs_result.append(stand)
            visit[stand] = True
        # print(stand, graph[stand])
        graph[stand].reverse()
        # print(stand, graph[stand])
        for i in graph[stand]:
            if not visit[i]:
                stack.append(i)


visit = [False for _ in range(N + 1)]
dfs(V, graph)
for i in range(len(dfs_result)):
    print(str(dfs_result[i]), end='')
    if i != len(dfs_result) - 1: print(' ', end='')
print()

for i in range(len(bfs_result)):
    print(str(bfs_result[i]), end='')
    if i != len(bfs_result) - 1: print(' ', end='')

# import heapq, queue
#
# first = input()
#
# s = first.split()
# N = int(s[0])
# M = int(s[1])
# V = s[2]
#
# graph = {}
#
# for i in range(M):
#     next = input().split()
#     p = next[0]
#     c = next[1]
#     if p in graph.keys():
#         child = graph[p]
#         heapq.heappush(child, c)
#         graph[p] = child
#     else:
#         graph[p] = [c]
#
#     if c in graph.keys():
#         child = graph[c]
#         heapq.heappush(child, p)
#         graph[c] = child
#     else:
#         graph[c] = [p]
#
#
# def dfs(V):
#     stack = list()
#     visit = set()
#     answer = list()
#     stack.append(V)
#     while stack:
#         value = stack.pop()
#         l = graph[value]
#         l.sort(reverse=True)
#         for v in l:
#             if v not in visit:
#                 stack.append(v)
#         if value not in visit:
#             answer.append(value)
#         visit.add(value)
#
#     return ' '.join(answer)
#
#
# print(dfs(V))
#
#
# def bfs(V):
#     que = queue.Queue()
#     visit = set()
#     answer = list()
#     que.put(V)
#     while not que.empty():
#         value = que.get()
#         l = graph[value]
#         l.sort(reverse=False)
#         for v in l:
#             if v not in visit:
#                 que.put(v)
#         if value not in visit:
#             answer.append(value)
#         visit.add(value)
#
#     return ' '.join(answer)
#
# print(bfs(V))