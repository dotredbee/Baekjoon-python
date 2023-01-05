import sys
if __name__ == "__main__" :
    n, k = map(int, sys.stdin.readline().split())

    temps = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n) :
        w, v = map(int, sys.stdin.readline().split())

        for j in range(1, k + 1) :
            if j < w :
                temps[i+1][j] = temps[i][j]
            else :
                temps[i+1][j] = max(v + temps[i][j - w], temps[i][j])
    print(temps[n][k])
