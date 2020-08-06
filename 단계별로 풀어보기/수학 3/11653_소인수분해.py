# 소인수분해를 배우는 문제
# 문제
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
#
# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다.
#
# 예제 입력 1
# 72
# 예제 출력 1
# 2
# 2
# 2
# 3
# 3
# 예제 입력 2
# 3
# 예제 출력 2
# 3
# 예제 입력 3
# 6
# 예제 출력 3
# 2
# 3
# 예제 입력 4
# 2
# 예제 출력 4
# 2
# 예제 입력 5
# 9991
# 예제 출력 5
# 97
# 103
import sys

N = int(sys.stdin.readline())
decimal = 1
while N > 1:
    decimal += 1
    while N % decimal == 0:
        print(decimal)
        N //= decimal


# 시간 초과 실패
# def check_decimal(number):
#     for case in range(2, int(number ** 1/2)):
#         if number % case == 0: return False
#     return True
#
#
# N = int(sys.stdin.readline())
# result = []
# for decimal in range(2, N + 1):
#     if check_decimal(decimal):
#         while N % decimal == 0:
#             result.append(decimal)
#             N //= decimal
#
# for number in result:
#     print(number)

# 시간 초과 실패
# def check_decimal(number):
#     for case in range(2, int(number ** 1/2)):
#         if number % case == 0: return False
#     return True
#
#
# def find_decimal(number):
#     decimal_list = []
#     for case in range(2, number + 1):
#         if check_decimal(case):
#             decimal_list.append(case)
#     return decimal_list
#
#
# N = int(sys.stdin.readline())
# decimal_list = find_decimal(N)
# result = []
# for decimal in decimal_list:
#     while N % decimal == 0:
#         result.append(decimal)
#         N //= decimal
#
# for number in result:
#     print(number)