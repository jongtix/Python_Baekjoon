# 분할 정복으로 행렬의 거듭제곱을 빠르게 계산하는 문제
# 문제
# 크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.
#
# 입력
# 첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)
#
# 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.
#
# 출력
# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
#
# 예제 입력 1
# 2 5
# 1 2
# 3 4
# 예제 출력 1
# 69 558
# 337 406
# 예제 입력 2
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 예제 출력 2
# 468 576 684
# 62 305 548
# 656 34 412
# 예제 입력 3
# 5 10
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 1 0 0 0 1
# 예제 출력 3
# 512 0 0 0 512
# 512 0 0 0 512
# 512 0 0 0 512
# 512 0 0 0 512
# 512 0 0 0 512
import sys


def solution(A, B):
    if B == 1:
        result = []
        for a in A:
            temp = []
            for n in a:
                temp.append(n % 1000)
            result.append(temp)
        return result
    elif B % 2 == 0:
        result = solution(A, B // 2)
        return calculate(result, result)
    elif B % 2 == 1:
        result = solution(A, B // 2)
        return calculate(calculate(result, result), A)


def calculate(A, _A):
    result_list = []
    for i in range(N):
        temp = []
        for j in range(N):
            result = 0
            for k in range(N):
                # print(i, j, k)
                result += A[i][k] * _A[k][j]
            temp.append(result % 1000)
        result_list.append(temp)
    return result_list


N, B = map(int, sys.stdin.readline().split(' '))
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split(' '))))
A = solution(A, B)

for l in A:
    for r in l:
        print(r, end=' ')
    print()