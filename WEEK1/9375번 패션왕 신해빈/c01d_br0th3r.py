import sys
input = sys.stdin.readline

tc = int(input())
while tc:
    n = int(input())
    d = dict()
    for _ in range(n):
        val, key = input().split()
        if key in d:
            d[key].append(val)
        else:
            d[key] = [val]
    ret = 1
    for key in d:
        ret *= len(d[key]) + 1
    print(ret-1)
    tc -= 1
