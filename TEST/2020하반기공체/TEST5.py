def get_sec(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def solution(play_time, adv_time, logs):
    answer = ''

    logs.sort()
    log_list = []
    for log in logs:
        start, end = log.split('-')
        log_list.append([start, end])
    print(log_list)

    temp_list = []
    start_time = '00:00:00'
    end_time = '00:00:00'
    count = 0
    for l in log_list:
        if l[0] <= end_time:
            count += 1
        else:
            start_time = l[0]
            end_time = l[1]
            count = 1
        temp_list.append([count, start_time, end_time])
    temp_list.sort(key=lambda x: x[0], reverse=True)
    print(temp_list)
    print(get_sec(temp_list[0][2]) - get_sec(adv_time))
    print(get_sec(temp_list[0][2]) - get_sec(temp_list[0][1]) - get_sec(adv_time))
#    if get_sec(temp_list[0][2]) - get_sec(adv_time) < 0:
#      if (get_sec(temp_list[0][2] - temp_list[0][1])) < get_sec(adv_time):
#
#      else:
#    else:
#        answer =


    return answer


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "21:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))