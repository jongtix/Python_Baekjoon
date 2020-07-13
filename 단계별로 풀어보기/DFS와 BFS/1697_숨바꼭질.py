# 또 다른 BFS 최단거리 연습문제
# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
#
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.
#
# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
#
# 예제 입력 1
# 5 17
# 예제 출력 1
# 4
import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())
maximum = max(N, K) * 2
visited = [0 for _ in range(maximum + 1)]
que = deque()
que.append((N, 0))

if not N == K:
    while que:
        # print(que)
        cur_point, time = map(int, que.popleft())
        if not visited[cur_point] or visited[cur_point] > time: visited[cur_point] = time
        next_points = [cur_point + 1, cur_point - 1, cur_point * 2]
        for next_point in next_points:
            if 0 <= next_point <= maximum and (not visited[next_point] or visited[next_point] > time + 1): que.append((next_point, time + 1))

print(visited[K])


# 런타임 에러 실패
# sys.setrecursionlimit(100000)
# N, K = map(int, sys.stdin.readline().split())
# maximum = max(N * 2, K * 2)
# visited = [0 for _ in range(maximum + 1)]
#
#
# def bfs(visited, point, time):
#     visited[point] = time
#     if point == K: return
#     if 0 <= point + 1 <= maximum and (not visited[point + 1] or visited[point + 1] > time + 1): bfs(visited, point + 1, time + 1)
#     if 0 <= point - 1 <= maximum and (not visited[point - 1] or visited[point - 1] > time + 1): bfs(visited, point - 1, time + 1)
#     if 0 <= point * 2 <= maximum and (not visited[point * 2] or visited[point * 2] > time + 1): bfs(visited, point * 2, time + 1)
#
#
# bfs(visited, N, 0)
# print(visited[K])