# Diamond pattern

n = int(input('Enter value : '))

for i in range(n):
	for j in range(n,i+1,-1):
		print(' ',end = ' ')
	for j in range(i+1):
		print('*',end = ' ')
	for j in range(i):
		print('*', end = ' ')
	print(' ')

for i in range(1,n):
	for j in range(i):
		print(' ',end = ' ')
	for j in range(n,i,-1):
		print('*',end = ' ')
	for j in range(i+1,n):
		print('*',end = ' ')
	print(' ')