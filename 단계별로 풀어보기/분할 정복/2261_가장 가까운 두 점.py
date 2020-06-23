# 가장 가까운 두 점을 구하는 문제. 잘 알려진 문제지만 상당히 어렵기 때문에 검색을 추천드립니다.
# 문제
# 2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 n(2 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 줄에는 차례로 각 점의 x, y좌표가 주어진다. 각각의 좌표는 절댓값이 10,000을 넘지 않는 정수이다. 같은 점이 여러 번 주어질 수도 있다.
#
# 출력
# 첫째 줄에 가장 가까운 두 점의 거리의 제곱을 출력한다.
#
# 예제 입력 1
# 4
# 0 0
# 10 10
# 0 10
# 10 0
# 예제 출력 1
# 100
import sys


def dist(first_point, second_point):
    return


# def find_dist(point_list):
    # if left == right:
    # return


point_list = []
for _ in range(int(sys.stdin.readline())):
    point_list.append(tuple(map(int, sys.stdin.readline().split(' '))))
print(find_dist(point_list))