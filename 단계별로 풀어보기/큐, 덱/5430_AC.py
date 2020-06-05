# 덱을 활용하여 시간복잡도를 향상시키는 문제
# 문제
# 선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
#
# 함수 R은 배열에 있는 숫자의 순서를 뒤집는 함수이고, D는 첫 번째 숫자를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
#
# 함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 숫자를 버리는 함수이다.
#
# 배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.
#
# 각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
#
# 다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)
#
# 다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 수가 주어진다. (1 ≤ xi ≤ 100)
#
# 전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.
#
# 출력
# 각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.
#
# 예제 입력 1
# 4
# RDD
# 4
# [1,2,3,4]
# DD
# 1
# [42]
# RRD
# 6
# [1,1,2,3,5,8]
# D
# 0
# []
# 예제 출력 1
# [2,1]
# error
# [1,2,3,5,8]
# error
from collections import deque
import sys

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline()[:-1]
    # idx = 0
    # pre_command = ''
    # while len(command) > 1 and idx < len(command):
    #     if pre_command == 'R' and command[idx] == 'R':
    #         command = command[:idx - 1] + command[idx + 1:]
    #         pre_command = ''
    #         idx -= 1
    #     else:
    #         pre_command = command[idx]
    #         idx += 1
    # if idx < len(command) and pre_command == 'R' and command[idx] == 'R':
    #     command = command[:idx - 1]

    n = int(sys.stdin.readline())
    AC_list = []
    list_num = sys.stdin.readline()[1:-2]
    if len(list_num) > 0:
        AC_list = list(map(int, list_num.split(',')))
    que = deque(AC_list)

    left, right = 0, n - 1
    stand = 'left'
    flag = True
    for com in command:
        if com == 'R':
            if stand == 'left':
                stand = 'right'
            else: stand = 'left'
        elif com == 'D':
            if left <= right:
                if stand == 'left':
                    left += 1
                else: right -= 1
            else:
                print('error')
                flag = False
                break
    # print(stand, left, right)
    if flag:
        print('[', end='')
        temp_list = []
        if stand == 'left':
            temp_list = list(que)[left:right + 1]
            # print(list(que)[left:right + 1])
        else:
            if left == 0:
                temp_list = list(que)[right::-1]
                # print(list(que)[right::-1])
            else:
                temp_list = list(que)[right:left - 1:-1]
                # print(list(que)[right:left - 1:-1])
        for idx in range(len(temp_list)):
            print(temp_list[idx], end='')
            if idx != len(temp_list) - 1:
                print(',', end='')
        print(']')


# 시간 초과 실패
# for _ in range(int(sys.stdin.readline())):
#     command = sys.stdin.readline()[:-1]
#     n = int(sys.stdin.readline())
#     AC_list = []
#     list_num = sys.stdin.readline()[1:-2]
#     if len(list_num) > 0:
#         AC_list = list(map(int, list_num.split(',')))
#     que = deque(AC_list)
#     flag = True
#     idx = 0
#     while idx < len(command):
#         com = command[idx]
#         if idx + 1 < len(command) and com == 'R' and command[idx + 1] == 'R':
#             idx += 1
#             continue
#
#         if com == 'R':
#             que.reverse()
#         elif com == 'D':
#             if que:
#                 que.popleft()
#             else:
#                 print('error')
#                 flag = False
#                 break
#         idx += 1
#     if flag:
#         print(list(que))