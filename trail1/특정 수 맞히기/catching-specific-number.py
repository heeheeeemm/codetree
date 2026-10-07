arr = []

while True:
    n = int(input())
    arr.append(n)

    if n < 25 :
        print('Heigher')

    elif n > 25:
        print('Lower')

    elif n == 25:
        print("Good")
        break


