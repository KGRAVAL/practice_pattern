'''
Implement Circular Queue
You script should contain four functions

1. Front: Get the front item from queue.

2. Rear: Get the last item from queue.

3. enqueue(value)

4. dequeue()

User will be given choice to perform action from above four.
Script should be kept running until user chooses to exit.
'''

from queue import Queue as q 

class Main():
	def __init__(self):
		self.Front = self.Rear = -1
		while True:
			try:
				self.len_que = int(input('Enter maximum size of queue : '))
				break
			except:
				print("Enter valid input.")
		self.que = q(maxsize = self.len_que)

	def front_cqueue(self):
		#Front
		if self.Front == -1:
			if self.que.empty():
				print('None')
			else:
				print('Element at Front position : ', list(self.que.queue)[0])
		else:
			if self.que.empty():
				print('Queue is empty!!')
			else:
				print('Element at Front position : ', list(self.que.queue)[0])

	def rear_cqueue(self):
		#Rear
		print(len(list(self.que.queue)))
		if self.Rear == -1:
			print('None')
		else:

			if self.que.empty():
				print('Queue is empty!!')
			else:
				print('Element at Rear position : ', list(self.que.queue)[-1])

	def que_enque(self):
		#enqueue
		if self.que.full():
			print('Queue is already full ~o~ now insertion can not be done.')
		else:
			itm = input('Enter value to insert : ')
			self.que.put(itm)
			self.Rear += 1
			print('Queue elements :',list(self.que.queue))
			return self.Rear

	def que_denque(self):
		#dequeue
		if self.que.empty():
			print('Queue is already empty!! Now, no element is there in the queue .')
		else:
			print(self.que.get())
			if self.Front == -1:
				self.Front = 0
			print('Queue elements :',list(self.que.queue))
			return self.Front

	def input_user(self):
		inp_choice = 0
		print('Here are choices : \n1. Front\n2. Rear\n3. enqueue\n4. dequeue\n5. EXIT')
		try:
			inp_choice = int(input('Enter choice from given : '))
		except:
			print('Enter valid input')
			main.input_user()
		main.case_match(inp_choice)
	
	def case_match(self, inp_choice):
		while inp_choice < 6:
			match inp_choice:
				case 1:
					#Front
					print('operation : Front')	
					main.front_cqueue()
					main.input_user()
				case 2:
					#Rear
					print('operation : Rear')
					main.rear_cqueue()
					main.input_user()

				case 3:
					#enqueue
					print('operation : enqueue')
					main.que_enque()
					main.input_user()

				case 4:
					#dequeue
					print('operation : dequeue')
					main.que_denque()
					main.input_user()

				case 5:
					#exit
					exit()
		else:
			main.input_user()

main = Main()
main.input_user()