import sys
sys.stdin = open("./inputs/input_maze.txt", "r")


def solve(maze):
    n = len(maze)
    visited = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        visited.append(temp)
    i, j = 0, 0
    start, end = (), ()


    while len(start) == 0 or len(end) == 0:
        if maze[i][j] == 2:
            start = (i, j)
        elif maze[i][j] == 3:
            end = (i, j)
        if j == n - 1:
            i += 1
            j = 0
        else:
            j += 1

    map_stack = []
    r, c = start[0], start[1]
    map_stack.append((r, c))
    ans = 0

    while len(map_stack) > 0:
        cur = map_stack.pop()
        r, c = cur[0], cur[1]
        if c == end[1]:
            if r-1 == end[0] or r + 1 == end[0]:
                ans = 1
                break
        if r == end[0]:
            if c-1 == end[1] or c+1 == end[1]:
                ans = 1
                break
        if c-1 >= 0 and maze[r][c-1] == 0 and visited[r][c-1] == 0: #왼쪽
            map_stack.append((r, c-1))
            visited[r][c-1] = 1 #방문했다
        if r+1 < n and maze[r+1][c] == 0 and visited[r+1][c] == 0: #벽이아니고, 길이어야하고, 방문하지 않았다면 이동하라
            map_stack.append((r+1, c))
            visited[r+1][c] = 1
        if c+1 < n and maze[r][c+1] == 0 and visited[r][c+1] == 0:
            map_stack.append((r, c+1))
            visited[r][c+1] = 1
        if r-1 >= 0 and maze[r-1][c] == 0 and visited[r-1][c] == 0:
            map_stack.append((r-1, c))
            visited[r-1][c] = 1
    return ans








T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    maze = []
    for i in range(n):
        maze.append(list(map(int, input())))

    print('#{0} {1}'.format(test_case, solve(maze)))