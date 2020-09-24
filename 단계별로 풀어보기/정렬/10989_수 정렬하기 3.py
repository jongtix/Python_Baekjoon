# 수의 범위가 작다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있습니다.
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
# 출처: https://blockdmask.tistory.com/177
# 메모리 초과 실패
import sys


def swap(number_list, low, high):
    temp = number_list[low]
    number_list[low] = number_list[high]
    number_list[high] = temp

#
# def get_pivot(number_list, left, right):
#     pivot = number_list[left]
#     low = left + 1
#     high = left
#
#     while low <= right:
#         while number_list[low] < pivot:
#             high += 1
#             low += 1
#         swap(number_list, low, high)
#     number_list[left] = number_list[low]
#     number_list[low] = pivot
#
#     return low


def quick_sort(number_list, left, right):
    if left >= right: return

    pivot = number_list[left]
    start = left + 1
    end = right

    while start < end:
        while number_list[start] < pivot: start += 1
        while number_list[end] > pivot: end -= 1
        if start < end: swap(number_list, start, end)
    swap(number_list, left, end - 1)

    quick_sort(number_list, left, end - 1)
    quick_sort(number_list, start, right)


N = int(sys.stdin.readline()[:-1])
number_list = []
for _ in range(N):
    number_list.append(int(sys.stdin.readline()[:-1]))
    # print(number_list)

quick_sort(number_list, 0, N - 1)
for number in number_list:
    print(number)

# import sys
#
# count_list = [0 for _ in range(10000)]
# N = int(sys.stdin.readline())
# max_number = 0
# for _ in range(N):
#     number = int(sys.stdin.readline())
#     count_list[number - 1] += 1
#     if max_number < number: max_number = number
#
#
# for number in range(max_number):
#     for _ in range(count_list[number]):
#         print(number + 1)
#     if max_number == number + 1:
#         break



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