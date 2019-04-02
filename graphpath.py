import sys
sys.stdin = open("./inputs/input_graphpath.txt", "r")

def pathsum(a, b):
    #a => [1, 2]
    #b => [2, 4]
    c = []
    if a[-1] == b[0]:
        c.append(a[0])
        c.append(b[-1])
    else: return 0
    return c


def solve(path, stack, result):
    fore = result[0]
    i = 0
    while 1:
        while i < len(path):
            if path[i][0] == fore:
                stack.append(path[i])
                fore = path[i][1]
                i = 0
                continue
            i += 1

        for j in range(len(stack) - 1):
            this = stack[j]
            check = pathsum(this, stack[j + 1])
            if len(stack) >= 2:
                stack[j + 1] = check

        print(stack)
        if check == result:
            return 1
        else:
            continue




T = int(input())
answer =[]
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    path = []
    stack = []
    for i in range(E):
        path.append(list(map(int, input().split())))
    result = list(map(int, input().split()))
    print(solve(path, stack, result))


# for test_case in range(1, T+1):
#     print(f'#{test_case}', answer[test_case - 1])