'''
Bubble sort
Use a static list 
Use bubble sort to sort this list'''

# sort_list = [531,621, 121, 4, 2, 1, 9, 20, 141]
sort_list = []

while True:
	try:
		len_list = int(input('Enter length of list : '))		
		break
	except:
		print('Please enter valid input.')

while len(sort_list) != len_list:
	try:
		element = int(input('Enter elements to insert in list : '))		
		sort_list.append(int(element))
	except:
		print('Please enter valid input.')
print('List to sort :',sort_list)

def swap(lst,a,b):
	c = lst[a]
	lst[a] = lst[b]
	lst[b] = c

def sort_bubble(lst):
	print('List to sort :' ,lst)
	for x in range(len(lst)):
		is_swap = False 
		for j in range(len(lst) - x - 1):
			if lst[j] > lst[j+1]:
				swap(lst, j, j + 1)  
				is_swap = True
				print(lst)
		print('sort ',x+1,' done')
		if not is_swap:
			break
	return lst

# sort_bubble(sort_list)
print('Sorted list  :' ,sort_bubble(sort_list))