# 위와 비슷한데 N! 대신 이항계수가 들어간 문제
# 문제
# nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수 n, m(0≤m≤n≤2,000,000,000, n!=0)이 들어온다.
#
# 출력
# 첫째 줄에 0의 개수를 출력한다.
#
# 예제 입력 1
# 25 12
# 예제 출력 1
# 2
import sys

n, m = map(int, sys.stdin.readline()[:-1].split())

cnt_five = 0
i = 1
while n // 5 ** i > 0:
    cnt_five += n // 5 ** i
    i += 1
i = 1
while m // 5 ** i > 0:
    cnt_five -= m // 5 ** i
    i += 1
i = 1
while (n - m) // 5 ** i > 0:
    cnt_five -= (n - m) // 5 ** i
    i += 1

cnt_two = 0
i = 1
while n // 2 ** i > 0:
    cnt_two += n // 2 ** i
    i += 1
i = 1
while m // 2 ** i > 0:
    cnt_two -= m // 2 ** i
    i += 1
i = 1
while (n - m) // 2 ** i > 0:
    cnt_two -= (n - m) // 2 ** i
    i += 1

print(min(cnt_five, cnt_two))
#
# sys.setrecursionlimit(100000)
# # cache = [0 for _ in range(2000000001)]
# #
# #
# # def factorial(n):
# #     if n <= 1:
# #         return 1
# #     else:
# #         if cache[n] != 0: return cache[n]
# #         cache[n] = n * factorial(n - 1)
# #         return cache[n]
#
#
# def combination(n, m):
#     if m == 0 or n == m:
#         return 1
#     else:
#         return combination(n - 1, m - 1) + combination(n - 1, m)
#
#
# n, m = map(int, sys.stdin.readline()[:-1].split())
# # cnt = 0
# # for check in reversed(list(str(combination(n, m)))):
# # # for check in reversed(list(str(factorial(n) // (factorial(m) * factorial(n - m))))):
# #     if check == '0':
# #         cnt += 1
# #     else:
# #         break
# #
# # print(cnt)
# # number = combination(n, m)
# # print(number)
# cnt_five = 0
# i = 1
# while n // 5 ** i > 0:
#     cnt_five += n // 5 ** i
#     i += 1
# i = 1
# while m // 5 ** i > 0:
#     cnt_five -= m // 5 ** i
#     i += 1
# i = 1
# while (n - m) // 5 ** i > 0:
#     cnt_five -= (n - m) // 5 ** i
#     i += 1
#
# cnt_two = 0
# i = 1
# while n // 2 ** i > 0:
#     cnt_two += n // 2 ** i
#     i += 1
# i = 1
# while m // 2 ** i > 0:
#     cnt_two -= m // 2 ** i
#     i += 1
# i = 1
# while (n - m) // 2 ** i > 0:
#     cnt_two -= (n - m) // 2 ** i
#     i += 1
# # while number >= 5:
# #     cnt += number // 5
# #     number %= 5
# print(min(cnt_five, cnt_two))