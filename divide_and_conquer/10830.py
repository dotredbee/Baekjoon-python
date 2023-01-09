import sys
input = sys.stdin.readline
MOD = 1000

def mul(proc_1, proc_2) :
    global n
    ret = [[0] * n for _ in range(n)]

    for idx in range(n) :
        for row in range(n) :
            tmp = proc_1[row][idx]
            for col in range(n) :
                ret[row][col] += tmp * proc_2[idx][col]
                ret[row][col] %= MOD
    return ret

def solve(proc, exp) :
    if exp == 1 :
        return proc

    ret = solve(proc, exp // 2)

    ret = mul(ret, ret)

    if exp % 2 :
        ret = mul(ret, proc)

    return ret

if __name__ == "__main__" :
    n, b = map(int, input().split())

    proc = [list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            proc[i][j] %= MOD

    ret = solve(proc, b)

    for _, row in enumerate(ret, 1) :
        print(*row)

