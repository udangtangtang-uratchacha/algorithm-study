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
        go(n//3, sy, sx)
        go(n//3, sy, sx + n//3)
        go(n//3, sy, sx + (n//3) * 2)

        go(n//3, sy + n//3, sx)
        go(n//3, sy + n//3, sx + n//3)
        go(n//3, sy + n//3, sx + (n//3) * 2)

        go(n//3, sy + (n//3) * 2, sx)
        go(n//3, sy + (n//3) * 2, sx + n//3)
        go(n//3, sy + (n//3) * 2, sx + (n//3) * 2)

    else:
        if flag == -1:
            cnt[0] += 1
        elif flag == 0:
            cnt[1] += 1
        else:
            cnt[2] += 1


n = int(input())
arr = []
cnt = [0, 0, 0]
for _ in range(n):
    arr.append(list(map(int, input().split())))
go(n, 0, 0)
for c in cnt:
    print(c)
