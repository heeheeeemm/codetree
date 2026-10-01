A,B,C,D = map(int,input().split())

if D-B<0:
    DB = D + 60 - B
    CA = C - A - 1

else:
    DB = D -B
    CA = C - A

TTIME = CA * 60 + DB

print(TTIME)