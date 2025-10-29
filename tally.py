class Counter:
	def __init__(self,inital_value=0):
		self._value=inital_value

	def getvalue(self):
		return self._value

	def click(self):
		self._value=self._value+1

	def clear(self):
		self._value=0

	def setlimit(self,maximum):
		if self._value <= maximum:
			print('Limit exceed')

	def undo(self):
		self._value = self._value - 1
		print(f"You undo the click, new value is now {self._value}")

	def __str__(self):
		return str(self._value)





counter1 = Counter()
counter1.click()
counter1.click()
counter1.click()
counter1.click()
counter1.click()
counter1.click()
print(counter1)
counter1.undo()
print(counter1)
counter1.setlimit(10)
counter1.click()
counter1.click()
counter1.click()
counter1.click()
counter1.click()
counter1.click()
print(counter1)


