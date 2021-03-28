import sys
input = sys.stdin.readline


def go(cx):
    global ret
    if cx == n:
        ret += 1
        return

    for i in range(n):
        if not (row[i] or diagonal_left[cx+i] or diagonal_right[cx-i+n-1]):
            row[i] = True
            diagonal_left[cx+i] = True
            diagonal_right[cx-i+n-1] = True
            go(cx+1)
            row[i] = False
            diagonal_left[cx+i] = False
            diagonal_right[cx-i+n-1] = False


n = int(input())
row = [False] * 16
diagonal_left = [False] * 32
diagonal_right = [False] * 32
ret = 0

go(0)
print(ret)
