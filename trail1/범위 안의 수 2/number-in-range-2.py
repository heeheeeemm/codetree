ll = [int(input()) for _ in range(10)]

cnt = 0
ccnt = 0

for i in range(10):
    if ll[i] >= 0 and ll[i] <= 200:
        cnt += ll[i]
        ccnt += 1
        pp = cnt / ccnt

print(cnt,round(pp,1))