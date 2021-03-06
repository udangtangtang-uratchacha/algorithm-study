import sys
input = sys.stdin.readline


def binarySearch(question):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if poke_sorted[mid][1] < question:
            left = mid + 1
        else:
            right = mid - 1

    return poke_sorted[left][0]


n, m = map(int, input().split())
poke = dict()
for i in range(n):
    inp = input().rstrip()
    poke[i+1] = inp
poke_sorted = sorted(poke.items(), key=(lambda x: x[1]))
for _ in range(m):
    question = input().rstrip()
    if question.isdigit():
        print(poke[int(question)])
    else:
        print(binarySearch(question))
