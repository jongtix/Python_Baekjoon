# 벨만 포드 알고리즘을 배우는 문제
# 문제
# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다. 각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다. 시간 C가 양수가 아닌 경우가 있다. C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.
#
# 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 도시의 개수 N (1 ≤ N ≤ 500), 버스 노선의 개수 M (1 ≤ M ≤ 6,000)이 주어진다. 둘째 줄부터 M개의 줄에는 버스 노선의 정보 A, B, C (1 ≤ A, B ≤ N, -10,000 ≤ C ≤ 10,000)가 주어진다.
#
# 출력
# 만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면 첫째 줄에 -1을 출력한다. 그렇지 않다면 N-1개 줄에 걸쳐 각 줄에 1번 도시에서 출발해 2번 도시, 3번 도시, ..., N번 도시로 가는 가장 빠른 시간을 순서대로 출력한다. 만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.
#
# 예제 입력 1
# 3 4
# 1 2 4
# 1 3 3
# 2 3 -1
# 3 1 -2
# 예제 출력 1
# 4
# 3
# 예제 입력 2
# 3 4
# 1 2 4
# 1 3 3
# 2 3 -4
# 3 1 -2
# 예제 출력 2
# -1
# 예제 입력 3
# 3 2
# 1 2 4
# 1 2 3
# 예제 출력 3
# 3
# -1
import sys, math, copy

N, M = map(int, sys.stdin.readline()[:-1].split())
visited = []
timer = [math.inf for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, sys.stdin.readline()[:-1].split())
    visited.append((A, B, C))

cur_point = 1
timer[cur_point] = 0
flag = False
check = []
for i in range(N):
    for start, end, next_timer in visited:
        if timer[end] > timer[start] + next_timer:
            # if end == 1 and timer[start] + next_timer < 0: flag = True
            timer[end] = timer[start] + next_timer
    if i == N - 2: check = copy.copy(timer) # 벨만 포드 알고리즘에서 음의 사이클 검증하기
if timer == check: flag = True
# print(timer)
# print(check)

if flag:
    for t in timer[2:]:
        if t == math.inf:
            print(-1)
        else:
            print(t)
else:
    print(-1)


# 시간 초과 실패
# visited = ['' for _ in range(N + 1)]
#
# flag = False
# que = [(0, 1)]
# timer[1] = 0
# visited[1] += '1'
# while que:
#     cur_timer, cur_point = heapq.heappop(que)
#     for next_timer, next_point in graph[cur_point]:
#         if timer[next_point] == 'INF' or timer[next_point] > cur_timer + next_timer:
#             if visited[next_point] and visited[next_point][-2:] == str(cur_point) * 2:
#                 flag = True
#                 break
#             heapq.heappush(que, (cur_timer + next_timer, next_point))
#             timer[next_point] = cur_timer + next_timer
#             visited[next_point] += str(cur_point)
#     if flag: break
# # print(timer, flag)
# if flag:
#     print(-1)
# else:
#     for v in timer[2:]:
#         if v == 'INF':
#             print(-1)
#         else:
#             print(v)