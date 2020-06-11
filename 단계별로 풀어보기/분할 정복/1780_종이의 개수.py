# 쿼드트리와 비슷한데 4개 대신 9개로 나누는 문제
# 문제
# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다. 우리는 이 행렬을 적절한 크기로 자르려고 하는데, 이때 다음의 규칙에 따라 자르려고 한다.
#
# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1≤N≤3^7, N은 3^k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.
#
# 출력
# 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.
#
# 예제 입력 1
# 9
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 0 1 -1 0 1 -1 0 1 -1
# 0 -1 1 0 1 -1 0 1 -1
# 0 1 -1 1 0 -1 0 1 -1
# 예제 출력 1
# 10
# 12
# 11
import sys

# 런타임 에러 실패
# def cut(org_list: list, s: str):
#     global cnt_one, cnt_minus, cnt_zero
#
#     size = len(org_list)
#     if org_list == [[0 for _ in range(size)] for _ in range(size)]:
#         cnt_zero += 1
#         return '0'
#     elif org_list == [[1 for _ in range(size)] for _ in range(size)]:
#         cnt_one += 1
#         return '1'
#     elif org_list == [[-1 for _ in range(size)] for _ in range(size)]:
#         cnt_minus += 1
#         return '-1'
#     else:
#         s += '('
#         s += cut([[org_list[i][j] for i in range(0, size // 3)] for j in range(0, size // 3)], '')
#         s += cut([[org_list[i][j] for i in range(0, size // 3)] for j in range(size // 3, (size // 3) * 2)], '')
#         s += cut([[org_list[i][j] for i in range(0, size // 3)] for j in range((size // 3) * 2, (size // 3) * 3)], '')
#         s += cut([[org_list[i][j] for i in range(size // 3, (size // 3) * 2)] for j in range(0, size // 3)], '')
#         s += cut([[org_list[i][j] for i in range(size // 3, (size // 3) * 2)] for j in range(size // 3, (size // 3) * 2)], '')
#         s += cut([[org_list[i][j] for i in range(size // 3, (size // 3) * 2)] for j in range((size // 3) * 2, (size // 3) * 3)], '')
#         s += cut([[org_list[i][j] for i in range((size // 3) * 2, (size // 3) * 3)] for j in range(0, size // 3)], '')
#         s += cut([[org_list[i][j] for i in range((size // 3) * 2, (size // 3) * 3)] for j in range(size // 3, (size // 3) * 2)], '')
#         s += cut([[org_list[i][j] for i in range((size // 3) * 2, (size // 3) * 3)] for j in range((size // 3) * 2, (size // 3) * 3)], '')
#         s += ')'
#         return s
#
#
# N = int(sys.stdin.readline())
# cnt_minus = 0
# cnt_zero = 0
# cnt_one = 0
# org_list = []
# for _ in range(N):
#     org_list.append(list(map(int, list(sys.stdin.readline()[:-1].split(' ')))))
# cut(org_list, '')
# print(cnt_minus, cnt_zero, cnt_one, sep='\n')