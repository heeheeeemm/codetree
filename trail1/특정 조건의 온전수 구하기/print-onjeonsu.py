N = int(input())

for i in range(1,N+1):
    if N < 10:
        if i % 2 == 0 or i == 5 or (i % 3 == 0 and i % 9 != 0):
            continue
        else: print(i, end = " ")

    elif N < 100 :
        if i % 2 == 0 or i // 10 == 5 or (i % 3 == 0 and i % 9 != 0):
            continue
        else: print(i, end = " ")
    else : 
        if i % 2 == 0 or i // 10 == 5 or (i % 3 == 0 and i % 9 != 0):
            continue
        else: print(i, end = " ")