'''
Create an ATM machine

- User should be able get money out of it
- User should be able to deposite money into it
- You must ask card number and pin before any transaction
- User can get overall information about his bank account
- There should be a limit in one time transaction and total transaction in a day (Consider day as from starting of script to exit)
- Limit on number of transaction
- Let user choose the bank of ATM
- Every ATM will have some initial balance
- Every user has it's own bank
- If user takes money from an ATM other than his bank take 5% cut in withdrawl amount

Nice to have features:
- Insert, update and delete users (Generate card number and PIN randomly)
- Insert, update and delete ATMs
- Insert, update and delete banks
- Insert money into ATM (No database is needed for this it can be managed using dicts)

Hint: You can manage all this with data dictionary data type.'''

import random as r
import maskpass as m

class Main():
	def __init__(self):
		self.acc_no = card_pin = r.randint(1000,10000)
		print(f"Account numbers for default accounts are : {self.acc_no}, {self.acc_no + 1}, {self.acc_no + 2}, {self.acc_no + 3}")

		self.atm_list = {'atm1' : {'bank' : 'bank1', 'balance_avilable' : 500},
						 'atm2' : {'bank' : 'bank2', 'balance_avilable' : 40000},
						 'atm3' : {'bank' : 'bank3', 'balance_avilable' : 50000},
						 'atm4' : {'bank' : 'bank4', 'balance_avilable' : 50000},
						 'atm5' : {'bank' : 'bank1', 'balance_avilable' : 20000}}

		# datails for default accounts 
		self.accounts = {int(self.acc_no): {'name': 'abc', 'mo_num': 1234567890, 'city': 'opwert', 'acc_balance': 100000, 'bank_branch': 'bank1', 'card_no.': 'Card Not Issued', 'card_pin': 'Card Not Issued', 'transaction_onetime' : 5000, 'transaction_oneday' : 50000, 'limit_transaction' : 5},
						int(f'{self.acc_no+1}'): {'name': 'def', 'mo_num': 9876543211, 'city': 'qwert', 'acc_balance': 200000, 'bank_branch': 'bank2', 'card_no.': 453267243517, 'card_pin': 6542, 'transaction_onetime' : 5000, 'transaction_oneday' : 50000, 'limit_transaction' : 5},
						int(f'{self.acc_no+2}'): {'name': 'ghi', 'mo_num': 2876543212, 'city': 'qwert', 'acc_balance': 300000, 'bank_branch': 'bank3', 'card_no.': 'Card Not Issued', 'card_pin': 'Card Not Issued', 'transaction_onetime' : 5000, 'transaction_oneday' : 50000, 'limit_transaction' : 5},
						int(f'{self.acc_no+3}'): {'name': 'jkl', 'mo_num': 3876543213, 'city': 'qwert', 'acc_balance': 400000, 'bank_branch': 'bank4', 'card_no.': 175366174352, 'card_pin': 8724, 'transaction_onetime' : 5000, 'transaction_oneday' : 50000, 'limit_transaction' : 5}}

		# datails for admins(static admins) 
		self.admin = {1001: {'name': 'admin1', 'password': 'admin!#01'},
					  1002: {'name': 'admin2', 'password': 'admin!#12'}}

		# bank collections derived from ATMs
		self.bank = set()
		for x in self.atm_list:
			self.bank.add(self.atm_list[x]['bank'])

	def delete_user_admin(self):
		while True:	
			try:
				acc_nm1 = int(input('Enter account number : '))
				if acc_nm1 in (list(self.accounts.keys())):
					print('Account details are :: \n')
					for x,y in list(self.accounts[acc_nm1].items())[:-3]:
					    print(x,'\t:\t',y)

					v = input('Is it confirm to delete account ?? y/n : ').lower()
					if v == 'y':
						print('Deleting Account')
						del self.accounts[acc_nm1]
					elif v == 'n':
						print('Declined to delete')
						self.admin_operation()
					else:
						self.admin_operation()
						break
					break
				else :
					print('Account not available with account no. : ', acc_nm1)
					self.manage_user_admin()
			except:
				print(':::: PLEASE ENTER PROPER INPUT to user choice ::::')
	
	def update_user_admin(self):
		print('Updating user account details')
		while True:
			try:
				acc_nm = int(input('Enter account number : '))
				if acc_nm in (list(self.accounts.keys())):
					print('Account details are :: \n')
					for x,y in list(self.accounts[acc_nm].items())[:-4]:
					    print(x,'\t:\t',y)
					update_field, val_update= input('Enter name of field required updation : '),  input("Enter new value : ")
					temp = self.accounts[acc_nm][update_field]
					self.accounts[acc_nm][update_field] = val_update
					print(f"VALUE '{temp}' UPDATED WITH VALUE '{val_update}'")
					break
				else :
					print('Account not available with account no. : ', acc_nm)
			except:
				print(':::: PLEASE update user ENTER PROPER INPUT to user choice ::::')

	def manage_user_admin(self):
		try:
			crud_choice_user = int(input('\nINSERT USER : 1\nUPDATE USER : 2\nDELETE USER : 3\nGO BACK : 4\nEnter your choice here : '))
			while crud_choice_user <= 4:
				match crud_choice_user:
					case 1:
						print('INSERT USER')
						self.create_account()
						self.admin_operation()
						break

					case 2:
						print('UPDATE USER')
						self.update_user_admin()
						self.admin_operation()
						break
						
					case 3:
						print('DELETE USER')
						self.delete_user_admin()
						self.admin_operation()
						break

					case 4:
						print('Go back')
						self.admin_operation()
						return False
			else:
				print(':::: PLEASE ENTER PROPER INPUT to user choice ::::')
				self.operation_choice_user()
		except:
			print(':::: PLEASE ENTER PROPER INPUT ::::')

	def manage_atm_admin(self):
		try:
			crud_choice_atm = int(input('\nINSERT ATM : 1\nUPDATE ATM : 2\nDELETE ATM : 3\nGO BACK : 4\nEnter your choice : '))
			while crud_choice_atm <= 4:		
				match crud_choice_atm:
					case 1:
						print('INSERT ATM')
						bank_name = input('Enter bank name : ')
						while True:
							try:
								atm_balance = int(input('Enter base bank balance : '))	
								self.atm_list[r.randint(1000,10000)] = {'bank' : bank_name, 'balance_avilable' : atm_balance}
								break
							except:
								print('Enter valid amount')
								self.admin_operation()
						break
					
					case 2:
						print('UPDATE ATM')
						for x in self.atm_list.keys():
						    print(x)
						atm_nm = input('Enter name of ATM to update data : ')
						print(self.atm_list[atm_nm])
						while True:
						    try:
						        choice = int(input('For changing bank enter 1\nFor changing balance in ATM enter 2\nEnter your choice here : '))
						        if choice == 1:
						            # Change in bank
						            bank_name = input('Enter new value to Change : ')
						            self.atm_list[atm_nm]['bank'] = bank_name
						            break        
						        elif choice == 2:
						            # Change in ATM
						            print('Avaailable value in ATM is : ',self.atm_list[atm_nm]['balance_avilable'])
						            val_add = int(input('Enter value you want to add : '))
						            self.atm_list[atm_nm]['balance_avilable'] = self.atm_list[atm_nm]['balance_avilable'] + val_add
						            print('Now available value in ATM is : ',self.atm_list[atm_nm]['balance_avilable'])
						            break
						        else:
						            print('PLEASE ENTER valid INPUT')
						            self.admin_operation()
						    except:
						        print('PLEASE ENTER VALID INPUT')
						        self.admin_operation()
						break
					
					case 3:
						print('DELETE ATM')
						for x in self.atm_list.keys():
						    print(x)
						inp_name_atm = input('Enter name of ATM you want to delete : ').lower()
						if inp_name_atm in list(self.atm_list.keys()):
						    del self.atm_list[inp_name_atm]
						    print(f"ATM '{inp_name_atm}' DELETED !!")
						else:
						    print('No ATM identified !!')
						break
					
					case 4:
						print('Go back')
						self.admin_operation()
						break
			else:
				print(':::: PLEASE ENTER PROPER INPUT to user choice ::::')
		except:
			print(':::: PLEASE ENTER PROPER INPUT ::::')
	
	def manage_bank_admin(self):
		print(self.bank)
		try:
			crud_choice_bank = int(input('\nUPDATE BANK : 1\nDELETE BANK : 2\nGO BACK : 3\nEnter your choice : '))
			while crud_choice_bank <= 3:
				match crud_choice_bank:
					case 1:
						print('UPDATE bank')
						old_val = input('Enter name of bank which you want to update : ')
						update_value = input('Enter new value : ')
						for x in self.atm_list:
						    if self.atm_list[x]['bank'] == old_val:
						        self.atm_list[x].update({'bank': update_value})
						for x in self.accounts:
						    if self.accounts[x]['bank_branch'] == old_val:
						        self.accounts[x].update({'bank_branch': update_value})
						print(f'Bank updated to "{update_value}"')
						break
					case 2:
						print('DELETE bank')				
						del_bank = input('Enter name of bank to delete : ')
						for x in list(self.accounts):
						    if self.accounts[x]['bank_branch'] == del_bank:
						        del self.accounts[x]
						for x in list(self.atm_list):
						    if self.atm_list[x]['bank'] == del_bank:
						        del self.atm_list[x]
						        print(f'{del_bank} deleted')
						break
					case 3:
						print('Go back')
						break
			else:
				print(':::: PLEASE ENTER PROPER INPUT to user choice ::::')
				self.admin_operation()
		except:
			print(':::: PLEASE ENTER PROPER INPUT ::::')
			self.admin_operation()

	def admin_operation(self):
		print('ADMIN OPERATIONS')
		try:
			choice_admin_ope = int(input('\nTo MANAGE BANK\t: 1\nTo MANAGE ATM  \t: 2\nTo MANAGE USER  : 3\nTo EXIT \t: 4\nEnter your choice as per the given option : '))
			while choice_admin_ope <= 4:
				match choice_admin_ope:
					case 1:
						print('MANAGE BANK')
						self.manage_bank_admin()
						self.admin_operation()
						break				
					case 2:
						print('MANAGE ATM')
						self.manage_atm_admin()
						self.admin_operation()						
						break				
					case 3:
						print('MANAGE USER')
						self.manage_user_admin()
						self.admin_operation()
						break				
					case 4:
						print('EXIT...')
						self.operation_choice_user()
						return False
			else:
				print(':::: PLEASE ENTER PROPER INPUT to user choice ::::')
				self.admin_operation()
		except:
			print(':::: PLEASE ENTER PROPER INPUT ::::')
			self.admin_operation()

	def admin_login(self):
		login_adminid = int(input('Enter admin id here : '))
		print(login_adminid)
		if login_adminid not in list(self.admin.keys()):
			print('Admin not found !!')
		else:
			login_admin_pass = m.askpass(prompt='Enter admin password : ', mask="*")
			if login_admin_pass != self.admin[login_adminid]['password']:
				print("wrong credentialss !!!")
				self.operation_choice_user()
			else:
				self.admin_operation()

	def generate_card(self):
		card_number = r.randint(100000000000,1000000000000)
		card_pin_digit = r.randint(1000,10000)
		return card_number,card_pin_digit

	def withdraw_money(self):
		print('WITHDRAW')
		while True:
			try:
				self.amount_withdraw = int(input('Enter value you want to withdraw : '))
				if self.accounts[self.acc_num]['acc_balance'] > self.amount_withdraw:
					print('Withdrawal process .....')
					for x in self.bank:
						print(list(self.bank).index(x)+1,x)
					while True:
						try:
							bank_name = int(input('Please enter name of the bank from given list to withdraw money : '))
							if bank_name <= len(self.bank):
								print('You choose bank ', list(self.bank)[bank_name-1])
								if (self.accounts[self.acc_num]['transaction_oneday']) >= self.amount_withdraw:
									print('One day limit available')
									if (self.accounts[self.acc_num]['transaction_onetime']) >= self.amount_withdraw:
										print('One time limit available')
										if self.atm_list['atm1']['balance_avilable'] >= self.amount_withdraw:
											print('You asked for amount : ', self.amount_withdraw)
											print("Your choosen bank is : ", bank_name, list(self.bank)[bank_name - 1])
											if self.accounts[self.acc_num]['bank_branch'] != list(self.bank)[bank_name - 1]:
												withdrawal_money = self.amount_withdraw - (self.amount_withdraw * 0.5)
												print('Your withdrawal amount is : ',withdrawal_money)
											else:
												withdrawal_money = self.amount_withdraw
												print('Your withdrawal amount is : ',withdrawal_money)
											self.accounts[self.acc_num]['transaction_oneday'] -= withdrawal_money
										else:
											print('NO SUFFICIENT BALANCE in ATM')
									else:
										print('One time limit excedded')
								else:
									print('One day limit excedded')
							else:
								print('You entered value not in list given !!')
							break
						except:
							print('Please enter valid input ')
							self.withdraw_money()
				else:
					print('NO SUFFICIENT BALANCE IN YOUR ACCOUNT !!')
				break
			except:
				print('Please enter valid input.')

	def deposit_money(self):
		print('DEPOSIT')
		while True:
			try:
				self.amount = float(input('Enter value you want to deposit : '))
				while True:
					try:
						self.v_pin = m.askpass(prompt='Enter card pin : ', mask="#")
						if len(str(self.v_pin)) == 4:
							if int(self.v_pin) == self.accounts[self.acc_num]['card_pin']:
								print('card pin matched')
								self.accounts[self.acc_num].update({"acc_balance": float(self.accounts[self.acc_num]['acc_balance'] + self.amount)})
								self.show_balance()
							return False
						else:
							print('You entered wrong pin !!')
					except:
							print('Please enter valid input.')
			except:
				print('Please enter valid input.')

	def collect_card_detail(self):
		while True:
			try:
				self.card_num = int(input('Enter card number : '))
				if len(str(self.card_num)) == 12:
					while True:
						try:
							self.pin = m.askpass(prompt='Enter card pin : ', mask="#")
							if len(str(self.pin)) == 4:
								return False
							else:
								print('You entered wrong pin !!')
						except:
							print('Please enter valid input.')
					return False
				else:
					print('You entered wrong card number !!')
			except:
				print('Please enter valid input.')
		return self.card_num,self.pin

	def bank_details(self):
		print('BANK DETAILS')
		print('Your account number is : ')
		for x,y in list(self.accounts[self.acc_num].items())[:5]:
			print(f'{x}\t:\t{y}')

	def show_balance(self):
		print('CHECK BALANCE')
		print('Your account balance is : ',self.accounts[self.acc_num]['acc_balance'])

	def delete_account(self):
		print('Deleting process')
		while True:
			try:
				self.acc = int(input('Enter account number : '))
				self.mo = int(input('Enter mobile number : '))
				break
			except:
				print(':::: PLEASE ENTER PROPER INPUT to user choice ::::')
		if self.mo == self.accounts[self.acc]['mo_num']:
			for x,y in self.accounts[self.acc].items():
				print(f"{x}\t:\t{y}")
			temp = self.accounts[self.acc]
			del self.accounts[self.acc]
			print('DELETED USER HAD DETAILS : ',temp)
		else :
			print('Wrong cradentials')
			self.delete_account()

	def update_account(self):
		print('Updating account details')
		while True:
			try:
				self.acc = int(input('Enter account number : '))
				self.mo = int(input('Enter mobile number : '))
				break
			except:
				print(':::: PLEASE ENTER PROPER INPUT to user choice ::::')

		if self.mo == self.accounts[self.acc]['mo_num']:
			for x,y in self.accounts[self.acc].items():
				print(f"{x}\t:\t{y}")

			update_field = input('Enter name of field required updation : ')
			val_update = input("Enter new value : ")
			temp = self.accounts[self.acc][update_field]
			self.accounts[self.acc][update_field] = val_update
			print(f"VALUE '{temp}' UPDATED WITH VALUE '{val_update}'")
		else :
			print('Wrong cradentials')
			self.function_banking()

	def view_acc_details(self):
		print('Show Bank Details')
		while True:
			try:
				self.acc_inp = int(input('Enter account number : '))
				break
			except:
				print(':::: PLEASE ENTER PROPER INPUT to user choice ::::')
		for x,y in self.accounts[self.acc_inp].items():
			print(f"{x}\t:\t{y}")

	def create_account(self):
		self.name = input('Enter account holder name : ')
		while True:
			try:
				self.mo_num = int(input('Mo. number : '))
				if len(str(self.mo_num)) == 10:
					self.city = input('Enter city name : ')
					self.city1 = input('Enter city name of bank branch : ')
					user = int(f'{self.acc_no + len(self.accounts)}')
					self.accounts[user] = {'name' : self.name, 'mo_num' : self.mo_num, 'city' : self.city, 'acc_balance' : 0, 'bank_branch' : self.city1, 'card_no.' : 'Card Not Issued', 'card_pin' : 'Card Not Issued'}
					v = input('Do you want to issue card ?? y/n : ').lower() 
					if v == 'y':
					    print('Issuing card')
					    temp_crd_num, temp_crd_pin = list(self.generate_card())[0],list(self.generate_card())[1] 
					    print(f'Card number is : {temp_crd_num}\nCard pin is : {temp_crd_pin}')
					    self.accounts[user]['card_no.'] = temp_crd_num
					    self.accounts[user]['card_pin'] = temp_crd_pin
					elif v == 'n':
					   print('Declined to Issue card !!')
					else:
						print('Entered wrong input')				    
					print('\nAccount created with details :')
					print('Account No.\t:\t',user)
					for keys,values in self.accounts[user].items():
						print(f'{keys}\t:\t{values}')
					return False
				else:
					print('Please enter correct Mo. number...')
			except:
				print('Please enter valid input.')

	def atm_ope(self):
		self.collect_card_detail()
		while True:
			try:
				self.acc_num = int(input('Enter account number : '))
				break
			except:
				print(':::: PLEASE ENTER CORRECT INPUT ::::')

		if self.accounts[self.acc_num]:
			if self.card_num == self.accounts[self.acc_num]['card_no.']:
				if int(self.pin) == self.accounts[self.acc_num]['card_pin']:
					self.atm_operation_choice()
				else:
					print('CARD PIN NOT MATCHED !!')
					self.atm_ope()
			else:
				print('CARD NOT ISSUED')
				self.atm_ope()
		else:
			print("Account NOT FOUND !!")
			self.atm_ope()

	def atm_operation_choice(self):
		if self.accounts[self.acc_num]['limit_transaction'] >= 1:
			try:
				choice_atm_ope = int(input('\nTo DEPOSIT MONEY \t   : 1\nTo WITHDRAW MONEY \t   : 2\nTo CHECK BALANCE \t   : 3\nFor BANK DETAILS \t   : 4\nTo CANCEL ALL TRANSACTIONS : 5\n\nEnter your choice as per the given option : '))
				while choice_atm_ope <= 5:
					match choice_atm_ope:
						case 1:
							# DEPOSIT MONEY
							self.deposit_money()
							self.accounts[self.acc_num]['limit_transaction'] -= 1
							self.atm_operation_choice()
							break
						case 2:
							# WITHDRAW MONEY
							self.withdraw_money()
							self.accounts[self.acc_num]['limit_transaction'] -= 1
							self.atm_operation_choice()
							break
						case 3:
							# CHECK BALANCE
							self.show_balance()
							self.accounts[self.acc_num]['limit_transaction'] -= 1
							self.atm_operation_choice()
							break
						case 4:
							# BANK DETAILS
							self.bank_details()
							self.accounts[self.acc_num]['limit_transaction'] -= 1
							self.atm_operation_choice()
							break
						case 5:
							self.operation_choice_user()
							return False
				else:
					print(':::: PLEASE ENTER PROPER INPUT ::::')
					self.atm_operation_choice()
			except:
				print(':::: PLEASE ENTER PROPER INPUT ::::')
				self.atm_operation_choice()
		else:
			print("You can not do more transactions today !!")
			self.operation_choice_user()

	def function_banking(self):
		try:
			banking_ope_choice = int(input('\nOptions are...\n1 : VIEW ACCOUNT\n2 : ADD/CREATE ACCOUNT\n3 : UPDATE ACCOUNT\n4 : DELETE ACCOUNT\n5 : To EXIT\n\nEnter your choice as per the given option : '))
			while banking_ope_choice <= 5:
				match banking_ope_choice:
					case 1:
						print('VIEW ACCOUNT')
						self.view_acc_details()
						self.function_banking()
						break
					case 2:
						print('ADD/CREATE ACCOUNT')
						self.create_account()
						self.function_banking()
						break
					case 3:
						print("UPDATE ACCOUNT")
						self.update_account()
						self.function_banking()
						break
					case 4:
						print('DELETE ACCOUNT')
						self.delete_account()
						self.function_banking()
						break
					case 5:
						print('BACK...')
						self.operation_choice_user()
						return False

			else:
				print(':::: PLEASE ENTER PROPER INPUT to user choice ::::')
				self.function_banking()
		except:
			print(':::: PLEASE ENTER PROPER INPUT ::::')
			self.function_banking()
	
	def operation_choice_user(self):
		try:
			choice_user_ope = int(input('\nFor BANKING FUNCTIONALITY : 1\nFor ATM FUNCTIONALITY  \t  : 2\nFor ADMIN USAGE  \t  : 3\nTo EXIT \t\t  : 4\nEnter your choice as per the given option : '))
			while choice_user_ope <= 4:
				match choice_user_ope:
					case 1:
						print('BANKING FUNCTIONALITY')
						self.function_banking()
						break
					case 2:
						print('ATM FUNCTIONALITY')
						self.atm_ope()
						break
					case 3:
						print('ADMIN FUNCTIONALITY')
						self.admin_login()
						break
					case 4:
						print('EXIT...')		
						return False
			else:
				print(':::: PLEASE ENTER PROPER INPUT to user choice ::::')
				self.operation_choice_user()
		except:
			print(':::: PLEASE ENTER PROPER INPUT ::::')
			self.operation_choice_user()

main = Main()
main.operation_choice_user()			#done