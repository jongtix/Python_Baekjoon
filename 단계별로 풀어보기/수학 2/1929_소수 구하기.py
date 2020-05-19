# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.
#
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
#
# 예제 입력 1
# 3 16
# 예제 출력 1
# 3
# 5
# 7
# 11
# 13


M, N = input().split()
M = int(M)
N = int(N)
if M <= 1: M = 2
if N <= 1: N = 2
num_list = {x : False for x in range(M, N + 1)}

for i in range(2, N + 1):
    if i in num_list.keys() and num_list[i]: pass
    for j in range(2 * i, N + 1, i):
        if j in num_list.keys(): num_list[j] = True

# for i in range(2, N + 1):
#     if i in num_list.keys() and num_list[i]: pass
#     for j in range(2 * i, N + 1, i):
#         if i != j and j % i == 0:
#             num_list[j] = True
#
#
for number, check in num_list.items():
    if not check: print(int(number))