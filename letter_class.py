class Letter:
	def __init__(self, letterfrom:str, letterto:str):
		self._sender = letterfrom
		self._recepient = letterto
		self._body = ""

	def addline(self,line:str):
		self._body = self._body+"\n"+line

	def gettext(self):
		print( f"Dear {self._recepient}:\n{self._body}\n\nSincerely,\n\n{self._sender}" )


letter1 = Letter("Mary","John")
letter1.addline("Hope you are doing good.")	
letter1.addline("Wish you all the best for your exam")	
letter1.addline("See you soon.")
letter1.gettext()