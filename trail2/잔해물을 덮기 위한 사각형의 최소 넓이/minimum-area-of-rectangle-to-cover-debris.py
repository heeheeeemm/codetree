x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

# 원래 첫 번째 직사각형 크기
width = x2 - x1
height = y2 - y1

# 두 번째 직사각형이 첫 번째를 완전히 덮음
if a1 <= x1 and x2 <= a2 and b1 <= y1 and y2 <= b2:
    print(0)

# 위아래를 전부 덮고, 왼쪽을 덮음
elif b1 <= y1 and y2 <= b2 and a1 <= x1 < a2:
    print((x2 - a2) * height)

# 위아래를 전부 덮고, 오른쪽을 덮음
elif b1 <= y1 and y2 <= b2 and a1 < x2 <= a2:
    print((a1 - x1) * height)

# 좌우를 전부 덮고, 아래쪽을 덮음
elif a1 <= x1 and x2 <= a2 and b1 <= y1 < b2:
    print(width * (y2 - b2))

# 좌우를 전부 덮고, 위쪽을 덮음
elif a1 <= x1 and x2 <= a2 and b1 < y2 <= b2:
    print(width * (b1 - y1))

# 나머지는 원래 크기 그대로
else:
    print(width * height)