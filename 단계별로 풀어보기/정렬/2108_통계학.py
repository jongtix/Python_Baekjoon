# 문제
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
#
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.
#
# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
#
# 둘째 줄에는 중앙값을 출력한다.
#
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
#
# 넷째 줄에는 범위를 출력한다.
#
# 예제 입력 1
# 5
# 1
# 3
# 8
# -2
# 2
# 예제 출력 1
# 2
# 2
# 1
# 10
# 예제 입력 2
# 1
# 4000
# 예제 출력 2
# 4000
# 4000
# 4000
# 0
# 예제 입력 3
# 5
# -1
# -2
# -3
# -1
# -2
# 예제 출력 3
# -2
# -2
# -1
# 2


def sansool(number_list: list, length: int):
    return round(sum(number_list) / length)


def joongang(number_list: list, length: int):
    # idx = length // 2
    return number_list[length // 2]


def chaebeen(number_list: list):
    count_list = [0 for _ in range(8001)]
    for number in number_list:
        count_list[4000 + number] += 1
    # print(count_list)
    max_count = max(count_list)
    idx = 0
    result = 4001
    for i, count in enumerate(count_list):
        if count == max_count:
            idx += 1
            result = i - 4000
        if idx == 2: break
    return result

    # result = dict()
    # for number in set(number_list):
    #     count = number_list.count(number)
    #     if count in result:
    #         # print(type(result[count]))
    #         result[count].append(number)
    #     else:
    #         result[count] = [number]
    #
    # r = sorted(result[max(result.keys())])
    # # print(r)
    # if len(r) > 1:
    #     return r[1]
    # else:
    #     return r[0]


    # sorted(result.items(), key=(lambda k: k[0]))
    # result = sorted(result.items(), key=(lambda k: k[1]), reverse=True)
    # check = 0
    # r_s = set()
    # for idx, (number, value) in enumerate(result):
    #     if idx == 0: check = value
    #     if check > value: break
    #     r_s.add(number)
    # r = sorted(r_s)
    # if len(r) > 1:
    #     return r[1]
    # else: return r[0]

    # number_dict = dict()
    # for number in number_list:
    #     if number in number_dict.keys():
    #         number_dict[number] = number_dict[number] + 1
    #     else:
    #         number_dict[number] = 1
    # sorted(number_dict, key=lambda k: number_dict[k])
    # print(number_dict)
    # max_count = 0
    # # for key, value in number_dict.items():
    # #     if
    # return max(number_dict.keys(), key=lambda k: number_dict[k])


def bumwee(number_list: list, length: int):
    return number_list[length - 1] - number_list[0]

N = int(input())
number_list = [int(input()) for _ in range(N)]
number_list.sort()
length = len(number_list)
print(sansool(number_list, N))
print(joongang(number_list, N))
print(chaebeen(number_list))
print(bumwee(number_list, N))