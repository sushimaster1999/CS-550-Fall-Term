import os
def cls():
	os.system('cls' if os.name=='nt' else 'clear')
class RationalNumber:
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator
		if denominator == 0:
			print:("Error div by zero")
			sys.exit()
	def __mul__(self, other):
		numerator = self.numerator*other.numerator
		denominator = self.denominator*other.denominator
		return RationalNumber(numerator, denominator)
	def __add__(self, other):
		numerator = (self.numerator*(other.denominator)) + (other.numerator*(self.denominator))
		denominator = self.denominator*other.denominator
		return RationalNumber(numerator, denominator)
	def __sub__(self, other):
		numerator = (self.numerator*(other.denominator)) - (other.numerator*(self.denominator))
		denominator = self.denominator*other.denominator
		return RationalNumber(numerator, denominator)
	def __div__(self, other):
		numerator = self.numerator*other.denominator
		denominator = self.denominator*other.numerator
		return RationalNumber(numerator, denominator)
	def __str__(self):
		numerator = self.numerator
		denominator = self.denominator
		return (str(numerator)+"/"+str(denominator))

n1 = RationalNumber(1,2)
n2 = RationalNumber(1,3)
print(n1)
print(n2)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1.__div__(n2)) #WHY U NO WORK!??!?!?!??!?!?!?!??!?!


