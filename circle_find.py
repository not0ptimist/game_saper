def circle_find(t, con_bomb, razmer):
    sdvigi = [1, razmer - 1, razmer, razmer + 1]# Centr
    left_side = [t - razmer, t - razmer + 1, t + 1, t + razmer, t + razmer + 1]# Left if == 0
    right_side = [t - razmer - 1, t - razmer, t - 1, t + razmer - 1, t + razmer]# Right if == razmer - 1:
    # print(left_side, right_side, len(con_bomb), t % razmer)
    sum_bomb = 0
    if t % razmer == 0:
        for i in left_side:
            if 0 <= i < len(con_bomb):
                sum_bomb += con_bomb[i]
    elif t % razmer == razmer - 1:
        for i in right_side:
            if i < len(con_bomb):
                sum_bomb += con_bomb[i]
    else:
        for i in sdvigi:
            if t + i < len(con_bomb):
                sum_bomb += con_bomb[t + i]
            if t - i >= 0:
                sum_bomb += con_bomb[t - i]
    # print(sum_bomb)
    return sum_bomb


# test = [\
#     0, 0, 0, 0, 0, 0,\
#     0, 0, 0, 0, 1, 1, \
#     0, 0, 1, 0, 0, 0, \
#     0, 0, 0, 0, 0, 1, \
#     0, 0, 0, 1, 0, 0, \
#     0, 0, 0, 1, 0, 0]
# print(circle_find(35, test, 6))
# [0 0 1 0]
# [0 0 0 0]
# [1 0 0 1]
# [0 0 1 0]