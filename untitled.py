
class Employee:
	
	raise_amount =0
	num_of_emp = 0

	def __init__ (self, first, last, pay):
		 self.first = first
		 self.last = last
		 self.pay = pay
		 self.email = str.lower(first+'.'+last+'@company.com')
		 Employee.num_of_emp += 1

	def fullname ( self ):
		
		print  ("{} {}".format(self.first,self.last))

	def pay_raise (self):
		self.pay = int(self.pay * self.raise_amount)
		 



'''Inheritance'''

class Developer(Employee):
	raise_amount = 0

	pass



class Manager(Employee):

	# MANAGERS ARE EMPLOYEES TOO, SO ALONG WITH ALL PROPERTIES FROM PARENT CLASS EMPLOYEES 
	# HERE WE PASS LIST AS EMPLOYESS, here we takke all the basic properties for emp object from Employee class


	def __init__ (self, first, last, pay, employees= None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

			#ADD & REMOVE EMPLOYEE TO MANAGER SUPERVISION

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def rem_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)


# print the managers list 
	def emp_list(self):
		for emp in self.employees:
			print (emp.fullname())
















# Employees

emp1= Developer("faisal", "khan", 20000)
emp2 = Developer('Test', "user", 4000)
emp3 = Employee ('ali','khna',2000)
#print ( "this is the email of emp1: {0} \nthis is the email of Employee 2: {1}".format(emp1.email, emp3.email) )


 

# Managers

mgr1= Manager("AADIL","KHAN", 9000, [emp1])

mgr1.add_emp(emp2)

#print(mgr1.emp_list())

mgr1.rem_emp(emp1)

print("__________", '\n',mgr1.emp_list(), '_________')
