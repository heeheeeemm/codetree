n = int(input())

arr = [0] * 201

for _ in range(n):
    a, b = map(int, input().split())
    
    a = a + 100
    b = b + 100

    for i in range(a,b) :
        arr[i] += 1

print(max(arr))