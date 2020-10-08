# -*- coding: utf-8 -*-
# 비트마스크 DP에 대해 다루기 전에, 일단 비트마스크부터 다뤄 봅시다.
# 문제
# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
#
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.
# 입력
# 첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
#
# 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.
#
# 출력
# check 연산이 주어질때마다, 결과를 출력한다.
#
# 예제 입력 1
# 26
# add 1
# add 2
# check 1
# check 2
# check 3
# remove 2
# check 1
# check 2
# toggle 3
# check 1
# check 2
# check 3
# check 4
# all
# check 10
# check 20
# toggle 10
# remove 20
# check 10
# check 20
# empty
# check 1
# toggle 1
# check 1
# toggle 1
# check 1
# 예제 출력 1
# 1
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 0
# 1
# 1
# 0
# 0
# 0
# 1
# 0
import sys

# 메모리 초과 실패
# M = int(sys.stdin.readline()[:-1])
# S = set()
# for _ in range(M):
#     temp = sys.stdin.readline().split()
#     command = temp[0]
#     number = 0
#     if len(temp) == 2:
#         number = int(temp[1])
#     if command == 'add':
#         if number not in S:
#             S.add(number)
#     elif command == 'remove':
#         if number in S:
#             S.remove(number)
#     elif command == 'check':
#         if number in S:
#             print(1)
#         else:
#             print(0)
#     elif command == 'toggle':
#         if number in S:
#             S.remove(number)
#         else:
#             S.add(number)
#     elif command == 'all':
#         S = set(num + 1 for num in range(20))
#     elif command == 'empty':
#         S.clear()

# 메모리 초과 실패
# # 출처: https://mygumi.tistory.com/361
# class BitMask:
#     S = 0
#
#     def __init__(self):
#         self.S = 0
#
#     def add(self, x):
#         if bin(self.S & 0b1 << (x - 1)) != bin(0b1 << (x - 1)):
#             self.S = int(bin(self.S | 0b1 << (x - 1)), 2)
#
#     def remove(self, x):
#         if bin(self.S & 0b1 << (x - 1)) != bin(0b0):
#             self.S = int(bin(self.S & ~(0b1 << (x - 1))), 2)
#
#     def check(self, x):
#         if bin(self.S & 0b1 << (x - 1)) != bin(0b0):
#             return '1'
#         else:
#             return '0'
#
#     def toggle(self, x):
#         if bin(self.S & 0b1 << (x - 1)) != bin(0b0):
#             self.remove(x)
#         else:
#             self.add(x)
#
#     def all(self):
#         self.S = 1048575
#
#     def empty(self):
#         self.S = 0
#
#
# M = int(sys.stdin.readline())
# b = BitMask()
# for _ in range(M):
#     temp_order = sys.stdin.readline()[:-1].split()
#     order = temp_order[0]
#     x = 0
#     if len(temp_order) == 2:
#         x = int(temp_order[1])
#     if order == 'add':
#         b.add(x)
#     elif order == 'remove':
#         b.remove(x)
#     elif order == 'check':
#         print(b.check(x))
#     elif order == 'toggle':
#         b.toggle(x)
#     elif order == 'all':
#         b.all()
#     elif order == 'empty':
#         b.empty()


# 메모리 초과 실패
# def convert_to_dec(x):
#     result = 0
#     for n in range(len(x)):
#         if x[n] == '1':
#             result += 2 ** int(len(x) - n - 1)
#     return result
#
#
# class BitMask:
#     S = 0
#
#     def __init__(self):
#         self.S = 0
#
#     def add(self, x):
#         temp = bin(self.S).replace('0b', '')
#         if temp == '0':
#             # self.S = convert_to_dec('1' + '0' * (x - 1))
#             self.S = int('1' + '0' * (x - 1), 2)
#         elif len(temp) < x:
#             # self.S = convert_to_dec('1' + '0' * (x - len(temp) - 1) + temp)
#             self.S = int('1' + '0' * (x - len(temp) - 1) + temp, 2)
#         else:
#             if temp[-x] == '0':
#                 # self.S = convert_to_dec(temp[:x] + '1' + temp[min(x + 1, len(temp) - 1):])
#                 self.S = int(temp[:x] + '1' + temp[min(x + 1, len(temp) - 1):], 2)
#
#     def remove(self, x):
#         temp = bin(self.S).replace('0b', '')
#         if temp[-x] == '1':
#             bin_temp = temp[:-x] + '0' + temp[min(-x + 1, len(temp) - 1):]
#             if bin_temp.startswith('0'): bin_temp = bin_temp[:1]
#             # self.S = convert_to_dec(bin_temp)
#             self.S = int(bin_temp, 2)
#
#     def check(self, x):
#         temp = bin(self.S).replace('0b', '')
#         if len(temp) < x:
#             return '0'
#         else:
#             if temp[-x] == '1':
#                 return '1'
#             else:
#                 return '0'
#
#     def toggle(self, x):
#         temp = bin(self.S).replace('0b', '')
#         if temp[-x] == '1':
#             self.remove(x)
#         else:
#             self.add(x)
#
#     def all(self):
#         self.S = 1048575
#
#     def empty(self):
#         self.S = 0
#
#
# M = int(sys.stdin.readline())
# b = BitMask()
# for _ in range(M):
#     temp_order = sys.stdin.readline()[:-1].split()
#     order = temp_order[0]
#     x = 0
#     if len(temp_order) == 2:
#         x = int(temp_order[1])
#     if order == 'add':
#         b.add(x)
#     elif order == 'remove':
#         b.remove(x)
#     elif order == 'check':
#         print(b.check(x))
#     elif order == 'toggle':
#         b.toggle(x)
#     elif order == 'all':
#         b.all()
#     elif order == 'empty':
#         b.empty()