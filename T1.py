'''Implement Stack

Your script should contain three functions
1. push
2. pop
3. peep

User will be given choice to perform action from above three.
Script should be kept running until user chooses to exit.'''

class Main:
	def __init__(self):
		self.stack = []

	def input_user(self):
		inp_choice = 0
		print('Here are choices : \n1. push\n2. pop\n3. peep\n4. EXIT')
		try:
			inp_choice = int(input('Enter choice from given : '))
		except:
			print('Enter valid input')
			main.input_user()
		main.case_match(inp_choice)
	
	def case_match(self, inp_choice):
		while inp_choice < 5:
			match inp_choice:
				case 1:
					#push
					inp_push = input('Enter value to push : ')
					main.stack.append(inp_push)
					# print('push')
					print(self.stack)
					main.input_user()

				case 2:
					#pop
					# print('pop')
					try:
						main.stack.pop()
					except:
						print('No element are there !!')
					print(self.stack)
					main.input_user()

				case 3:
					#peep
					# print('peep')
					print(self.stack)
					try:
						index_element = int(input('Enter index : '))
					except:
						main.input_user()
					# print(len(self.stack))
					if len(self.stack) <= index_element:
						print('There are less element in stack ...')
					else:
						print(self.stack[index_element])
					main.input_user()

				case 4:
					#exit
					exit()
	#				break
		else:
			main.input_user()

main = Main()
main.input_user()