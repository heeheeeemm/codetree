N = int(input())

ll = [int(input()) for _ in range(N)]
cnt = 0

for i in range(N):
    cnt += ll[i]
pp = cnt / N

print(cnt,round(pp,1))