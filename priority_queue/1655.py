import sys
import heapq


# 중간 값보다 작은 값을 최소 힙(left)에 유지
# 중간 값보다 큰 값을 최대 힙(right)에 유지
def solve(m, left, right) :
    if len(left) == len(right) :
        heapq.heappush(left, (-m, m))
    else :
        heapq.heappush(right, (m, m))

    if right and left[0][1] > right[0][1] :
        min_m = heapq.heappop(right)[1]
        max_m = heapq.heappop(left)[1]
        heapq.heappush(left, (-min_m, min_m))
        heapq.heappush(right, (max_m, max_m))
    return left, right
if __name__ == "__main__" :
    n = int(sys.stdin.readline())

    # left : 최소 힙
    # right: 최대 힙
    left = list()
    right = list()

    for i in range(n) :
        m = int(sys.stdin.readline())

        left, right = solve(m, left, right)
        print(left[0][1])