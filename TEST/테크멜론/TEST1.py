import string


def solution(args: str):
    answer = 0
    spell = string.ascii_uppercase
    str_arr = list(args)
    last_idx = 0
    for word in str_arr:
        cur_idx = spell.index(word)
        if abs(cur_idx - last_idx) <= 13:
            answer += abs(cur_idx - last_idx)
        else:
            answer += min((26 - cur_idx) + last_idx, (26 - last_idx) + cur_idx)
        last_idx = cur_idx

    return answer


print(solution('BZA'))