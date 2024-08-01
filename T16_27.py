def task_16_pattern():
	'''
	*
	* *
	* * *
	* * * *
	* * * * *
	'''
	for x in range(int(input('Enter value : '))+1):
		for j in range(x):
			print('*', end = ' ')
		print('')

def task_17_pattern():
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

def task_18_pattern():
	'''
	A
	B B
	C C C
	D D D D
	E E E E E
	'''
	for x in range(0,int(input('Enter value : '))):
		for j in range(x+1):
			print(chr(65+x), end = ' ')
		print('')

def task_19_pattern():
	'''
	* * * * *
	* * * *
	* * * 
	* *
	*
	'''
	for x in range(int(input('Enter value : ')),0,-1):
		for j in range(0,x):
			print('*',end = ' ')
		print('')

def task_20_pattern():
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

def task_21_pattern():
	'''
	        *
	      * * *
	    * * * * *
	  * * * * * * *
	* * * * * * * * *
	'''
	n = int(input('Enter value : '))
	for x in range(0,n+1):
		for j in range(n,x,-1):
			print(' ',end = ' ')
		for j in range(x+1):
			print('*',end = ' ')
		for j in range(x):
			print('*', end = ' ')
		print(' ')

def task_22_pattern():
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

def task_23_pattern():
	'''
	* * * * * * * * *
	  * * * * * * *
	    * * * * *
	      * * *
	        *
	'''
	n = int(input('Enter value : '))
	for x in range(n):
	    for y in range(x):
	        print(' ',end = ' ')
	    for y in range(n,x,-1):
	        print('*',end = ' ')
	    for y in range(x+1,n):
	        print('*',end = ' ')
	    print(' ')

def task_24_pattern():
	n = int(input('Enter value : '))
	lst = []

	for x in range(n):
		temp = [1]
		for y in range(1, x):
			temp.append(lst[x - 1][y - 1] + lst[x - 1][y])
		if x > 0:
			temp.append(1)
		lst.append(temp)

	for x in lst:
		for j in range( (n - len(x))):
			print(' ', end = '')
		for j in x:
			print(j, end=" ")
		print('')

def task_25_pattern():
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
	        k = k + 1
	        print(k,end = ' ')
	    print(' ')

def task_26_pattern():
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
	    print()

def task_27_pattern():
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

def task__choice():
	try:
		choice_tasknum = int(input('\nFor TASK 16 : 16\nFor TASK 17 : 17\nFor TASK 18 : 18\nFor TASK 19 : 19\nFor TASK 20 : 20\nFor TASK 21 : 21\nFor TASK 22 : 22\nFor TASK 23 : 23\nFor TASK 24 : 24\nFor TASK 25 : 25\nFor TASK 26 : 26\nFor TASK 27 : 27\nTo EXIT     : 28\nEnter your choice as per the given option : '))
		while (choice_tasknum >= 16 and choice_tasknum <= 28):
			match choice_tasknum:
				case 16:
					task_16_pattern()
					task__choice()
					break
				case 17:
					task_17_pattern()
					task__choice()
					break
				case 18:
					task_18_pattern()
					task__choice()
					break
				case 19:
					task_19_pattern()
					task__choice()
					break
				case 20:
					task_20_pattern()
					task__choice()
					break
				case 21:
					task_21_pattern()
					task__choice()
					break
				case 22:
					task_22_pattern()
					task__choice()
					break
				case 23:
					task_23_pattern()
					task__choice()
					break
				case 24:
					task_24_pattern()
					task__choice()
					break
				case 25:
					task_25_pattern()
					task__choice()
					break
				case 26:
					task_26_pattern()
					task__choice()
					break
				case 27:
					task_27_pattern()
					task__choice()
					break
				case 28:
					return False
		else:
			print(':::: PLEASE ENTER PROPER INPUT to user choice ::::')
			task__choice()
	except:
		print('Enter value from given')
		task__choice()