import sys
input = sys.stdin.readline


def go(s, t):
    while len(s) != len(t):
        if t[-1] == 'A':
            t = t[:-1]
        else:
            t = t[:-1]
            t = t[::-1]
    if s == t:
        return 1
    else:
        return 0


s = input().rstrip()
t = input().rstrip()

print(go(s, t))
