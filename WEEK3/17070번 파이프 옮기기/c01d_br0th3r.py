import sys
input = sys.stdin.readline


def go(y, x, dir):
    global ret

    if y == n - 1 and x == n - 1:
        ret += 1
        return

    if dir == 0 or dir == 2:
        if x + 1 < n and house[y][x+1] == 0:
            go(y, x+1, 0)

    if dir == 1 or dir == 2:
        if y + 1 < n and house[y+1][x] == 0:
            go(y+1, x, 1)

    if y + 1 < n and x + 1 < n:
        if house[y][x+1] == 0 and house[y+1][x] == 0 and house[y+1][x+1] == 0:
            go(y+1, x+1, 2)


n = int(input())
ret = 0
house = []
for _ in range(n):
    house.append(list(map(int, input().split())))
go(0, 1, 0)
print(ret)
