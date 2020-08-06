# 약수의 성질을 활용하는 문제
# 문제
# 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.
#
# 출력
# 첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.
#
# 예제 입력 1
# 2
# 4 2
# 예제 출력 1
# 8
import sys

# 틀렸습니다 실패
# int(sys.stdin.readline()[:-1])
# measures = list(map(int, sys.stdin.readline()[:-1].split()))
# print(min(measures) * max(measures))

# 틀렸습니다 실패
# measure_cnt = int(sys.stdin.readline()[:-1])
# measures = list(map(int, sys.stdin.readline()[:-1].split()))
# minimum = max(measures) * 2
# while True:
#     flag = True
#     cnt = 0
#     for measure in measures:
#         if minimum % measure != 0:
#             flag = False
#         else:
#             cnt += 1
#     if measure_cnt == cnt and flag: break
#     minimum += 1
#
# print(minimum)