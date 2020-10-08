import heapq, math


def solution(n, s, a, b, fares):
    answer = 0

    graph = [[] for _ in range(n + 1)]
    dist = [math.inf for _ in range(n + 1)]
    for fare in fares:
        c, d, f = fare
        graph[c].append((f, d))
        graph[d].append((f, c))

    que = []
    heapq.heappush(que, (0, s))
    dist[s] = 0
    while que:
        cost, cur_point = heapq.heappop(que)
        for value, next_point in graph[cur_point]:
            if dist[next_point] > cost + value:
                heapq.heappush(que, (cost + value, next_point))
                dist[next_point] = cost + value

    print(dist)
    answer_list = []
    for idx, start in enumerate(dist):
        if idx == 0: continue

        temp_dist = [math.inf for _ in range(n + 1)]
        temp_que = []
        heapq.heappush(temp_que, (0, idx))
        temp_dist[idx] = 0
        while temp_que:
            temp_cost, temp_cur_point = heapq.heappop(temp_que)
            for temp_value, temp_next_point in graph[temp_cur_point]:
                if temp_dist[temp_next_point] > temp_cost + temp_value:
                    heapq.heappush(temp_que, (temp_cost + temp_value, temp_next_point))
                    temp_dist[temp_next_point] = temp_cost + temp_value
        print(start, temp_dist[a], temp_dist[b])
        answer_list.append(start + temp_dist[a] + temp_dist[b])

    print(answer_list)
    answer = min(answer_list)

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))