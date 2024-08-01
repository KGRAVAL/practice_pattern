'''
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

n = int(input('Enter value : '))

for x in range(n):
    for y in range(x):
        print(' ',end = ' ')
    for y in range(n,x,-1):
        print('*',end = ' ')
    for y in range(x+1,n):
        print('*',end = ' ')
    print(' ')