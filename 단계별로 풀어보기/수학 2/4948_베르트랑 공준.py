# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
#
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
#
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
#
# n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하며, 한 줄로 이루어져 있다. (n ≤ 123456)
#
# 입력의 마지막에는 0이 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
#
# 예제 입력 1
# 1
# 10
# 13
# 100
# 1000
# 10000
# 100000
# 0
# 예제 출력 1
# 1
# 4
# 3
# 21
# 135
# 1033
# 8392
sosoo_list = list()


# def check(number):
#     count = 0
#     for num in range(2, int(number ** 1/2) + 1):
#         if number % num == 0:
#             count += 1
#     if count == 0:
#         sosoo_list.append(number)
#         return True
#     else:
#         return False


def answer(n):
    count = 0
    M = n
    N = 2 * n
    num_list = {x: False for x in range(M + 1, N + 1)}

    for i in range(2, N + 1):
        if i in num_list.keys() and num_list[i]: pass
        for j in range(2 * i, N + 1, i):
            if j in num_list.keys(): num_list[j] = True

    for number, check in num_list.items():
        if not check: count += 1
    #
    #
    # for number in range(n, 2 * n):
    #     number += 1
    #     if number in sosoo_list: count += 1
    #     elif check(number): count += 1
    return count

while True:
    n = int(input())
    if not n: break
    print(answer(n))
