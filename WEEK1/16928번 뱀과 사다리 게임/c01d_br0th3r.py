import sys
from collections import deque
input = sys.stdin.readline

MAX_BOARD_SIZE = 104


def move(x):
    for start, end in cases:
        if start == x:
            return end
    return x


def isRange(x):
    if x > 0 and x <= 100:
        return True
    else:
        return False


def bfs(visited):
    q = deque()
    dx = [1, 2, 3, 4, 5, 6]
    q.append((1, 0))
    while q:
        cx, cnt = q.popleft()
        if cx == 100:
            print(cnt)
            break
        visited[cx] = True
        for i in dx:
            nx = cx + i
            if isRange(nx) and not visitd[nx]:
                nx = move(nx)
                visited[nx] = True
                q.append((nx, cnt+1))


n, m = map(int, input().split())
cases = []
for _ in range(n+m):
    start, end = map(int, input().split())
    cases.append([start, end])

board = [i for i in range(1, MAX_BOARD_SIZE)]
visitd = [False] * MAX_BOARD_SIZE
bfs(visitd)
