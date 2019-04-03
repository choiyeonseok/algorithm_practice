import sys
import queue
sys.stdin = open("./inputs/input_pizza.txt")


T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    cooking = queue.Queue(n)                    #큐의 길이를 설정
    m_list = list(map(int, input().split()))    #피자 갯수와 치즈정보를 받아온다.
    i = 0                                       #i는 몇번째 피자인지 식별하기 위한 번호표다.
    while i < m and not cooking.full():         #i가 피자갯수보다 적고, 큐가 다 차지 않았으면
        cooking.put([i, m_list[i]//2])          #번호표(?) 함께 치즈 절반을 넣는다. 어차피 확인할때는 절반이 되어야하므로 미리 줄여도 상관없다.
        i += 1                                  #다음 피자를 대기시킨다.
    while cooking.qsize() > 1:                  #현재 피자가 한개라도 돌아가고 있으면 회전을 시킨다.
        take = cooking.get()                    #가장앞에있는 피자를 뺀다. >> 중요한 연산
        if take[1] > 0:                         #피자의 치즈양이 0보다 크면
            cooking.put([take[0], take[1]//2])  #절반으로 줄이고 원래 번호와 함께 다시 돌린다.
        else:                                   #치즈가 0인거제
            if i < m:                           #피자번호가 총갯수보다 작으면 아직 다 안들어온거제
                cooking.put([i, m_list[i]//2])  #새로운 피자를 넣고 새로운 번호를 매기는거제
                i += 1
    ans = cooking.get()[0] + 1                  #큐에 피자가 한개남아있으면 해당 피자의 번호를 확인하고 1을 더해서 정답으로 리턴한다.
    print('#{0} {1}'.format(test_case, ans))

