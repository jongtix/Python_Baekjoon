# 동적 계획법을 이용해 계단 수를 구하는 문제
# 문제
# 45656이란 수를 보자.
#
# 이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.
#
# 세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
#
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)
#
# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
#
# 예제 입력 1
# 1
# 예제 출력 1
# 9
# 예제 입력 2
# 2
# 예제 출력 2
# 17
import sys

append_number = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7, 9], 9: [8]}
# append_number = [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
count_number = [1 for _ in range(10)] # 0 ~ 9 까지 숫자의 개수
count_number[0] = 0
N = int(sys.stdin.readline())
for i in range(1, N):
    temp = [0 for _ in range(10)]
    for idx in range(10):
        for number in append_number[idx]:
            temp[number] += count_number[idx] * 1
    count_number = temp
# print(count_number)
print(sum(count_number) % 1000000000)

# 틀렸습니다 실패
# append_number = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7, 9], 9: [8]}
# # append_number = [1, 2, 2, 2, 2, 2, 2, 2, 2, 1]
# count_number = [1 for _ in range(10)] # 0 ~ 9 까지 숫자의 개수
# count_number[0] = 0
# N = int(sys.stdin.readline())
# for i in range(1, N):
#     temp = [0 for _ in range(10)]
#     for idx in range(10):
#         for number in append_number[idx]:
#             temp[number] += count_number[idx] * 1
#     count_number = temp
# # print(count_number)
# print(sum(count_number))

# 메모리 초과 실패
# N = int(sys.stdin.readline())
# numbers = [i + 1 for i in range(9)]
# for i in range(2, N + 1):
#     temp = []
#     for number in numbers:
#         if int(str(number)[-1]) - 1 >= 0: temp.append(number * 10 + (int(str(number)[-1]) - 1))
#         if int(str(number)[-1]) + 1 < 10: temp.append(number * 10 + (int(str(number)[-1]) + 1))
#     numbers = temp
# print(len(numbers) % 1000000000)