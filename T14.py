# Find LCM and GCD of a number

import math
import sys as s

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

def lcm_number(num):
	num_fact = []
	for x in num:
		if x > 0:
			pass
		elif x < 0:
			num[num.index(x)] = abs(x)
		elif x == 0:
			num.remove(x)
		else:
			pass

	temp1 = num[0]
	for x in num[1:]:
		temp1 = int((temp1*x)/gcd_number([temp1,x]))
	return temp1

def gcd_number(num = []):
	for x in num:
		if x == 0:
			num.remove(x)
		else:
			pass
	temp = []
	for x in num:
	    temp.append(num_find_factor(x))
	# 'GCD of given list : ',
	return max(set.intersection(*temp))

a = True
while a:
	try:
		choice = int(input('Enter 1 to find LCM \nEnter 2 to find GCD \nEnter 3 to EXIT \nEnter your choice : '))
		while choice <= 3:
			match choice:
				case 1:
					num = list(map(int,input('Enter a number to calculate : ').split()))
					# print("Finding LCM")
					print("Finding LCM for : ",num)
					print('LCM of given list : ',lcm_number(num))
					break
				case 2:
					num = list(map(int,input('Enter a number to calculate : ').split()))
					# print("Finding GCD")
					print('GCD of given list : ',gcd_number(num))
					break
				case 3:
					print("EXIT")
					a = False
					break
		else:
			print('Entered wrong inputs!!')
			a = True
	except:
		print('Please enter a valid input ...')