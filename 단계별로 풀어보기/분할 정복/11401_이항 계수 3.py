# 분할 정복을 사용한 거듭제곱과 페르마의 소정리를 이용해 곱셈의 역원을 구하는 문제
# 문제
# 자연수 N과 정수 K가 주어졌을 때 이항 계수 (NK)를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 4,000,000, 0 ≤ K ≤ N)
#
# 출력
#  (NK)를 1,000,000,007로 나눈 나머지를 출력한다.
#
# 예제 입력 1
# 5 2
# 예제 출력 1
# 10
import sys

# 런타임 에러 실패
# sys.setrecursionlimit(100000)
# N, K = map(int, sys.stdin.readline()[:-1].split())
# P = 1000000007
# cache = [0 for _ in range(N + 1)]
# inverse = [0 for _ in range(N + 1)]
#
#
# def factorial(N):
#     if N <= 1:
#         return 1
#
#     if cache[N] != 0:
#         return cache[N]
#     cache[N] = (N * factorial(N - 1)) % P
#     return cache[N]
#
#
# def power(x, y):
#     temp = 1
#     while y > 0:
#         if y % 2 != 0:
#             temp = (x * temp) % P
#         x = (x * x) % P
#         y //= 2
#     return temp
#
#
# inverse[N] = power(factorial(N), P - 2)
# for idx in range(N - 1, min(K, N - K) - 1, -1):
#     inverse[idx] = (inverse[idx + 1] * (idx + 1)) % P
#
# if N == K or K == 0:
#     sys.stdout.write('1')
# else:
#     print((((cache[N] * inverse[N - K]) % P) * inverse[K]) % P)

# 런타임 에러 실패
# sys.setrecursionlimit(10000)
# N, K = map(int, sys.stdin.readline()[:-1].split())
# # cache = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
#
#
# def combination(N, K):
#     if N == K or K == 0:
#         return 1
#
#     # if cache[N][K] != 0 or cache[N][N - K]:
#     #     return max(cache[N][K], cache[N][N - K])
#     #
#     # cache[N][K] = (combination(N - 1, K - 1) + combination(N - 1, K)) % 1000000007
#     # cache[N][N - K] = cache[N][K]
#     # return cache[N][K]
#     return (combination(N - 1, K - 1) + combination(N - 1, K)) % 1000000007
#
#
# print(combination(N, K))

# 런타임 에러
# def comb(N, K):
#     # print(N, K)
#     if N == K or K == 0:
#         return 1
#     else:
#         K1, K2 = K, N - K if K >= N - K else N - K
#         return (comb(N - 1, K1) + comb(N - 1, K2)) % 1000000007
#
#
# N, K = map(int, sys.stdin.readline()[:-1].split(' '))
# print(comb(N, K))