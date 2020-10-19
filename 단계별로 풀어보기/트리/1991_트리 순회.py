# 이진 트리에 대해 알아보고, 이진 트리를 순회해 봅시다.
# 문제
# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
#
#
#
# 예를 들어 위와 같은 이진 트리가 입력되면,
#
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.
#
# 입력
# 첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현된다.
#
# 출력
# 첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
#
# 예제 입력 1
# 7
# A B C
# B D .
# C E F
# E . .
# F . G
# D . .
# G . .
# 예제 출력 1
# ABDCEFG
# DBAECFG
# DBEGFCA
import sys
# 런다임 에러 실패
# sys.setrecursionlimit(10 ** 5)
N = int(sys.stdin.readline()[:-1])
tree = {}
for _ in range(N):
    root, left, right = sys.stdin.readline()[:-1].split()
    tree[root] = [left, right]

# print(tree)


def preorder_traverse(root):
    print(root, end='')
    left = tree[root][0]
    right = tree[root][1]
    if left != '.': preorder_traverse(left)
    if right != '.': preorder_traverse(right)


def inorder_traverse(root):
    left = tree[root][0]
    right = tree[root][1]
    if left != '.': inorder_traverse(left)
    print(root, end='')
    if right != '.': inorder_traverse(right)


def postorder_traverse(root):
    left = tree[root][0]
    right = tree[root][1]
    if left != '.': postorder_traverse(left)
    if right != '.': postorder_traverse(right)
    print(root, end='')


preorder_traverse('A')
print()
inorder_traverse('A')
print()
postorder_traverse('A')

# 메모리 초과 실패
# sys.setrecursionlimit(200000)
# N = int(sys.stdin.readline()[:-1])
# upper_string = string.ascii_uppercase + '.'
# tree = [[-1, -1] for _ in range(N)]
# for _ in range(N):
#     root, left, right = sys.stdin.readline()[:-1].split()
#     root = upper_string.index(root)
#     left = upper_string.index(left) != 26 and upper_string.index(left) or -1
#     right = upper_string.index(right) != 26 and upper_string.index(right) or -1
#     tree[root][0] = left
#     tree[root][1] = right
#
# # print(tree)
#
#
# def preorder_traverse(root, preorder):
#     preorder += upper_string[root]
#     left = tree[root][0]
#     right = tree[root][1]
#     if left > -1: preorder += preorder_traverse(left, '')
#     if right > -1: preorder += preorder_traverse(right, '')
#     return preorder
#
#
# def inorder_traverse(root, inorder):
#     left = tree[root][0]
#     right = tree[root][1]
#     if left > -1: inorder += inorder_traverse(left, '')
#     inorder += upper_string[root]
#     if right > -1: inorder += inorder_traverse(right, '')
#     return inorder
#
#
# def postorder_traverse(root, postorder):
#     left = tree[root][0]
#     right = tree[root][1]
#     if left > -1: postorder += postorder_traverse(left, '')
#     if right > -1: postorder += postorder_traverse(right, '')
#     postorder += upper_string[root]
#     return postorder
#
#
# print(preorder_traverse(0, ''))
# print(inorder_traverse(0, ''))
# print(postorder_traverse(0, ''))