# -*- coding: utf-8 -*-
# 가능한 한 많은 구간을 선택하는 문제
# 문제
# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
#
# 입력
# 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.
#
# 출력
# 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.
#
# 예제 입력 1
# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14
# 예제 출력 1
# 4
import sys

N = int(sys.stdin.readline())
conferences = []
count = 0

for _ in range(N):
    start, end = map(int, sys.stdin.readline()[:-1].split())
    conferences.append([start, end])

conferences.sort(key=lambda x: (x[1], x[0]))
end_time = 0
for conference in conferences:
    if conference[0] >= end_time:
        end_time = conference[1]
        count += 1

print(count)

# 틀렸습니다 실패
# N = int(sys.stdin.readline())
# conferences = []
# count = 0
#
# for _ in range(N):
#     start, end = map(int, sys.stdin.readline()[:-1].split())
#     if start == end: count += 1
#     else:
#         conferences.append([start, end])
#
# conferences.sort(key=lambda x: x[0])
# conferences.sort(key=lambda x: x[1])
# end_time = 0
# for conference in conferences:
#     if conference[0] >= end_time:
#         end_time = conference[1]
#         count += 1
#
# print(count)

# 틀렸습니다 실패
# N = int(sys.stdin.readline())
# maximum_time = [0, 0]
# count = 0
#
# for _ in range(N):
#     start, end = map(int, sys.stdin.readline()[:-1].split())
#     if end - start == 0: count += 1
#     else:
#         if maximum_time[1] <= start:
#             maximum_time = [start, end]
#             count += 1
#
# print(count)

# 시간 초과 실패
# N = int(sys.stdin.readline())
#
# conferences = []
# schedules = []
#
# count = 0
# for _ in range(N):
#     start, end = map(int, sys.stdin.readline()[:-1].split())
#     if end - start == 0: count += 1
#     else:
#         flag = False
#         for schedule in schedules:
#             if bool(set(range(start, end)) & set(range(schedule[0], schedule[1]))): flag = True
#         if not flag:
#             schedules.append([start, end])
#             count += 1
# # print(schedules)
# print(count)

# conferences.sort()
#
# for conference in conferences:
#     start_time, end_time = conference
#     if True not in schedule[start_time:end_time]:
#         for idx in range(start_time, end_time):
#             schedule[idx] = True
#         count += 1
#
# print(count)

# 틀렸습니다 실패
# N = int(sys.stdin.readline())
#
# conferences = []
# latest_time = 0
#
# for _ in range(N):
#     start, end = map(int, sys.stdin.readline()[:-1].split())
#     if latest_time < end: latest_time = end
#     conferences.append([end - start, start, end])
#
# timer = [False for _ in range(latest_time + 1)]
# conferences.sort()
# count = 0
# result = []
# for conference in conferences:
#     gap, start, end = conference
#     if True not in timer[start: end]:
#         for idx in range(start, end):
#             timer[idx] = True
#         result.append((start, end))
#         count += 1
#
# print(result)
# print(count)