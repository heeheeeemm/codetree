N = int(input())

ll = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N):
    if ll[i] == 1 :
        cnt += 1
    elif ll[i] % 2 != 0 and ll[i] % 3 == 0:
        cnt += ll[i]

print(cnt)


