# Palindrome number

class Palindrome:
	def __init__(self):
		self.value = input('Enter value to check weather it is palindrome or not : ')

	def palindrome_check(self):
		
		if list(str(self.value)) == list(str(self.value))[::-1]:
		    print(f'Entered value {self.value} is palindrom ')
		else:
		    print(f'Entered value {self.value} is not palindrom ')
	
main = Palindrome()
main.palindrome_check()