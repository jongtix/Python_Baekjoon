# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
#
# 예제 입력 1
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7
# 예제 출력 1
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# 7

#############
### 미해결 ###
#############

import sys

count_list = [0 for _ in range(10000)]
N = int(sys.stdin.readline())
max_number = 0
for _ in range(N):
    number = int(sys.stdin.readline())
    count_list[number - 1] += 1
    if max_number < number: max_number = number


for number in range(max_number):
    for _ in range(count_list[number]):
        print(number + 1)
    if max_number == number + 1:
        break



# number_list = []
# count_list = [0 for _ in range(10000)]
# N = int(input())
# for _ in range(N):
#     NN = int(input())
#     number_list.append(NN)
#     count_list[NN - 1] += 1
# for idx, count in enumerate(count_list):
#     if idx != 0:
#         count_list[idx] = count_list[idx - 1] + count
# result = [None for _ in range(N)]
# for number in reversed(number_list):
#     # print(count_list[number - 1])
#     result[count_list[number - 1] - 1] = number
#     count_list[number - 1] -= 1
# for r in result:
#     print(r)


# number_list = [int(input()) for _ in range(int(input()))]
# result = []
# for number in set(number_list):
#     for _ in range(number_list.count(number)):
#         result.append(number)
# for number in result:
#     print(number)