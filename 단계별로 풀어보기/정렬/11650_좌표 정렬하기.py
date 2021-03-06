# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
#
# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
#
# 예제 입력 1
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3
# 예제 출력 1
# 1 -1
# 1 1
# 2 2
# 3 3
# 3 4


# N = int(input())
# x_point = list()
# y_point = list()
# for _ in range(N):
#     x, y = input().split()
#     x_point.append(x)
#     y_point.append(y)
#
# for i in range(N - 1):
#     for j in range(i, N):
#         if x_point[i] > x_point[j]:
#             x_point[i], x_point[j] = x_point[j], x_point[i]
#             y_point[i], y_point[j] = y_point[j], y_point[i]
#         elif x_point[i] == x_point[j]:
#             if y_point[i] > y_point[j]:
#                 x_point[i], x_point[j] = x_point[j], x_point[j]
#                 y_point[i], y_point[j] = y_point[j], y_point[i]
#
# for idx in range(N):
#     print(x_point[idx], y_point[idx])

N = int(input())
point_list = [(tuple(map(int, input().split()))) for _ in range(N)]
point_list = sorted(point_list, key=lambda k:(k[0], k[1]))
# for i in range(N - 1):
#     for j in range(i, N):
#         if point_list[i][1] > point_list[j][1]:
#             point_list[i], point_list[j] = point_list[j], point_list[i]
for x in point_list:
    print(x[0], x[1])
