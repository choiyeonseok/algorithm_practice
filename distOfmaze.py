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
    success = 0 #길찾기 성공여부
    fail = 0    #길찾기 실패여부
    count = 1   #움직인 칸 수
    r, c = 0, 0
    while len(search_queue) > 0 and success == 0:
        if count == 0:                  #정답 발견시 반환
            count = len(search_queue)   #경로수는 큐의 갯수
            ans += 1
        r, c = search_queue.pop(0)      #경로하나 빼면 경로수 감소
        count -= 1                      #여기가 좀 핵심

        for m in moves:                 #이동요소들을 미리 정의 해놓고 각각 더해서 이동시킴
            nr, nc = r + m[0], c + m[1]
            if nr < 0 or nr >= n or nc < 0 or nc >= n:  #이동할 수 없는 방향의 위치라면
                continue                                #다른 방향 이동으로
            elif visited[nr][nc] == 1:                  #이미 방문한 경로라면
                continue                                #다른 이동가능한 방향으로
            else:
                if maze[nr][nc] == 0:                   #이동이 가능한 길이면// 해당노드에 연결된 노드들 추가
                    search_queue.append([nr, nc])       #큐에 경로를 추가하고
                    visited[nr][nc] = 1                 #방문했다고 표시한다.
                elif maze[nr][nc] == 3:                 #이동 후 도착지에 도착했다면
                    success = 1                         #성공표시하고
                    break                               #루프를 나간다.
    if success == 0:                                    #success 가 0이라면 즉 도착지를 찾기 못했다면
        ans = 0                                         #경로는 없다고 나온다.

    print('#{0} {1}'.format(test_case, ans))
