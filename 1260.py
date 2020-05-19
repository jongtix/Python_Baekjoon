# DFS와 BFS
# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
#
# 예제 입력 1
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 예제 출력 1
# 1 2 4 3
# 1 2 3 4
# 예제 입력 2
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1
# 예제 출력 2
# 3 1 2 5 4
# 3 1 4 2 5
# 예제 입력 3
# 1000 1 1000
# 999 1000
# 예제 출력 3
# 1000 999
# 1000 999
import queue


def solution(first_args, second_args):
    N = first_args[0] # 정점의 개수
    M = first_args[1] # 간선의 개수
    V = int(first_args[2]) - 1 # 탐색을 시작할 정점의 번호

    a = [[0 for col in range(N)] for row in range(N)]
    for arg in second_args:
        i = arg[0] - 1
        j = arg[1] - 1
        a[i][j] = 1
        a[j][i] = 1

    c = [False for x in range(N)]
    dfs(a, c, V)
    print()
    bfs(a, V)
    print()
    # c2 = [False for x in range(N)]
    # dfs2(a, c2, V)


def bfs(a, v):
    n = len(a)

    que = queue.Queue
    que.put(v)
    print(str(v + 1), end=' ')

    for i in range(n):
        


def dfs(a, c, v):
    n = len(a)
    c[v] = True
    print(str(v + 1), end=' ')

    for i in range(0, n):
        if a[v][i] == 1 and not c[i]:
            dfs(a, c, i)


def dfs2(a, c, v):
    stack = []
    n = len(a)

    stack.append(v)
    c[v] = True
    print(str(v + 1), end=' ')

    while stack:
        vv = stack[len(stack) - 1]

        flag = False

        for i in range(0, n):
            if a[vv][i] == 1 and not c[i]:
                stack.append(i)
                print(str(i + 1), end=' ')

                c[i] = True
                flag = True
                break

        if not flag: stack.pop()

first_args = [4, 5, 1]
second_args = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]
first_args = [5, 5, 3]
second_args = [[5, 4], [5, 2], [1, 2], [3, 4], [3, 1]]
solution(first_args, second_args)