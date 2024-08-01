# '''
# Matrix Multiplication

# 1. Take two 3x3 matrix.
# 2. take user inputs to fill it up.
# 3. Multiply them both and store it in another 3x3 matrix.
# 4. Display the result.'''

matrix_list = []
# matrix_list = [[[1, 2, 3],[4, 5, 6],[7, 8, 9]], [[9, 8, 7],[6, 5, 4],[3, 2, 1]]]
# matrix_list = [[[1, 4, 7],[2, 5, 8],[3, 6, 9]],[[9, 6, 3],[8, 5, 2],[7, 4, 1]]]
# matrix_list = [[[3],[1],[4]],[[4, 2, 6],[3, 5, 8]]]

while True:
	try:
		num_matrix = int(input('Enter number of matrix : '))
		break
	except:
		print('Please enter valid input.')

for x in range(num_matrix):
	nm = f'matrix_{x+1}'
	print(nm)
	while True:
		try:
			row = int(input(f'Enter value of row for matrix {x+1} : '))
			col = int(input(f'Enter value of collumn for matrix {x+1} : '))
			break
		except:
			print('Please enter valid input.')

	matrix = [[int(input(f'Enter value row vise to add in matrix {x+1} : ')) for _ in range(row)] for j in range(col)]
	matrix_list.append(matrix)
print('Matrix are :')
for u in matrix_list:
	for t in u:
		print(t, end = '')
	# print(matrix_list.index(u))
	print('')

def matrix_multiply(m1, m2):
	import math
	m1_row, sm, m1_col, m2_row, m2_col, mult = len(m1[0]), 0, len(m1), len(m2[0]), len(m2), []
	
	print(f'Matrix multiplication for {m1_row} * {m1_col} and {m2_row} * {m2_col} matrix...')

	if m1_col == m2_row:
		print(f'Matrix multiplication output for matrix will be of order {m1_row} * {m2_col}')
	
		mult = [[sum(a * b for a, b in zip(m1_row, m2_col)) 
						for m2_col in zip(*m2)]
								for m1_row in m1]
		return mult

	else:
		err = (f'Matrix multiplication can not be done for matrix with indices  {m1_row} * {m1_col} and {m2_row} * {m2_col}')
		# print(err)
		return err
		


op_multiply = matrix_multiply(matrix_list[0],matrix_list[1])
# x = matrix_multiply(matrix_list[1],matrix_list[0])
print(op_multiply)