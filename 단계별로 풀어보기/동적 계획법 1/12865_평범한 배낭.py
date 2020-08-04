# 대표적인 DP 문제 중 하나인 "냅색 문제"
# 문제
# 이 문제는 아주 평범한 배낭에 관한 문제이다.
#
# 한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.
#
# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 아직 행군을 해본 적이 없는 준서는 최대 K무게까지의 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.
#
# 입력
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
#
# 입력으로 주어지는 모든 수는 정수이다.
#
# 출력
# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.
#
# 예제 입력 1
# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
# 예제 출력 1
# 14
import sys

# 틀렸습니다 실패
N, K = map(int, sys.stdin.readline()[:-1].split())
things = []
for _ in range(N):
    W, V = map(int, sys.stdin.readline()[:-1].split())
    things.append([W, V])

things.sort()
print(things)
values = [0 for _ in range(100000 + 1)]

for idx in range(N):
    values[things[idx][0]] = max(values[things[idx][0]], things[idx][1])
    for jdx in range(idx + 1, N):
        if things[idx][0] + things[jdx][0] <= K:
            values[things[idx][0] + things[jdx][0]] = max(values[things[idx][0] + things[jdx][0]], things[idx][1] + things[jdx][1])

# print(values)
print(max(values))

# 메모리 초과 실패
# N, K = map(int, sys.stdin.readline()[:-1].split())
# things = []
# for _ in range(N):
#     things.append(tuple(map(int, sys.stdin.readline()[:-1].split())))
#
# things.sort()
#
# values = []
#
# for thing in things:
#     for value in values:
#         if thing[0] + value[0] <= K:
#             values.append([thing[0] + value[0], thing[1] + value[1]])
#     values.append(list(thing))
#
# print(max(values, key=lambda x: x[1])[1])

# 틀렸습니다 실패
# N, K = map(int, sys.stdin.readline()[:-1].split())
# things = []
# for _ in range(N):
#     things.append(tuple(map(int, sys.stdin.readline()[:-1].split())))
#
# things.sort(reverse=True, key=lambda x: x[1])
# value = [0 for _ in range(N + 1)]
# weight = 0
# for idx in range(1, N + 1):
#     if weight + things[idx - 1][0] <= K:
#         weight += things[idx - 1][0]
#         value[idx] = value[idx - 1] + things[idx - 1][1]
#     else:
#         weight = things[idx - 1][0]
#         value[idx] = things[idx - 1][1]
#
# print(max(value))