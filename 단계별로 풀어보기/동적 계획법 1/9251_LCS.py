# LCS(Longest Common Subsequence)를 구하는 문제
# 문제
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
#
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
#
# 입력
# 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
#
# 출력
# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
#
# 예제 입력 1
# ACAYKP
# CAPCAK
# 예제 출력 1
# 4
import sys, copy

first = list(sys.stdin.readline()[:-1])
second = list(sys.stdin.readline()[:-1])
first_length = len(first)
second_length = len(second)
dp = [0 for _ in range(max(first_length, second_length) + 1)]

for idx in range(second_length):
    stand = second[idx]
    temp_dp = copy.copy(dp)
    for jdx in range(first_length):
        if stand == first[jdx]:
            dp[jdx + 1] = temp_dp[jdx] + 1
        else:
            dp[jdx + 1] = max(temp_dp[jdx + 1], dp[jdx])

    # print(dp)
print(max(dp))