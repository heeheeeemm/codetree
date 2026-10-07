n = int(input())

arr = [[0]*201 for _ in range(201)]

for _ in range(n):
    x1, y1 = map(int,input().split())

    x1 = x1 + 100
    y1 = y1 + 100

    for i in range(x1,x1+8):
        for j in range(y1,y1+8):
            arr[i][j] = 1

cnt = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)
