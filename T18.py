'''
A
B B
C C C
D D D D
E E E E E
'''

# print(chr(65))

for x in range(0,int(input('Enter value : '))):
	for j in range(x+1):
		print(chr(65+x), end = ' ')
	print('')