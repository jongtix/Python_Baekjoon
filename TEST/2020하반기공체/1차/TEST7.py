def solution(sales, links):
    answer = 0

    graph = [[] for _ in range(len(sales) + 1)]
    for link in links:
        start, end = link
        if start not in graph[start]: graph[start].append((start, sales[start - 1]))
        graph[start].append((end, sales[end - 1]))
    print(graph)


    return answer


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
print(solution([5, 6, 5, 3, 4], [[2,3], [1,4], [2,5], [1,2]]))
print(solution([5, 6, 5, 1, 4], [[2,3], [1,4], [2,5], [1,2]]))
print(solution([10, 10, 1, 1], [[3,2], [4,3], [1,4]]))