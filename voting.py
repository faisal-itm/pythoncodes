class Voting:
	def __init__(self):
		self.total_votes = 0
		self.__to_repulic = 0
		self.__to_democratic = 0

	def democratic(self):
		self.__to_democratic += 1
		self.total_votes+=1
		print("Vote casted to the Democratic party")

	def republic(self):
		self.total_votes+=1
		self.__to_repulic += 1
		print("Vote casted to the Republic Party")

	def clear(self):
		self.total_votes = 0
		return "Machine cleared"

	def __str__(self):
		return f"total Votes casted: {self.total_votes}\nDemocratic: {self.__to_democratic}\nRepublic: {self.__to_repulic}"


Voting1 = Voting()
Voting1.clear()
print(Voting1)
Voting1.republic()
Voting1.democratic()
Voting1.republic()
Voting1.democratic()
Voting1.republic()
Voting1.democratic()
Voting1.republic()
Voting1.republic()
Voting1.republic()
Voting1.republic()
Voting1.democratic()

print(Voting1)