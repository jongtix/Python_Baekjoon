# 점화식의 값을 특정 상수로 나눈 나머지를 구하는 문제 #
# 문제
# 지원이에게 2진 수열을 가르쳐 주기 위해, 지원이 아버지는 그에게 타일들을 선물해주셨다. 그리고 이 각각의 타일들은 0 또는 1이 쓰여 있는 낱장의 타일들이다.
#
# 어느 날 짓궂은 동주가 지원이의 공부를 방해하기 위해 0이 쓰여진 낱장의 타일들을 붙여서 한 쌍으로 이루어진 00 타일들을 만들었다. 결국 현재 1 하나만으로 이루어진 타일 또는 0타일을 두 개 붙인 한 쌍의 00타일들만이 남게 되었다.
#
# 그러므로 지원이는 타일로 더 이상 크기가 N인 모든 2진 수열을 만들 수 없게 되었다. 예를 들어, N=1일 때 1만 만들 수 있고, N=2일 때는 00, 11을 만들 수 있다. (01, 10은 만들 수 없게 되었다.) 또한 N=4일 때는 0011, 0000, 1001, 1100, 1111 등 총 5개의 2진 수열을 만들 수 있다.
#
# 우리의 목표는 N이 주어졌을 때 지원이가 만들 수 있는 모든 가짓수를 세는 것이다. 단 타일들은 무한히 많은 것으로 가정하자.
#
# 입력
# 첫 번째 줄에 자연수 N이 주어진다.(N ≤ 1,000,000)
#
# 출력
# 첫 번째 줄에 지원이가 만들 수 있는 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.
#
# 예제 입력 1
# 4
# 예제 출력 1
# 5
# def tile(N: int):
#     if N == 1:
#         return 1
#     elif N == 2:
#         return 2
#     else:
#         return tile(N - 1) * 2 - (N - 1) // 2
#
#
# print(tile(int(input())) % 15746)
# def tile(N: float):
#     if N == 1:
#         return 1
#     elif N == 2:
#         return 2
#     else:
#         return tile(N - 1) * 2 - ((N - 1) // 2)
#
#
# print(tile(int(input())) % 15746)
#
# 시간 초과 실패
# import decimal
#
#
# def combination(n, r):
#     s = 0
#     e = 0
#     if r == 0 or n == 0 or n == r: return 1
#     if n - r > r:
#         s = n - r
#         e = r
#     else:
#         s = r
#         e = n - r
#     p = 1
#     for t in range(n, s, -1):
#         p *= t
#     c = 1
#     for t in range(e, 0, -1):
#         c *= t
#     return decimal.Decimal(p) / decimal.Decimal(c)
#
#
# N = int(input())
# sum_cnt = 0
# for nth in range(N // 2 + 1):
#     sum_cnt += combination(N - nth, N - 2 * nth)
# print(int(sum_cnt % 15746))

# 런타임 에러 실패
# N <= 1,000,000
# --> int 범위 초과
# def factorial(n):
#     result = 1
#     for r in range(n):
#         result *= r + 1
#     return result
#
#
# def combination(n, r):
#     return factorial(n) / (factorial(r) * factorial(n - r))
#
#
# def tile(N):
#     if N == 1:
#         return ['1']
#
#     temp_list = tile(N - 1)
#     for nth in range(len(temp_list)):
#         temp_list[nth] = temp_list[nth] + '1'
#
#     if N % 2 == 0:
#         temp_list.append('0' * (N // 2))
#
#     return temp_list
#
#
# def cal(temp_list):
#     sum_cnt = 0
#     n = 0
#     r = 0
#     for l in temp_list:
#         r = l.count('1')
#         n = l.count('0')
#         # print(n, r)
#         # print(compination(n + r, r))
#         sum_cnt += compination(n + r, r)
#     return int(sum_cnt)
#
# # print(tile(4))
# # print(1e6)
# # print(cal(tile(1e6)))
# print(cal(tile(int(input()))) % 15746)


# print(factorial(0))