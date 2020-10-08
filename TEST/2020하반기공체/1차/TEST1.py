import re


def solution(new_id):
    answer = ''

    temp = ''

    # step 1
    p = re.findall('[A-Z]+', new_id)
    for o in p:
        new_id = new_id.replace(o, o.lower())
    print(1, p)

    # step 2
    p = re.findall('[a-z0-9\-_.]+', new_id)
    for o in p:
        temp += o
    new_id = temp
    temp = ''
    print(2, p)

    # step 3
    p = re.findall('[.]{2,}', new_id)
    for o in p:
        new_id = new_id.replace(o, '.')
    print(3, p)
    print(3, new_id)

    # step 4
    p = re.match('^\.', new_id)
    if p:
        new_id = new_id[1:]
    print(4, new_id)
    p = re.search('[.]$', new_id)
    print(4, p)
    if p:
        new_id = new_id[:-1]
    print(4, new_id)

    # step 5
    if not new_id:
        new_id = 'a'
    print(5, new_id)

    # step 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    print(61, new_id, len(new_id))
    p = re.search('[.]$', new_id)
    print(62, p)
    if p:
        new_id = new_id[:-1]
    print(6, new_id)

    # stop 7
    answer = new_id
    if len(new_id) <= 2:
        while len(answer) < 3:
            answer += new_id[-1]
    print(7, p)

    # print(new_id)

    return answer


#print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution('z-+.^.'))
#print(solution('=.='))
#print(solution('123_.def'))
print(solution('abcdefghijklmn.p'))