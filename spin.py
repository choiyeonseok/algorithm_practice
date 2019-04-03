import sys
sys.stdin = open("./inputs/input_spin.txt")

def solve(q):
    for i in range(m):
        q.append(q.pop(0))
    return q[0]


T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    answer = solve(q)
    print('#{0} {1}'.format(test_case, answer))
