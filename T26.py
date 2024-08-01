'''
1    2    3    4
12  13  14  5
11  16  15  6
10  9    8    7
'''

n = int(input('Enter number here : '))
list_element = [[0 for x in range(n)] for y in range(n)]
initial_val, low, high, count = 1, 0, n-1, int((n+1)/2)

for i in range(count):
    for j in range(low, high + 1):
        list_element[i][j] = initial_val
        initial_val += 1
        
    for j in range(low + 1, high + 1):
        list_element[j][high] = initial_val
        initial_val += 1
        
    for j in range(high - 1, low - 1, -1):
        list_element[high][j] = initial_val
        initial_val += 1
        
    for j in range(high - 1, low, -1):
        list_element[j][low] = initial_val
        initial_val += 1
    low += 1
    high -= 1 

for x in list_element:
    for j in x:
        print(j, end = '\t')
    print('')