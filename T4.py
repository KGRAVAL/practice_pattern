'''
Selection sort

Use a static list 

Use selection sort to sort this list'''

# sort_list = [531, 2, 621, 121, 4, 2, 1, 9, 20, 141]
# sort_list = []

# while True:
# 	try:
# 		len_list = int(input('Enter length of list : '))		
# 		break
# 	except:
# 		print('Please enter valid input.')

# while len(sort_list) != len_list:
# 	try:
# 		element = int(input('Enter elements to insert in list : '))		
# 		sort_list.append(element)
# 	except:
# 		print('Please enter valid input.')

def swap(lst,a,b):
	c = lst[a]
	lst[a] = lst[b]
	lst[b] = c

# def sorting(lst):
# 	print('List to sort : ',lst)
# 	sorted_lst = []
# 	for x in range(len(lst)):
# 		j = lst.pop(lst.index(min(lst)))
# 		sorted_lst.append(j)
# 	print('Sorted List : ',sorted_lst)
# 	return sorted_lst

def sort_selection(lst):
	print('List to sort :',lst)
	print(len(lst))
	for x in range(len(lst)):
		for j in range(x+1,len(lst)):
			min_ele = min(lst[j:])
			print(lst[x] , min_ele)
			print(lst[x] == min_ele)
			print('Sorted list  :' ,lst)
			if lst[x] < min_ele:
				pass
			elif lst[x] == min_ele:
				swap(lst,lst.index(lst[x]),lst.index(min_ele))
			else:
				swap(lst,lst.index(lst[x]),lst.index(min_ele))
		# print('Sorted list  :' ,lst)
	return lst

# sorting(sort_list)
# sort_selection(sort_list)
print('Sorted list  :' ,sort_selection(sort_list))