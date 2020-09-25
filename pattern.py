n=int(input('enter a number '))
for i in range(1,n+1):
    for k in range(0,n-i):
        print(' ',end=' ')
    for j in range(1,n+1):
        print('*',end=' ')
    print()
