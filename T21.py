'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''
n = 5
n = 7
n = int(input('Enter value : '))

for x in range(0,n+1):
        for j in range(n,x,-1):
                print(' ',end = ' ')
        for j in range(x+1):
                print('*',end = ' ')
        for j in range(x):
                print('*', end = ' ')
        print(' ')