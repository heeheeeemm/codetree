A, B = map(int,input().split())
cnt = 0
ccnt = 0

for i in range(A, B+1):
    if i % 5 == 0 or i % 7 == 0:
        cnt += i
        ccnt += 1

        pp = cnt / ccnt

print(cnt,round(pp,1))
