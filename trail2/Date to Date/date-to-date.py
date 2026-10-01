m1, d1, m2, d2 = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
ddd = days[m1:m2+1]


if d2 - d1 >= 0:
    if m2 - m1 >=2:
        for i in range(len(days)):
            cnt = 0
            for i in range(m1, m2+1):
                cnt += ddd[i]
            dd = (days[m1]- d1 + 1) + d2 + cnt
    else: dd = (days[m1] - d1 + 1 )+ d2


print(dd) 

