A, B = map(int,input().split())
cnt = 1

for i in range(1,B+1):
    if i % A == 0 :
        cnt *= i

print(cnt)