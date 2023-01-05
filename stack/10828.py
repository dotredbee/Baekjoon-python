import sys

def solve(cmd, stack) :
    if cmd[0] == "push" :
        stack.append(cmd[1])
    elif cmd[0] == "pop" :
        if len(stack) == 0 : print(-1)
        else : print(stack.pop())
    elif cmd[0] == "size" :
        print(len(stack))
    elif cmd[0] == "empty" :
        if len(stack) == 0 : print(1)
        else : print(0)
    elif cmd[0] == "top" :
        if len(stack) == 0 : print(-1)
        else : print(stack[-1])

if __name__ == "__main__" :
    n = int(sys.stdin.readline())

    stack = list()
    for _ in range(n) :
        cmd = sys.stdin.readline().split()
        solve(cmd, stack)