N = int(input())
answer = 1
if N == 0:
    print(answer)
else:
    for n in range(1, N + 1):
        answer *= n
    print(answer)