# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
#
# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
#
# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.
#
# 예제 입력 1
# 30 20
# 10 10
# 10 20
# 예제 출력 1
# 30 10


def dist(x1, x2, y1, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

xy = list()
# y = list()
xy.append((x1, y1))
xy.append((x2, y2))
xy.append((x3, y3))
# y.append(y1)
# y.append(y2)
# y.append(y3)

min_x = min(xy)[0]
# min

point_x = 0
point_y = 0
for idx in range(3):
    # if (x[idx % 3] - x[(idx + 1) % 3]) ** 2 + (y[idx % 3] - y[(idx + 1) % 3]) ** 2 + (x[idx % 3] - x[(idx + 2) % 3]) ** 2 + (y[idx % 3] - y[(idx + 2) % 3]) ** 2 == (x[(idx + 1) % 3] - x[(idx + 2) % 3]) ** 2 + (y[(idx + 1) % 3] - y[(idx + 2) % 3]) ** 2:
    if dist(xy[idx][0], xy[(idx + 1) % 3][0], xy[idx][1], xy[(idx + 1) % 3][1]) + dist(xy[idx][0], xy[(idx + 2) % 3][0], xy[idx][1], xy[(idx + 2) % 3][1]) == dist(xy[(idx + 2) % 3][0], xy[(idx + 1) % 3][0], xy[(idx + 2) % 3][1], xy[(idx + 1) % 3][1]):
        point_x = xy[idx][0]
        point_y = xy[idx][1]
        xy.remove(xy[idx])
        # y.remove(y[idx])
        break

# print(point_x, point_y)
# print(xy)

for x_p in range(1, 1001):
    if point_x - xy[0][0] == 0:
        print(xy[1][0], xy[0][1])
        break
    elif point_x - xy[1][0] == 0:
        print(xy[0][0], xy[1][1])
        break
    flag = False
    for y_p in range(1, 1001):
        if ((point_y - xy[0][1]) / (point_x - xy[0][0])) * (x_p - xy[1][0]) + xy[1][1] == ((point_y - xy[1][1]) / (point_x - xy[1][0])) * (x_p - xy[0][0]) + xy[0][1]:
            print(x_p, int((point_y - xy[0][1]) / (point_x - xy[0][0])) * (abs(x_p - xy[1][0]) - xy[0][0]) + (xy[0][1] + xy[1][1]))
            flag = True
            break
    if flag: break