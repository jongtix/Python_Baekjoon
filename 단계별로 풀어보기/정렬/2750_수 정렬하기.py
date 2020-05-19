# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
#
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
#
# 예제 입력 1
# 5
# 5
# 2
# 3
# 4
# 1
# 예제 출력 1
# 1
# 2
# 3
# 4
# 5


N = int(input())
result = list()
for _ in range(N):
    result.append(int(input()))
# print(result)

# 삽입 정렬
for start in range(1, len(result)):
    for idx in range(start, 0, -1):
        if result[idx - 1] > result[idx]:
            result[idx - 1], result[idx] = result[idx], result[idx - 1]
    # print(result)

# 버블 정렬
# for start in range(len(result) - 1):
#     for idx in range(len(result) - start - 1):
#         if result[idx] > result[idx + 1]:
#             result[idx], result[idx + 1] = result[idx + 1], result[idx]
#     print(result)

# for i in range(len(result)):
#     for j in range(len(result)):
#         if result[i] < result[j]:
#             result[i], result[j] = result[j], result[i]

print('\n'.join(map(str, result)))