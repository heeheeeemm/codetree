A, B = map(int,input().split())
cnt = 0

for i in range(A, B+1):
    cnt += i

print(cnt)
