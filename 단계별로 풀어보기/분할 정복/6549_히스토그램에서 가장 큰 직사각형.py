# -*- coding: utf-8 -*-
# 히스토그램에서 가장 큰 직사각형을 찾는 문제. 분할 정복으로도 풀 수 있고, 스택으로 풀 수도 있습니다.
# 문제
# 히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다. 예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인 직사각형으로 이루어진 히스토그램이다.
#
#
#
# 히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.
#
# 입력
# 입력은 테스트 케이스 여러 개로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, 직사각형의 수 n이 가장 처음으로 주어진다. (1 ≤ n ≤ 100,000) 그 다음 n개의 정수 h1, ..., hn (0 ≤ hi ≤ 1,000,000,000)가 주어진다. 이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 왼쪽부터 오른쪽까지 순서대로 주어진다. 모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.
#
# 예제 입력 1
# 7 2 1 4 5 1 3 3
# 4 1000 1000 1000 1000
# 0
# 예제 출력 1
# 8
# 4000
import sys

# 메모리 초과 실패
# def find_square(h_list):
#     global maximum
#     h_m = min(h_list)
#     m = h_list.index(h_m)
#     if m > 0:
#         find_square(h_list[:m])
#     if m < len(h_list) - 1:
#         find_square(h_list[m + 1:])
#     if maximum < h_m * len(h_list):
#         maximum = h_m * len(h_list)
#
#
# while True:
#     args = list(map(int, sys.stdin.readline().split()))
#     if args == [0]:
#         break
#     maximum = 0
#     find_square(args[1:])
#     print(maximum)

# 시간 초과 실패
# def find_square(n, k, h_list, maximum):
#     if k > n:
#         return maximum
#
#     for start in range(len(h_list) - k + 1):
#         temp = min(h_list[start:start + k]) * k
#         if maximum < temp: maximum = temp
#
#     return find_square(n, k + 1, h_list, maximum)
#
#
# while True:
#     args = list(map(int, sys.stdin.readline().split()))
#     if args == [0]:
#         break
#     print(find_square(args[0], 1, args[1:], 0))
