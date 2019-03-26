#외판원 순회
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


def TSP(cost, list):
    n = len(list)
    result = []
    while list[0] == 1:
        sum = 0
        for i in range(len(list)):
            if cost[list[i % 4] - 1][list[(i + 1) % 4] - 1] == 0:
                sum += 10000000
            sum += cost[list[i % 4] - 1][list[(i + 1) % 4] - 1]
        result.append(sum)
        list = next_permutation(list, n)

    return min(result)


city = [1, 2, 3, 4]
cost = [[0, 10, 15, 20],
        [5, 0,  9,  10],
        [6, 13, 0,  12],
        [8,  8,  9,  0]]

print(TSP(cost, city))
