import sys
input = sys.stdin.readline


def go(n, sy, sx):
    check = False
    flag = arr[sy][sx]
    for i in range(sy, sy + n):
        for j in range(sx, sx + n):
            if arr[i][j] != flag:
                check = True
                break
        if check:
            break

    if check:
        print('(', end='')
        go(n//2, sy, sx)
        go(n//2, sy, sx + n//2)
        go(n//2, sy + n//2, sx)
        go(n//2, sy + n//2, sx + n//2)
        print(')', end='')
    else:
        print(flag, end='')
        return flag


n = int(input())
arr = []
for _ in range(n):
    inp = input().rstrip()
    tmp = []
    for i in inp:
        tmp.append(int(i))
    arr.append(tmp)

go(n, 0, 0)
