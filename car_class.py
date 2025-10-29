class Car():
	def __init__(self, gas=0):
		self._gas = gas
		self._distance = 0
		self._consumed = 0
		self._milage = 10

	def addgas(self, gas=0):
		self._gas = self._gas + gas
		print(f'tank has now {self._gas}. ')


	def drive(self,distance=0):
		if self._gas > 0:
			self._distance = self._distance + distance
			self._consumed = self._distance / self._milage
			print(f"you drove {self._distance} miles consumed {self._consumed} gallon of gas")
		else:
			print('you can not drive, tank is empty')

	def gasleft(self):
		self._gas = self._gas - (self._consumed)
		return self._gas, print(f"you have {self._gas} left")



car1 = Car(25)		
car1.addgas(50)
car1.drive(100)
car1.gasleft()


