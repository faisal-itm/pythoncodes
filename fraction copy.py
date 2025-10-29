class Fraction:
	def __init__(self, numerator=0, denumerator=1):
		if (not isinstance(numerator, int) or 
			not isinstance(denumerator, int)):
			raise TypeError("The numerator & denumerator must be integers")

		if denumerator == 0:
			raise ZeroDivisionError("Zero denumerator")
		if numerator == 0:
			self._denumerator = 1 
			self._numerator = 0
		else:
			if(numerator < 0 and denumerator >= 0 or 
				numerator >=0 and denumerator < 0):
				sign = -1
			else:
				sign = 1
			
			# Euclid Algorithm 

			a = abs(numerator)
			b = abs(denumerator)	
			while a % b != 0:
				tempA = a
				tempB = b 
				a = tempB
				b = tempA % tempB
			self._numerator = abs(numerator) // b * sign
			self._denumerator = abs(denumerator)//b
	def __repr__(self):
		return (f'{self._numerator}/{self._denumerator}')


	def __eq__(self, rhsValue):
		return (self._numerator == rhsValue._numerator and
			    self._denumerator == rhsValue._denumerator)

	def __add__(self, rhsValue):
		if isinstance(rhsValue,int):
			rhsFrac = Fraction(rhsValue, 1)
		elif isinstance(rhsValue, Fraction):
			rhsFrac = rhsValue
		else:
			raise TypeError("augment must be int or fraction")

		num = (self._numerator *  rhsFrac._denumerator +
			self._denumerator*rhsFrac._numerator)
		den = self._denumerator*rhsFrac._denumerator
		return Fraction(num, den)	



frac1 = Fraction(1,3)
print(frac1._numerator)