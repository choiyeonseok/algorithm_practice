def flip(some_list):
    if len(some_list) == 1 or len(some_list) == 0:
        return some_list
    return some_list[-1:] + flip(some_list[:-1])


def next_permutation(clist):
    cand = 0
    for i in range(1, len(clist)):
        #r은 5 ~ 1까지 참조
        r = len(clist) - i
        if clist[r - 1] < clist[r]:
            for j in range(r, len(clist)):
                if clist[r - 1] > clist[j]:
                    cand = min(clist[r:j])
            for j in range(r, len(clist)):
                if clist[j] == cand:
                    temp = clist[j]
                    clist[j] = clist[r-1]
                    clist[r-1] = temp
            clist[r:] = flip(clist[r:])
        if cand != 0:
            return clist

print(next_permutation([7, 2, 3, 5, 4, 1]))


