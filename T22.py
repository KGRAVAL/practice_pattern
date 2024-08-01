'''
        1
      2 3 2
    3 4 5 4 3
  4 5 6 7 6 5 4
5 6 7 8 9 8 7 6 5
'''

n = int(input('Enter value : '))

for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end="")
    
    for j in range(i, i * 2):
        print(j, end=" ")
    
    for j in range(i * 2 - 2, i - 1, -1):
        print(j, end=" ")
    print('')