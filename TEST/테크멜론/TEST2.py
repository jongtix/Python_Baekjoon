def solution(arr):
    minimum = arr[0]
    maximum = -1
    for idx in range(1, len(arr)):
        stand = arr[idx]
        comp = arr[idx - 1]
        if minimum > comp: minimum = comp
        if stand > minimum and stand - minimum > maximum: maximum = stand - minimum
    return maximum


print(solution([7,4,5,3,8,2]))