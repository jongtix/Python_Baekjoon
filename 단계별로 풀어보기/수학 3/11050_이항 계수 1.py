# N개의 물건 중 순서를 고려하지 않고 K개를 고르는 경우의 수, 이항 계수를 구하는 문제
# 문제
# 자연수 N과 정수 K가 주어졌을 때 이항 계수 (NK)를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)
#
# 출력
# (NK)를 출력한다.
#
# 예제 입력 1
# 5 2
# 예제 출력 1
# 10
import sys

# 틀렸습니다 실패
# cache = [0 for _ in range(11)]
# N, K = map(int, sys.stdin.readline()[:-1].split())
#
#
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         if cache[n] != 0: return cache[n]
#         cache[n] = n * factorial(n - 1)
#         return cache[n]
#
#
# print(factorial(N) // (factorial(K) * factorial(N - K)))

# 틀렸습니다 실패
# N, K = map(int, sys.stdin.readline()[:-1].split())
#
#
# def solution(n, k):
#     if k == 0 or n == k:
#         return 1
#     else:
#         return solution(n - 1, k - 1) + solution(n - 1, k)
#
#
# print(solution(N, K))

# 틀렸습니다 실패
# N, K = map(int, sys.stdin.readline()[:-1].split())
#
# parent = 1
# child = 1
#
# for i in range(1, N + 1):
#     parent *= i
#
# for j in range(1, K + 1):
#     child *= j
# for k in range(1, N - K + 1):
#     child *= k
#
# print(int(parent / child))