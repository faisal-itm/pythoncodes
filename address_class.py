class Address:

	def __init__(self, house,street,city,state,postal_code,appartment=0):
		self._house = house
		self._street = street
		self._city = city
		self._state = state
		self._postal_code = postal_code
		if appartment != 0:
			self._appartment = appartment

	def __str__(self):
		if self._appartment!=0:
			return f'{self._appartment}\n{self._house}, {self._street}\n{self._city}, {self._state}\n{self._postal_code}'	
		else:	
			return f'{self._house}, {self._street}\n{self._city}, {self._state}\n{self._postal_code}'	

	def comebefore(self, other):
		if other._postal_code < self._postal_code:
			print(f'{other._postal_code} comes before {self._postal_code}')
		else:
			print(f'{self._postal_code} comes before {other._postal_code}')	



addr1 = Address(180,56,"G9","islamabad",29,21)
addr2 = Address(120,33,"G9", "islamabad",20,21)

addr1.comebefore(addr2)
print(addr2,"\n____\n",addr1)