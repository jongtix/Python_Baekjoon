# 최대공약수와 최소공배수를 구하는 문제
# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
#
# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
#
# 예제 입력 1
# 24 18
# 예제 출력 1
# 6
# 72
import sys

# 유클리드 호제법
# 2개의 자연수 또는 정식(整式)의 최대공약수를 구하는 알고리즘의 하나이다.
# 호제법이란 말은 두 수가 서로(互) 상대방 수를 나누어(除)서 결국 원하는 수를 얻는 알고리즘을 나타낸다.
# 2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
# 이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.
x, y = map(int, sys.stdin.readline()[:-1].split())


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(min(x, y), max(x, y) % min(x, y))


result = gcd(x, y)
print(result)
print((x * y) // result)


# x, y = map(int, sys.stdin.readline()[:-1].split())
# decimal = 1
# x_decimal = [1]
# while x > 1:
#     decimal += 1
#     while x % decimal == 0:
#         x_decimal.append(decimal)
#         x //= decimal
#
# decimal = 1
# y_decimal = [1]
# while y > 1:
#     decimal += 1
#     while y % decimal == 0:
#         y_decimal.append(decimal)
#         y //= decimal
#
# common_factor = 1
# common_multiple = 1
# for number in list(set(x_decimal) & set(y_decimal)):
#     common_factor *= number ** min(x_decimal.count(number), y_decimal.count(number))
# for number in list(set(x_decimal + y_decimal)):
#     common_multiple *= number ** max(x_decimal.count(number), y_decimal.count(number))
#
# print(common_factor)
# print(common_multiple)

# 시간 초과 실패
# x, y = map(int, sys.stdin.readline()[:-1].split())
#
#
# def find_common_factor(x, y):
#     factor_x = []
#     factor_y = []
#     for factor in range(1, max(x, y) + 1):
#         if x >= factor and x % factor == 0: factor_x.append(factor)
#         if y >= factor and y % factor == 0: factor_y.append(factor)
#     return max(set(factor_x) & set(factor_y))
#
#
# def find_common_multiple(x, y):
#     multiple_x = [x]
#     multiple_y = [y]
#     idx = 1
#     result = 0
#     while True:
#         idx += 1
#         if x * idx in multiple_y:
#             result = x * idx
#             break
#         if y * idx in multiple_x:
#             result = y * idx
#             break
#         multiple_x.append(x * idx)
#         multiple_y.append(y * idx)
#     return result
#
#
# print(find_common_factor(x, y))
# print(find_common_multiple(x, y))
