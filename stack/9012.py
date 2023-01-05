
def solve(s) :
    stack = list()

    for _, c in enumerate(s, 1) :
        if c == "(" :
            stack.append(c)
        elif c == ")" :
            if len(stack) == 0 :
                print("NO")
                return
            stack.pop()

    if len(stack) == 0 :
        print("YES")
    else :
        print("NO")

if __name__ == "__main__" :
    n = int(input())

    for _ in range(n) :
        s = input()
        solve(s)