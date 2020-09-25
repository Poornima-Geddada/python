n=int(input('enter number '))
for i in range(n):
    if i==0 or i==n-1:
        for k in range(n):
            print('*',end='')
    else:
        print('*',end='')
        for l in range(n-2):
            print(' ',end='')
        print('*',end='')
    print()
