# 행렬의 거듭제곱을 계산하기 전에 먼저 풀어야 할 문제
# 문제
# N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 행렬 A의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 순서대로 주어진다. 그 다음 줄에는 행렬 B의 크기 M과 K가 주어진다. 이어서 M개의 줄에 행렬 B의 원소 K개가 차례대로 주어진다. N과 M, 그리고 K는 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
#
# 출력
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 곱한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.
#
# 예제 입력 1
# 3 2
# 1 2
# 3 4
# 5 6
# 2 3
# -1 -2 0
# 0 0 3
# 예제 출력 1
# -1 -2 6
# -3 -6 12
# -5 -10 18
import sys


def calculate(first_list, second_list):
    result_list = []
    for i in range(N):
        temp = []
        for j in range(K):
            result = 0
            for k in range(M):
                # print(i, j, k)
                result += first_list[i][k] * second_list[k][j]
            temp.append(result)
        result_list.append(temp)
    return result_list


first_list = []
second_list = []
N, M = map(int, sys.stdin.readline().split(' '))
for _ in range(N):
    first_list.append(list(map(int, sys.stdin.readline().split(' '))))

M, K = map(int, sys.stdin.readline().split(' '))
for _ in range(M):
    second_list.append(list(map(int, sys.stdin.readline().split(' '))))
result = calculate(first_list, second_list)
for l in result:
    for n in l:
        print(str(n), end=' ')
    print()