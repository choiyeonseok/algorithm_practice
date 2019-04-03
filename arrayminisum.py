##이해가 안간다.


import sys
sys.stdin = open("./inputs/input_minisum.txt", "r")


def solve(array):
    ans = 0
    for i in range(n):
        ans += array[i][i]
    candidate = 0
    r = 0
    while r < n:
        f_select = 0
        for c in range(c_before[r] + 1, n):
            if availability_column[c] == 1:
                candidate += array[r][c]
                if candidate >= ans:
                    candidate -= array[r][c]
                else:
                    availability_column[c] = 0
                    c_before[r] = c
                    f_select = 1
                    break
        if f_select == 0:
            if r == 0:
                break
            candidate -= array[r-1][c_before[r-1]]
            availability_column[c_before[r-1]] = 1
            c_before[r] = -1
            r -= 1
        else:
            if r == n-1:
                ans = candidate
                candidate -= array[r][c_before[r]]
                availability_column[c_before[r]] = 1
            else:
                r += 1
    return ans


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    array = []
    availability_column = []
    c_before = []
    for i in range(n):
        array.append(list(map(int, input().split())))
        availability_column.append(1)
        c_before.append(-1)
    answer = solve(array)
    print('#{0} {1}'.format(test_case, answer))
