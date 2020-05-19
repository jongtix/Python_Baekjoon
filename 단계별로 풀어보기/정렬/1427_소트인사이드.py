# 문제
# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
#
# 입력
# 첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
#
# 출력
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
#
# 예제 입력 1
# 2143
# 예제 출력 1
# 4321


# N = input()
# number_list = sorted(list(input()))
# print(N.split())
# number_list = list(map(int, N.split()))
# number_list = []
# for n in N:
#     number_list.append(int(n))
# number_list.sort()
# print(number_list)
print(int(''.join(map(str, sorted(list(input()), reverse=True)))))