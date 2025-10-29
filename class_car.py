class Car:
	def __init__(self, gas=0):
		self._gas = gas
		self._milage = 10
		self._distance = 0
		self._gas_consumed = 0

	def addgas(self,fuel=0):
		self._gas = self._gas + fuel
		return self._gas
		print(f'Gas added now {self._gas}')

	def drive(self, distance=0):
		self._distance = int(self._distance + distance)
		self._gas_consumed = int(self._distance / self._milage)
		self._gas = int(self._gas - self._gas_consumed)


	def getgaslevel(self):
		return f"Car Fuel Tank has now {self._gas} gallons of gas left"

	def __str__(self):
		return f'Gas level: {self._gas}\nEfficiency: {self._milage}\nDistance covered: {self._distance}\nGas Consumed: {self._gas_consumed}\n-------------------'




hybrid=Car(50)
print(hybrid)
hybrid.addgas(10)
print(hybrid)
hybrid.drive(100)
print(hybrid)
print(hybrid.getgaslevel())
