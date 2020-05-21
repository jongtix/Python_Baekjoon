# 문제
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#
# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 입력
# 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)
#
# 출력
# 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
#
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.
#
# 예제 입력 1
# 3 1
# 예제 출력 1
# 1
# 2
# 3
# 예제 입력 2
# 4 2
# 예제 출력 2
# 1 1
# 1 2
# 1 3
# 1 4
# 2 1
# 2 2
# 2 3
# 2 4
# 3 1
# 3 2
# 3 3
# 3 4
# 4 1
# 4 2
# 4 3
# 4 4
# 예제 입력 3
# 3 3
# 예제 출력 3
# 1 1 1
# 1 1 2
# 1 1 3
# 1 2 1
# 1 2 2
# 1 2 3
# 1 3 1
# 1 3 2
# 1 3 3
# 2 1 1
# 2 1 2
# 2 1 3
# 2 2 1
# 2 2 2
# 2 2 3
# 2 3 1
# 2 3 2
# 2 3 3
# 3 1 1
# 3 1 2
# 3 1 3
# 3 2 1
# 3 2 2
# 3 2 3
# 3 3 1
# 3 3 2
# 3 3 3


def append_number(R: list, N: int):
    temp = []
    if R:
        for r in R:
            for i in range(N):
                i += 1
                temp_list = r[:]
                temp_list.append(i)
                temp.append(temp_list)
    else:
        for i in range(N):
            temp.append([i + 1])
    return temp


N, M = map(int, input().split())
total = 1
result = []
for _ in range(M):
    result = append_number(result, N)

for arr in result:
    print(' '.join(map(str, arr)))