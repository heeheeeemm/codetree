n = int(input())

arr = [0] * 2001
start = 1000

for _ in range(n):
    a, b = input().split()
    a = int(a)

    for i in range(a):
        if b == "R":
            arr[start] += 1
            start += 1
        elif b == "L":
            start -= 1
            arr[start] += 1

cnt = 0

for i in range(2001):
    if arr[i] >= 2:
        cnt += 1

print(cnt)