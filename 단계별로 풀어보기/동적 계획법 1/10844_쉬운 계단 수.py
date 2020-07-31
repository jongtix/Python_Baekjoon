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