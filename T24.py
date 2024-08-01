'''
            1
         1   1
       1   2   1
     1   3   3    1
   1  4    6   4   1
 1  5   10   10  5   1
 '''

n = int(input('Enter value : '))

lst = []

for x in range(n):
    temp = [1]
    for y in range(1, x):
        temp.append(lst[x - 1][y - 1] + lst[x - 1][y])
    if x > 0:
        temp.append(1)
    lst.append(temp)

for x in lst:
    for j in range( (n - len(x))):
        print(' ', end = '')
    for j in x:
        print(j, end=" ")
    print('')