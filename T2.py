'''Implement Queue

You script should contain three functions

1. enqueue
2. dequeue
3. peek 

User will be given choice to perform action from above three.

Script should be kept running until user chooses to exit.'''

from queue import Queue as q 
import queue 

class Main:
	def __init__(self):
		try:
			self.len_que = int(input('Enter maximum size of queue : '))
		except:
			print("Enter valid input.")
			Main()
		self.que = q(maxsize = self.len_que)
 
	def input_user(self):
		inp_choice = 0
		print('Here are choices : \n1. enqueue\n2. dequeue\n3. peek\n4. EXIT')
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
					#enqueue
					print('operation : enqueue')	
					main.que_enque()
					main.input_user()
				case 2:
					#dequeue
					print('operation : dequeue')
					main.que_denque()
					main.input_user()

				case 3:
					#peek
					print('operation : peek')
					main.que_peek()
					main.input_user()

				case 4:
					#exit
					exit()

		else:
			main.input_user()


	def que_enque(self):
		# print('que is full : ',self.que.full())
		if self.que.full():
			print('Queue is already full ~o~ now insretion can not be done.')
		else:
			itm = input('Enter value to insert : ')
			self.que.put(itm)
			print('Queue elements :',list(self.que.queue))
			# pass

	def que_denque(self):
		if self.que.empty():
			print('Queue is already empty!! Now, no element is there in the queue .')
		else:
			print(self.que.get())
			print('Queue :',list(self.que.queue))

	def que_peek(self):
		if self.que.empty():
			print('Queue is already empty!! Now, no element is there in the queue .')
		else:
			print('Queue elements :',list(self.que.queue))
			print('Last element of queue : ',list(self.que.queue)[-1])
			# print(self.que.get())
			# for x in self.que.queue:
			# 	print(x, end = ' ')
			# print('\n')
			# print('deque elements : ',self.que.queue)
			
main = Main()
main.input_user()