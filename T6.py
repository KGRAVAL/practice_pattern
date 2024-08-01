'''
Insertion sort
Use a static list 
Use insertion sort to sort this list'''

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
		sort_list.append(element)
	except:
		print('Please enter valid input.')

def swap(lst,a,b):
	c = lst[a]
	lst[a] = lst[b]
	lst[b] = c

def sort_insertion(lst):
	print('List to sort :' ,lst)
	for k in lst:	
		if len(lst[lst.index(k)+1:]) != 0:
			min_ele = min(lst[lst.index(k)+1:])
			# print(min_ele)
			swap(lst, lst.index(k), lst.index(min_ele))
			print(lst)
	return lst

# sort_insertion(sort_list)
print('Sorted List  :' ,sort_insertion(sort_list))