# -*- coding: utf-8 -*-
# BFS나 DFS로 트리에서 가장 먼 두 점을 찾는 문제
# 문제
# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.
#
# 입력
# 트리가 입력으로 주어진다. 먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2≤V≤100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다. (정점 번호는 1부터 V까지 매겨져 있다고 생각한다)
#
# 먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데, 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.
#
# 출력
# 첫째 줄에 트리의 지름을 출력한다.
#
# 예제 입력 1
# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1
# 예제 출력 1
# 11
import sys

V = int(sys.stdin.readline())
tree = [[] for _ in range(V + 1)]
visited = [0 for _ in range(V + 1)]
for _ in range(V):
    args = list(map(int, sys.stdin.readline()[:-1].split()))
    stand = args[0]
    for i in range(1, len(args) // 2, 2):
        tree[stand].append((args[i], args[i + 1]))

print(tree)


def dfs(cur_point, cur_value, maximum):
    for next_point, next_value in tree[cur_point]:
        if maximum < cur_value + next_value: maximum = cur_value + next_value
        dfs(next_point, cur_value + next_value, maximum)


dfs(1, 0, 0)