# -*- coding: utf-8 -*-
import copy, operator

# v_list = [[False for _ in range(9)] for _ in range(9)]
# for idx, v_x in enumerate(v_list):
#     for idy, value in enumerate(v_x):
#         print(idx, idy, value)

# old_list = [1, 2, 3]
# new_list1 = old_list
# new_list2 = old_list.copy()
# new_list3 = list(old_list)
# new_list4 = old_list[:]
# new_list5 = copy.copy(old_list)
# old_list[0] = 5
# print(old_list)
# print(new_list1)
# print(new_list2)
# print(new_list3)
# print(new_list4)
# print(new_list5)

# print(tuple(map(operator.add, (1, 1), (2, 3))))
# print([1,2,3,4][1::-1])

count = [7, 8, 9]
print(*count, sep='\n')
print('\n'.join(str(cnt) for cnt in count))
for cnt in count:
    print(cnt)