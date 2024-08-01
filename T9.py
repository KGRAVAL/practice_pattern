# Find diterminent of 3x3 matrix

# matrix_list = [[[1, 2, 3],[4, 5, 6],[7, 8, 9]]]
# matrix_list = [[[9, 8, 7],[6, 5, 4],[3, 2, 1]]]
# matrix_list = [[[1, 2, 3],[4, 5, 6]], [['a1', 'b1', 'c1'],['a2', 'b2', 'c2'],['a3', 'b3', 'c3']]]
matrix_list = []

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

# matrix determinant using numpy
def determinant_matrix_bynumpy(m1):
	import numpy as np

	for t in m1:
		print(t)
	m1_row, m1_col =  len(m1), len(m1[0])

	if m1_row == m1_col:
		print(f'Determinant for the Matrix with {m1_row} row and {m1_col} column is : ', end = '')
		n_arr = np.array(m1)
		determinant = np.linalg.det(n_arr) 
		return int(determinant)

	else:
		err = (f'Determinant for the Matrix with {m1_row} row and {m1_col} column can not be find')
		return err

# matrix properties using numpy
def other_details_matrix(m1):
	import numpy as np
	m1_row, m1_col =  len(m1), len(m1[0])

	while True:
		try:
			power_matrix = int(input('\nEnter value of power for matrix : '))
			break
		except:
			print('Please enter valid input.')

	for t in m1:
		print(t)

	# Rank of a matrix
	print("Rank of m1:", np.linalg.matrix_rank(m1))
	 
	# Trace of matrix m1
	print("\nTrace of m1:", np.trace(m1))
	 
	# Inverse of matrix m1
	if m1_row == m1_col:
		print("\nInverse of m1:\n", np.linalg.inv(m1))
	else:
		print(f'Inverce for the Matrix with {m1_row} row and {m1_col} column can not be find')
	
	# Power of matrix m1
	if m1_row == m1_col:
		print(f"\nMatrix m1 raised to power {power_matrix}:\n",
		           np.linalg.matrix_power(m1, power_matrix))
	else:
		print(f'Power for the Matrix with {m1_row} row and {m1_col} column can not be find')
	 
# matrix determinant without numpy
def determinant_matrix(m1):
	for t in m1:
		print(t)
	m1_row, m1_col =  len(m1), len(m1[0])
	temp = []

	if m1_row == m1_col:
		print(f'Determinant for the Matrix with {m1_row} row and {m1_col} column is : ', end = '')
		
		if m1_row == 1:
			determinant = m1[0][0]
			
		elif m1_row == 2:
			determinant = eval(f'''((m1[0][0]*m1[1][1]) - (m1[0][1]*m1[1][0]))''')
		# else:
		elif m1_row == 3:
			determinant = (m1[0][0] * (m1[1][1] * m1[2][2] - m1[2][1] * m1[1][2])) - (m1[0][1] * (m1[1][0] * m1[2][2] - m1[1][2] * m1[2][0])) + (m1[0][2] * (m1[1][0] * m1[2][1] - m1[1][1] * m1[2][0]))
		else:
			pass
		return determinant
	else:
		err = (f'Determinant for the Matrix with {m1_row} row and {m1_col} column can not be find')
		return err

op_diterminent = determinant_matrix(matrix_list[0])
print(op_diterminent)