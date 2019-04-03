import sys
sys.stdin = open("./inputs/input_distOfmaze.txt")


T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    maze = []
    visited = []
    for i in range(n):
        maze.append(list(map(int, input())))
        temp = []
        for j in range(n):
            temp.append(0)
        visited.append(temp)

    # print(maze)
    # print(visited)
    start = []
    i = 0
    while start == [] and i < n:
        j = 0
        while start == [] and j < n:
            if  maze[i][j] == 2:
                start = [i, j]
            j += 1
        i += 1
    search_queue = [start]
    visited[start[0]][start[1]] = 1 #출발점을 방문표시함
    moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ans = 0
    success = 0
    fail = 0
    count = 1
    r, c = 0, 0
    while len(search_queue)>0 and success == 0:
        if count == 0: #정답 발견시 반환
            count = len(search_queue)
            ans += 1
        r, c = search_queue.pop(0)
        count -= 1
        for m in moves:
            nr, nc = r + m[0], c + m[1]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            elif visited[nr][nc] == 1:
                continue
            else:
                if maze[nr][nc] == 0:
                    search_queue.append([nr, nc])
                    visited[nr][nc] = 1
                elif maze[nr][nc] == 3:
                    success = 1
                    break
    if success == 0:
        ans = 0

    print('#{0} {1}'.format(test_case, ans))
