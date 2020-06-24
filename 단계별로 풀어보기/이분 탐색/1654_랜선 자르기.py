# 흔히 parametric search라고도 부르는, 이분 탐색을 응용하여 최솟값이나 최댓값을 찾는 테크닉을 배우는 문제
# 문제
# 집에서 시간을 보내던 오영식은 박성원의 부름을 받고 급히 달려왔다. 박성원이 캠프 때 쓸 N개의 랜선을 만들어야 하는데 너무 바빠서 영식이에게 도움을 청했다.
#
# 이미 오영식은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다. 박성원은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
#
# 편의를 위해 랜선을 자르거나 만들 때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 그리고 자를 때는 항상 센티미터 단위로 정수길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 오영식이 이미 가지고 있는 랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력된다. K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수이다. 그리고 항상 K ≦ N 이다. 그 후 K줄에 걸쳐 이미 가지고 있는 각 랜선의 길이가 센티미터 단위의 정수로 입력된다. 랜선의 길이는 231-1보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 N개를 만들 수 있는 랜선의 최대 길이를 센티미터 단위의 정수로 출력한다.
#
# 예제 입력 1
# 4 11
# 802
# 743
# 457
# 539
# 예제 출력 1
# 200
import sys

# 47%에서 틀렸습니다
def solution(org_line, N):
    maximum = 0
    left = 0
    right = org_line[-1]
    while left <= right:
        cnt = 0
        pivot = left + (right - left) // 2
        for line in org_line:
            cnt += line // pivot
        if cnt < N:
            right = pivot - 1
        else:
            if pivot > maximum: maximum = pivot
            left = pivot + 1
    return maximum


# 시간 초과 실패
# def solution(org_line, N):
#     result = 0
#     i = 1
#     cut = org_line[-1] // i
#     while True:
#         result += i
#         for line in org_line[:-1]:
#             result += line // cut
#         if result >= N:
#             break
#         if result < N / i and result > N / (i + 1):
#             i += 1
#             cut = org_line[-1] // i
#         else:
#             i += 1
#             cut -= 1
#         result = 0
#     return cut


K, N = map(int, sys.stdin.readline()[:-1].split(' '))
org_line = []
for _ in range(K):
    org_line.append(int(sys.stdin.readline()))
org_line.sort()
if K >= N:
    print(org_line[-1])
else:
    print(solution(org_line, N))