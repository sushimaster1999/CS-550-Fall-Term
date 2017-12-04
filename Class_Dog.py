#Classes! 
import random
import os

def cls():
	os.system('cls' if os.name=='nt' else 'clear')
class Fly:
	def __init__(self, name, color):
		self.color = color
		self.name = name
		self.age = 0
		self.size = random.randint(1,10)
		self.hunger = 50
		self.energy = 50
		self.alive = True
	def eat(self, amount):
		self.age = self.age + 1
		if self.hunger > 0:
			self.hunger -=(amount)
			self.energy += amount*2
			print("nom nom nom")
		else:
			print(self.name + " is not hungry")
	def stats(self):
		print("Name: " +self.name)
		print("Energy: "+str(self.energy))
		print("Hunger: "+str(self.hunger))
		print("Age: "+str(self.age))
		print("Size: "+self.size)
		print("Color: "+self.color)
	def death(self):
		if self.age > 7:
			self.alive = False
			return self.alive
		else:
			self.alive = True
			return self.alive
	def fly(self):
		self.age += 1
		print(self.name+" flies around and discover a rotten banana in a trash can")
		self.energy -= 10
		self.hunger += 15
	def sleep(self):
		self.age += 1
		print("Your fly sleeps for 2 minutes. It is now well rested")
		self.energy += 30
		self.hunger -= 10
	def annoy(self, nombre):
		self.age += 1
		print("Your fly flies around "+nombre+"\'s head, annoying them")
		self.energy -= 30
		self.hunger -= 25

#
cls()
nam = input("What your Fly's name? ")
col = input("What is the color of your Fly? ")
myFly = Fly(nam, col)
cls()
while myFly.death():
	next = input("What would you like to have your fly do: \n fly, eat, sleep, annoy someone, or Check your stats? ")
	if next == "Fly" or next == "fly" or next == "Fly":
		myFly.fly()
	elif next ==  "eat" or next == "Eat":
		e = int(input("How much do you want your fly to eat?"))
		myFly.eat(e)
	elif next == "sleep" or next == "Sleep":
		myFly.sleep()
	elif next == "annoy" or next == "Annoy" or next == "Annoy somone" or next == "annoy someone":
		n = input("who would you like to annoy?")
		myFly.annoy(n)
	elif next == "stats" or next == "check stats" or next == "Check Stats" or next == "Stats":
		myFly.stats()
	else:
		print("Please choose a valid option")
print("Your Fly died. \n What did you expect?")