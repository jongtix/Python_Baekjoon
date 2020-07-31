# 메모이제이션으로 N을 1로 바꾸기 위해 주어진 연산을 몇 번 사용하는지 계산하는 문제
# 문제
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
#
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
#
# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
#
# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
#
# 예제 입력 1
# 2
# 예제 출력 1
# 1
# 예제 입력 2
# 10
# 예제 출력 2
# 3
import sys

N = int(sys.stdin.readline())
count = [-1, 0, 1, 1]
for i in range(4, N + 1):
    temp = []
    if i % 2 == 0:
        temp.append(count[i // 2])
    if i % 3 == 0:
        temp.append(count[i // 3])
    # if i % 6 == 0:
    #     temp.append(count[i // 6] + 1)
    temp.append(count[i - 1])
    count.append(min(temp) + 1)

print(count[N])

# 시간 초과 실패
# N = int(sys.stdin.readline())
# count = [0 for _ in range(N + 1)]
# count[2] = 1
# count[3] = 1
#
#
# def find_count(N):
#     if count[N]:
#         return count[N]
#     else:
#         temp = []
#         if N % 2 == 0:
#             temp.append(find_count(N // 2))
#         if N % 3 == 0:
#             temp.append(find_count(N // 3))
#         temp.append(find_count(N - 1))
#         count[N] = min(temp) + 1
#         return count[N]
#
#
# print(find_count(N))