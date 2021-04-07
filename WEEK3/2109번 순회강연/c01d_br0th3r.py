import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    p, d = map(int, input().split())
    arr.append((d, p))

arr = sorted(arr, key=lambda x: x[0])
pq = []

for a in arr:
    heapq.heappush(pq, a[1])
    if len(pq) > a[0]:
        heapq.heappop(pq)

print(sum(pq))
