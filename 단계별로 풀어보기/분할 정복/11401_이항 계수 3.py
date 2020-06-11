# 분할 정복을 사용한 거듭제곱과 페르마의 소정리를 이용해 곱셈의 역원을 구하는 문제
# 문제
# 자연수 과 정수 가 주어졌을 때 이항 계수 를 1,000,000,007로 나눈 나머지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 과 가 주어진다. (1 ≤  ≤ 4,000,000, 0 ≤  ≤ )
#
# 출력
#  를 1,000,000,007로 나눈 나머지를 출력한다.
#
# 예제 입력 1
# 5 2
# 예제 출력 1
# 10
import sys

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