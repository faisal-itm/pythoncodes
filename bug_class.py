class Bug:
	def __init__(self,position:int):
		self.position = position
		self.direction = True
	
	def move(self):
		if self.direction:
			self.position += 1
		else:
			self.position -= 1	

	def turn(self):
		if self.direction:
			self.direction = False
		else:
			self.direction = True	

	def __str__(self):
		return f'{self.direction}\n{self.position}'


buggy = Bug(10)
buggy.move()
buggy.turn()
buggy.move()
print(buggy)

