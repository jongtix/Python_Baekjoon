# 쿼드트리를 문자열로 바꾸는 문제
# 문제
# 흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다. 흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서 같은 숫자의 점들이 한 곳에 많이 몰려있으면, 쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다.
#
# 주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다. 만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며, 이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다
#
#
#
# 위 그림에서 왼쪽의 영상은 오른쪽의 배열과 같이 숫자로 주어지며, 이 영상을 쿼드 트리 구조를 이용하여 압축하면 "(0(0011)(0(0111)01)1)"로 표현된다.  N ×N 크기의 영상이 주어질 때, 이 영상을 압축한 결과를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에는 영상의 크기를 나타내는 숫자 N 이 주어진다. N 은 언제나 2의 제곱수로 주어지며, 1≤N ≤64의 범위를 가진다. 두 번째 줄부터는 길이 N 의 문자열이 N 개 들어온다. 각 문자열은 0 또는 1의 숫자로 이루어져 있으며, 영상의 각 점들을 나타낸다.
#
# 출력
# 영상을 압축한 결과를 출력한다.
#
# 예제 입력 1
# 8
# 11110000
# 11110000
# 00011100
# 00011100
# 11110000
# 11110000
# 11110011
# 11110011
# 예제 출력 1
# ((110(0101))(0010)1(0001))
import sys

# 런타임 에러 실패
# def cut(org_list, s):
#     global length
#     size = len(org_list)
# 
#     if org_list == [[0 for j in range(size)] for i in range(size)]:
#         if length == 2 and size != 1: s += '('
#         s += '0'
#         if length == 2 and size != 1: s += ')'
#         return s
#     elif org_list == [[1 for j in range(size)] for i in range(size)]:
#         if length == 2 and size != 1: s += '('
#         s += '1'
#         if length == 2 and size != 1: s += ')'
#         return s
# 
#     new_list1 = [[org_list[i][j] for j in range(0, size // 2)] for i in range(0, size // 2)]
#     new_list2 = [[org_list[i][j] for j in range(size // 2, size)] for i in range(0, size // 2)]
#     new_list3 = [[org_list[i][j] for j in range(0, size // 2)] for i in range(size // 2, size)]
#     new_list4 = [[org_list[i][j] for j in range(size // 2, size)] for i in range(size // 2, size)]
# 
#     s += '('
#     s += cut(new_list1, '')
#     s += cut(new_list2, '')
#     s += cut(new_list3, '')
#     s += cut(new_list4, '')
#     s += ')'
# 
#     return s
# 
# 
# org_list = []
# length = int(sys.stdin.readline())
# for _ in range(length):
#     org_list.append(list(map(int, list(sys.stdin.readline()[:-1]))))
# if length == 1: print('(', end='')
# print(cut(org_list, ''), end='')
# if length == 1: print(')', end='')

# 런타임 에러 실패
# def cut(start_x, start_y, end_x, end_y):
#     global result, size
#     list_sum = 0
#     for y in range(start_y, end_y):
#         for x in range(start_x, end_x):
#             list_sum += input_list[y][x]
#     if list_sum == 0:
#         if size <= 2: result += '('
#         result += '0'
#         if size <= 2: result += ')'
#         return
#     elif list_sum == (end_x - start_x) ** 2:
#         if size <= 2: result += '('
#         result += '1'
#         if size <= 2: result += ')'
#         return
#     else:
#         result += '('
#         if end_x - start_x > 2:
#             length = (end_x - start_x) // 2
#             cut(start_x, start_y, start_x + length, start_y + length)
#             cut(start_x + length, start_y, end_x, start_y + length)
#             cut(start_x, start_y + length, start_x + length, end_y)
#             cut(start_x + length, start_y + length, end_x, end_y)
#         else:
#             for temp in input_list[start_y:end_y]:
#                 for temp2 in temp[start_x:end_x]:
#                     result += str(temp2)
#         result += ')'
#
#
# result = ''
# input_list = []
# size = int(sys.stdin.readline())
# if size == 1:
#     print('(' + sys.stdin.readline()[:-1] + ')')
# else:
#     for _ in range(size):
#         input_list.append(list(map(int, list(sys.stdin.readline()[:-1]))))
#     cut(0, 0, size, size)
#     print(result)

# 틀렸습니다
# def cut(start_x, start_y, end_x, end_y):
#     global result
#     size = abs(end_x - start_x) // 2
#     if size >= 1:
#         result += '('
#         temp_sum = 0
#         for temp in n_list[start_y:start_y + size]:
#             temp_sum += sum(temp[start_x:start_x + size])
#         if temp_sum == 0:
#             result += '0'
#         elif temp_sum == 1:
#             result += '1'
#         else:
#             cut(start_x, start_y, start_x + size, start_y + size)
#         temp_sum = 0
#         for temp in n_list[start_y:start_y + size]:
#             temp_sum += sum(temp[start_x + size: end_x])
#         if temp_sum == 0:
#             result += '0'
#         elif temp_sum == 1:
#             result += '1'
#         else:
#             cut(start_x + size, start_y, end_x, start_y + size)
#         temp_sum = 0
#         for temp in n_list[start_y + size:end_y]:
#             temp_sum += sum(temp[start_x:start_x + size])
#         if temp_sum == 0:
#             result += '0'
#         elif temp_sum == 1:
#             result += '1'
#         else:
#             cut(start_x, start_y + size, start_x + size, end_y)
#         temp_sum = 0
#         for temp in n_list[start_y + size:end_y]:
#             temp_sum += sum(temp[start_x + size: end_x])
#         if temp_sum == 0:
#             result += '0'
#         elif temp_sum == 1:
#             result += '1'
#         else:
#             cut(start_x + size, start_y + size, end_x, end_y)
#         result += ')'
#     else:
#         result += str(n_list[start_y][start_x])
#
#
# n_list = []
# nth = int(sys.stdin.readline())
# result = ''
# if nth == 1:
#     result = '('
# for _ in range(nth):
#     n_list.append(list(map(int, list(sys.stdin.readline()[:-1]))))
# cut(0, 0, nth, nth)
# if nth == 1:
#     result += ')'
# print(result)

# 틀렸습니다
# def cut(start_x, start_y, end_x, end_y):
#     global result
#     num_sum = 0
#     for temp in n_list[start_y:end_y]:
#         num_sum += sum(temp[start_x:end_x])
#     if num_sum == abs(start_x - end_x) ** 2:
#         result += '1'
#         return
#     elif num_sum == 0:
#         result += '0'
#         return
#     else:
#         size = abs(start_x - end_x) // 2
#         result += '('
#         cut(start_x, start_y, start_x + size, start_y + size)
#         cut(start_x + size, start_y, end_x, start_y + size)
#         cut(start_x, start_y + size, start_x + size, end_y)
#         cut(start_x + size, start_y + size, end_x, end_y)
#         result += ')'
#
#
# n_list = []
# result = ''
# nth = int(sys.stdin.readline())
# if nth == 1:
#     print('(' + sys.stdin.readline()[:-1] + ')')
# elif nth == 2:
#     print('(' + sys.stdin.readline()[:-1] + sys.stdin.readline()[:-1] + ')')
# else:
#     for _ in range(nth):
#         n_list.append(list(map(int, list(sys.stdin.readline()[:-1]))))
#     cut(0, 0, nth, nth)
#     print(result)