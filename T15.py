'''
Rearrange array such that A[A[i]] is set i for every element A[i]
Note: all the element in the array are unique and positive
Input:[1, 3, 4, 2, 0]
Output:[4, 0, 3, 1, 2]

Explanation:

A[0] = 1, A[1] becomes 0
A[1] = 3, A[3] becomes 1
A[2] = 4, A[4] becomes 2
A[3] = 2, A[2] becomes 3
A[4] = 0, A[0] becomes 4
'''

A = []

while True:
	try:
		len_list = int(input("Enter length of list : "))
		while True:
			try:
				for x in range(len_list):
					j = int(input(f'Enter {x+1}th value to add in list : '))
					if j < 0 :
						print('None possitive value !!')
						# break		
					else:
						if j >= len_list:
							print('Enter number in list which is less then the length of list.')
						else:
							A.append(j)
				break		
			except:
				print('Error')
				print('Enter again')
		print(A)
		break
	except:
		print('YOU ENTERED VALUE WHICH IS NOT PROPER !!')
try:		
	temp = A.copy()
	for x in A:
		temp[A[A.index(x)]] = A.index(x)
except:
	print('Error accured in operation !!')

print(f'\n\nINPUT LIST\t:\t{A}')
print(f'OUTPUT LIST\t:\t{temp}')