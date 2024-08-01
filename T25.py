'''
1
2 3
4 5 6
7 8 9 10
'''
n = int(input('Enter value : '))

k = 0

for i in range(n):
    for j in range(i+1):
        k += 1
        print(k,end = ' ')
    print(' ')