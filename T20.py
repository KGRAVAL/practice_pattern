'''
1 2 3 4 5
1 2 3 4 
1 2 3
1 2
1
'''

for x in range(int(input('Enter value : ')),0,-1):
	for j in range(1,x+1):
		print(j,end = ' ')
	print('')