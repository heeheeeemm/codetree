m1, d1, m2, d2 = map(int, input().split())

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

date1 = 0
date2 = 0

for i in range(1, m1):
    date1 += days[i]
date1 += d1

for i in range(1, m2):
    date2 += days[i]
date2 += d2

diff = date2 - date1

print(week[diff % 7])