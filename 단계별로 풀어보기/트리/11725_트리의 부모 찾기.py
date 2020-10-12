# 루트가 1인 트리가 주어질 때, 각 노드의 부모를 구하는 문제
# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
#
# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
#
# 예제 입력 1
# 7
# 1 6
# 6 3
# 3 5
# 4 1
# 2 4
# 4 7
# 예제 출력 1
# 4
# 6
# 1
# 3
# 1
# 4
# 예제 입력 2
# 12
# 1 2
# 1 3
# 2 4
# 3 5
# 3 6
# 4 7
# 4 8
# 5 9
# 5 10
# 6 11
# 6 12
# 예제 출력 2
# 1
# 1
# 2
# 3
# 3
# 4
# 4
# 5
# 5
# 6
# 6
import sys

sys.setrecursionlimit(10 ** 9)
N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    node1, node2 = map(int, sys.stdin.readline()[:-1].split())
    tree[node1].append(node2)
    tree[node2].append(node1)

# print(tree)
parent = [0 for _ in range(N + 1)]
parent[1] = 1


def dfs(cur_point):
    for next_point in tree[cur_point]:
        if parent[next_point] != 0: continue
        parent[next_point] = cur_point
        dfs(next_point)


dfs(1)
for p in parent[2:]:
    print(p)

#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#
#     def __str__(self):
#         return str(self.data)
#
#     def add_child(self, child_node):
#         self.children.append(child_node)
#
#
# class Tree:
#     def __init__(self):
#         self.root = None
#
#     def make_root(self, node):
#         self.root = node
#
#     def make_node(self, parent_node, child_node):
#         parent_node.add_child(child_node)
#
#
# t = Tree()
# t.make_root(Node(1))
# for _ in range(int(sys.stdin.readline())):
#     n1, n2 = map(int, sys.stdin.readline()[:-1].split(' '))
#     t.make_node(Node(n1), Node(n2))