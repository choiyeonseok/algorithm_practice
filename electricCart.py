import sys
import itertools
sys.stdin = open("./inputs/input_electricCart.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    array =[]
    for i in range(n):
        array.append(list(map(int, input().split())))

    check = []
    for i in range(2, n + 1):
        check.append(i)
    result = list(itertools.permutations(check))
    costs = []

    for i in range(len(result)):
        cost = 0
        start, path = 1, 0
        for j in range(len(result[0])):
            path = result[i][j]
            cost += array[start - 1][path - 1]
            start = path
        path = 1
        cost += array[start - 1][path - 1]
        costs.append(cost)
    print("#{0} {1}".format(test_case, min(costs)))
