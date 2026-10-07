n = int(input())
arr = []

while True:
    b = n % 2
    arr.append(b)
    n = n // 2

    if n < 2:
        arr.append(n)
        break

for i in range(len(arr)-1,-1,-1):
    print(arr[i],end='')

