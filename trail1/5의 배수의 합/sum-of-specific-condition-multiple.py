A, B = map(int,input().split())
cnt = 0

if A <= B :
    for i in range(A, B+1):
        if i % 5 == 0:
            cnt += i
elif A > B :
    for i in range(A, B-1, -1):
        if i % 5 == 0:
            cnt += i

print(cnt)