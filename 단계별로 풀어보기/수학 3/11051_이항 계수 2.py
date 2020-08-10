# 더 넓은 범위의 이항 계수를 동적 계획법으로 구하는 문제
# 문제
# 자연수 N과 정수 K가 주어졌을 때 이항 계수 (NK)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ K ≤ N)
#
# 출력
#  (NK)를 10,007로 나눈 나머지를 출력한다.
#
# 예제 입력 1
# 5 2
# 예제 출력 1
# 10
import sys

sys.setrecursionlimit(10000)
cache = [0 for _ in range(1001)]


def factorial(N):
    if N <= 1:
        return 1
    else:
        if cache[N] != 0: return cache[N]
        cache[N] = N * factorial(N - 1)
        return cache[N]


N, K = map(int, sys.stdin.readline()[:-1].split())
print(int(factorial(N) // (factorial(K) * factorial(N - K))) % 10007)