# 식의 값을 가능한 한 작게 만드는 문제
# 문제
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 길이가 최대 50인 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
#
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
#
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고, 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다.
#
# 출력
# 첫째 줄에 정답을 출력한다.
#
# 예제 입력 1
# 55-50+40
# 예제 출력 1
# -35
import sys

numbers = list(sys.stdin.readline()[:-1].split('-'))
total = 0
for idx, number in enumerate(numbers):
    temp_sum = 0
    for n in number.split('+'):
        temp_sum += int(n)
    if idx == 0: total += int(temp_sum)
    else: total -= int(temp_sum)

print(total)

# 런타임 에러 실패
# numbers = list(sys.stdin.readline()[:-1])
#
# operator_list = []
# for idx, operator in enumerate(numbers):
#     if operator == '-' or operator == '+':
#         operator_list.append((operator, idx))
#
# total = int(''.join(numbers[:operator_list[0][1]]))
# start = 0
# end = 0
# flag = False
# for idx in range(len(operator_list) - 1):
#     operator = operator_list[idx][0]
#     start = operator_list[idx][1]
#     end = operator_list[idx + 1][1]
#     if operator == '-': flag = True
#     if operator == '+' and flag: operator = '-'
#     total += int(operator + ''.join(numbers[start + 1:end]))
#
# if flag: total += int('-' + ''.join(numbers[end + 1:]))
# else: total += int(operator_list[-1][0] + ''.join(numbers[end + 1:]))
#
#
# print(total)