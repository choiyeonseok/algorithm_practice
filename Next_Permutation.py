def swap(list, a, b):
    temp = list[b]
    list[b] = list[a]
    list[a] = temp


def next_permutation(c_list, n):
    i = n - 1
    while c_list[i - 1] >= c_list[i]:
        i -= 1
    if i <= 0: return False
    j = n - 1
    while c_list[j] <= c_list[i - 1]:
        j -= 1
    swap(c_list, j, i - 1)
    j = n - 1
    while i < j:
        swap(c_list, j, i)
        i += 1
        j -= 1
    return c_list


c_list = [7, 2, 3, 6, 5, 4, 1]
n = len(c_list)
print(next_permutation(c_list, n))


