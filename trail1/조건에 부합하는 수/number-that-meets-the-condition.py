A= int(input())

for i in range(1,A+1):
    b = i // 8 
    c = i % 7
    if (i % 2 == 0 and i % 4 != 0) or b % 2 == 0 or c < 4 :
        continue
    else : print(i,end = " ")

