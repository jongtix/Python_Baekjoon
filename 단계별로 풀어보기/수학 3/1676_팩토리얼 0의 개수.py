# 소인수분해의 성질을 활용하여 N!의 끝에 0이 얼마나 많이 오는지 구하는 문제
# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
#
# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.
#
# 예제 입력 1
# 10
# 예제 출력 1
# 2
import sys

cache = [0 for _ in range(501)]


def factorial(n):
    if n <= 1:
        return 1
    else:
        if cache[n] != 0: return cache[n]
        cache[n] = n * factorial(n - 1)
        return cache[n]


N = int(sys.stdin.readline())
cnt = 0
for check in reversed(list(str(factorial(N)))):
    if check != '0':
        break
    else:
        cnt += 1

print(cnt)

# 10 이 곱해져야 0 이 생기고 10 은 2 와 5 의 곱이다. 팩토리얼에서 2 는 충분히 많다고 가정했을 때 5 의 개수가 0 의 개수
# import sys
# N = int(sys.stdin.readline())
# print(N // 5 + N // 25 + N // 125)