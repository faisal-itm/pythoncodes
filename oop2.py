class Dog:
	species = "Canis familiaris"

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return f"{self.name} is {self.age} old."
	
	def speak(self, sound):
		self.sound = sound

		return f"{self.name} says \"{sound}\" .."


pilo = Dog("pillo", 12)		

print(pilo.speak("BOOOOOOO"))