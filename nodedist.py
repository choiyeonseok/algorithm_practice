import sys
import queue
sys.stdin = open("./inputs/input_nodedist.txt")

#방향성이 없는 그래프를 어떻게 구현할 것인가??
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())        #v, e 입력받기
    E_info = []
    visited = []
    for v in range(V+1):
        E_info.append([])
        visited.append(0)


    for e in range(E):
        A, B = map(int, input().split())
        E_info[A].append(B)
        E_info[B].append(A)
    S, G = map(int, input().split())
    path = queue.Queue(V)                   #큐의 길이는 (최대) v이다.
    path.put(S)
    visited[S] = 1
    f_end = 0
    cnt = 0
    ans = 0

    while f_end == 0 and not path.empty():
        if cnt == 0:
            ans += 1
            cnt = path.qsize()
        go = path.get()                     #path에서 하나를 추출
        cnt -= 1                            #거의 붙어다니는 수준
        for i in E_info[go]:                #츨발점
            if i == G:
                f_end = 1                   #반복문 탈출.
                break
            elif visited[i] == 0:           #아직 방문이 덜 된 경우,
                visited[i] = 1              #방문을 먼저하고 방문된 노드를 큐에 넣는다.
                path.put(i)
    if f_end == 0:
        ans = -1
    print('#{0} {1}'.format(test_case, ans))

