import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline


def isRange(y, x):
    if y >= 0 and y < n and x >= 0 and x < m:
        return True
    else:
        return False


def melt(paper):
    q = deque()
    q.append((0, 0))
    visited = [[False] * m for _ in range(n)]
    while q:
        cy, cx = q.popleft()
        visited[cy][cx] = True
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if isRange(ny, nx) and not visited[ny][nx]:
                if paper[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                else:
                    paper[ny][nx] += 1


def check(paper):
    ret = False
    for i in range(n):
        for j in range(m):
            if paper[i][j] >= 3:
                ret = True
                paper[i][j] = 0
            elif paper[i][j] > 0:
                ret = True
                paper[i][j] = 1
    return ret


n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
cnt = 0
while check(paper):
    melt(paper)
    check(paper)
    cnt += 1

print(cnt)
