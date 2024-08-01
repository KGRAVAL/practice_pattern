'''
Binary search

Use a static list 

Use Binary search to find element asked by user

Use one of the sorting algorithm that you have developed to sort list here'''

# sort_list = [531, 2, 621, 121, 4, 2, 1, 9, 20, 1, 141]
# import T4 as sort

sort_list = []

while True:
	try:
		len_list = int(input('Enter length of list : '))	
		search_element = int(input('Enter value to search in list : '))
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

def sorting(lst):
	sorted_lst = []
	for x in range(len(lst)):
		j = lst.pop(lst.index(min(lst)))
		sorted_lst.append(j)
	return sorted_lst

def search_binery(lst,search_element):
	sorted_lst = sorting(lst)
	import math
	hf_val = math.floor(len(sorted_lst)/2)
	val_half = sorted_lst[math.floor(len(sorted_lst)/2)]
	if search_element in sorted_lst:
		if int(val_half) == int(search_element):
			return sorted_lst.index(search_element)
		elif int(val_half) < int(search_element):
			search_binery(sorted_lst[hf_val:],search_element)
			return sorted_lst.index(search_element)
		elif int(val_half) > int(search_element):
			search_binery(sorted_lst[:hf_val],search_element)
			return sorted_lst.index(search_element)
	else:
		print('No element in list is there you are searching')

#  sort_binery(sort_list)
print('Element at index :' , search_binery(sort_list,search_element))