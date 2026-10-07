n, k = map(int, input().split())

arr = [0] * n

for _ in range(k):
    a, b = map(int,input().split())

    for i in range(a - 1, b):
        arr[i] += 1

print(max(arr))
