import sys
from collections import deque

def visit_water(m, wq1, wq2, wv) :
    global r, c, dx, dy
    while wq1 :
        x, y = wq1.popleft()
        m[x][y] = "."
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c or wv[nx][ny] : continue
            if m[nx][ny] == "." : wq1.append((nx, ny))
            else : wq2.append((nx, ny))
            wv[nx][ny] = True
    return m, wq1, wq2, wv

def init(wq, sq, wv, sv) :
    global r, c, m
    des = None
    for i in range(r) :
        for j in range(c) :
            if m[i][j] == "L" :
                if not sq :
                    sq.append((i, j))
                    sv[i][j] = True
                else :
                    des = (i, j)
                m[i][j] = "."
            if m[i][j] == "." :
                wq.append((i, j))
                wv[i][j] = True
    return des, wq, sq, wv, sv

if __name__ == "__main__" :
    r, c = map(int, sys.stdin.readline().split())

    dx, dy = (0, -1, 0, 1), (-1, 0, 1, 0)

    # 맵
    m = [list(sys.stdin.readline().strip()) for _ in range(r)]

    # 방문 체크
    wv = [[False] * c for _ in range(r)]
    sv = [[False] * c for _ in range(r)]

    # 딥큐
    wq1, wq2 = deque(), deque()
    sq1, sq2 = deque(), deque()

    # 초기 설정
    des, wq1, sq1, wv, sv = init(wq1, sq1, wv, sv)


    def visit_swam():
        while sq1:
            x, y = sq1.popleft()
            if x == des[0] and y == des[1]:
                return True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= r or ny < 0 or ny >= c or sv[nx][ny]: continue
                if m[nx][ny] == ".":
                    sq1.append((nx, ny))
                else:
                    sq2.append((nx, ny))
                sv[nx][ny] = True

        return False


    ret = 0
    while True :
        m, wq1, wq2, wv = visit_water(m, wq1, wq2, wv)
        if visit_swam() : break
        wq1 = wq2
        sq1 = sq2
        wq2, sq2 = deque(), deque()
        ret += 1

    print(ret)