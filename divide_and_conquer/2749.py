import sys
input = sys.stdin.readline
# 피사노 주기 이용
# m = 10^k (k > 2) 일때 주기는 15*10^(k-1)

m = 1000000
p = int(15 * (m / 10))

def solve(n) :
    s1, s2 = 0, 1
    for _ in range(n) :
        s1, s2 = s2%m, (s1 + s2)%m
    return s1

if __name__ == "__main__" :
    n = int(input())

    print(solve(n%p))
