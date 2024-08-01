# Find the factors of a number opimize it as much as you can

import math
while True:
	try:
		num = int(input('Enter a number to find factor : '))
		break
	except:
		print('Please enter a valid input ...')

def num_find_factor(num):
	factor_num = set()
	if num != 0:
		if num < 0:
			factor_num.add(num)
			for x in range(math.floor(num/2),-math.floor(num/2)+1):
				if x != 0:
					if (num % x) == 0:
						factor_num.add(x)
			factor_num.add(-num)
			return factor_num
		else:
			for x in range(1,math.floor(num/2)+1):
				if (num%x) == 0:
					factor_num.add(x)
			factor_num.add(num)
			return factor_num
	else :
		err = (f'{num} HAS NO FACTORS')
		return err

print(f'You entered numbe : {num}\nNumber {num} is having {len(num_find_factor(num))} factors  :  {num_find_factor(num)}')
