def swap(list, a, b):
    temp = list[b]
    list[b] = list[a]
    list[a] = temp


def next_permutation(c_list, n):
    i = n - 1
    while c_list[i - 1] >= c_list[i]:
        i -= 1
    if i <= 0:
        return False
    else:
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


def calculate_absum_value(plist):
    result = 0
    for i in range(1, len(plist)):
        result += abs(plist[i] - plist[i - 1])
    return result


def sort_list(list):
    if len(list) <= 1:
        return list

    for i in range(len(list)):
        if list[i] > list[-1]:
            swap(list, i, -1)
    return sort_list(list[:-1]) + list[-1:]


def find_max_perm(plist):
    length = len(plist)
    allCase = []
    while 1:
        if plist == False:
            break
        else:
            allCase.append(calculate_absum_value(next_permutation(plist, length)))
            plist = next_permutation(plist, length)
    return max(allCase)

A = [7, 2, 4, 1, 3, 5, 6]
A = sort_list(A)
n = len(A)

print(find_max_perm(A))



