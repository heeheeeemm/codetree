n = int(input())
cnt = 0
b = n

for i in range(1, 50001):
    b = b // i
    cnt += 1

    if b <= 1:
        print(cnt)
        break