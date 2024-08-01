'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

for x in range(1,int(input('Enter value : '))+1):
	for j in range(1,x+1):
		print(j, end = ' ')
	print('')