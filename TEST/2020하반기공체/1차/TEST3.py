def solution(info, query):
    answer = []

    info_list = []
    for p_info in info:
        l, p, c, f, s = p_info.split()
        info_list.append((int(s), [l, p, c, f]))

    for p_query in query:
        count = 0
        p_query = p_query.replace('and', '')
        query_list = p_query.split()
        for infomation in info_list:
            if infomation[0] >= int(query_list[-1]):
                flag = True
                for idx in range(4):
                    if query_list[idx] != '-':
                        if infomation[1][idx] != query_list[idx]:
                            flag = False
                            break
                if flag: count += 1
        answer.append(count)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))