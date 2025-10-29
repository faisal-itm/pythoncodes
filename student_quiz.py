class Student:
	

	def __init__(self,name:str):
		self._total_quizes = 0
		self._name = name
		self._score = 0
		self._avg = 0
		self._grade = 0
		self._out_of = 0

	def addQuiz(self,score: int):
		self._total_quizes = self._total_quizes + 1
		self._score = self._score + score 
		self._out_of = self._out_of + 100
		print("--- Quiz Added ---")
		#print(f'quizes = {self._total_quizes}\nScore = {self._score}\nOut of : {self._out_of}')

	def TotalScore(self):
		return self._score

	def getAvgScore(self):
		self._avg = self._score / self._total_quizes
		return self._avg

	def getname(self):
		return self._name

	def grade(self):
		self._grade = (self._score / self._out_of) * 100
		
		return self._grade
		
	def getgrade(self):
		if self._avg > 90:
			self._grade ="A"
		elif self._avg in range(80,90):
			self._grade = "B+"
		elif self._avg in  range(70,80):
			self._grade = "B"
		else:
			self._grade = "C"
		return self._grade


	def __str__(self):
		return f'---------------------\nName: {self._name}\nTotal Quizes: {self._total_quizes}\nScore: {self._score}\nAvg Score: {self._avg}\nGrade: {self._grade}\n----------------------'




student1 = Student("Ahmad Ali")
print(student1)
student1.addQuiz(80)
student1.addQuiz(70)
student1.addQuiz(90)
student1.TotalScore()
student1.getname()
student1.getAvgScore()
student1.getgrade()
print(student1)