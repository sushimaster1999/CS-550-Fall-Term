def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else: 
		return fib(n-1)+fib(n-2)
def fac(n):
	if n == 1:
		return 1
	else:
		return n*fac(n-1)

def mystery(n):
	if n < 10:
		return n
	else:
		return mystery(n//10) + n%10

	#if the number has only one digit (less than 10)
		#return sum
	#else:
		#take the number, mod 10, add it to sum, remove the last digit
def clean(x):
	#Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a single char. So "yyzzza" yields "yza".
	s = x
	if len(x) < 2:
		return x
	else:
		if (x[0] == x[1]):
			return clean(x[1:])
		else:
			return x[0]+clean(x[1:])

	#if every character only has one letter
		# return string
		#--> One way to know this is if the string is less than two letters.
	#else: 
		#take away one character that is repeating


n = abs(int(input("Number:")))
print("Factorial:", fac(n))
n = int(input("Number:"))
print("Fibonacci:", fib(n))
n = int(input("Mystery Number:"))
print("OOOOH Spooky mystery:")
print(mystery(n))
x = (input("String Cleaning:"))
print(clean(x))
print(clean('aabbccddd'))
print(clean('Happy'))


