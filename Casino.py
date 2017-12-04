#Project Casino
import sys
import math
import os
import time
from random import *
from random import choice as rc


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def total(hand): #This is code from a website for the aces.
    # how many aces in the hand
    aces = hand.count(11)
    # to complicate things a little the ace can be 11 or 1
    # this little while loop figures it out for you
    t = sum(hand)
    # you have gone over 21 but there is an ace
    if t > 21 and aces > 0:
        while aces > 0 and t > 21:
            # this will switch the ace from 11 to 1
            t -= 10
            aces -= 1
    return t
def Blackjack():
	profit = 0 # profit tracker
	cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] #Create the deck of cards
	dwin = 0  # dealer win counter
	pwin = 0  # player win counter 
	while True:
	    player = [] #create an array for the player's hand
	    player.append(rc(cards)) #adds 2 cards to the player's hand
	    player.append(rc(cards))
	    pbust = False
	    dbust = False
	    bet = 0
	    try:
	    	bet = float(input("How much money would you like to bet on this game?"))
	    except TypeError:
	    	print('That is not a valid number.')
	    while True:
	        tp = total(player) #checks players hand for aces
	        print ("You have %s with a total value of %d" % (player, tp))
	        if tp > 21:
	            print ("You busted!")
	            pbust = True
	            break
	        elif tp == 21:
	            print ("BLACKJACK!")
	            break
	        else:
	            choice = input("Hit or Stand?")
	            if choice == 'Hit' or choice == 'hit' or choice == 'h':
	                player.append(rc(cards)) #adds cards to the players hand when they want to hit
	            else:
	                break
	    while True:
	        dealer = [] # Creates an array for dealer's hand
	        dealer.append(rc(cards))
	        dealer.append(rc(cards)) # Add two cards from cards to the dealer's hand
	        while True:
	            td = total(dealer) #checks dealers hand for aces            
	            if td < 18: #Sets the limit to when the dealer will stand
	                dealer.append(rc(cards))
	            else:
	                break
	        print ("the dealer has %s for a total of %d" % (dealer, td))
	        if td > 21:
	            print (" The dealer busted!")
	            dbust = True
	            if pbust == False:
	                print ("You win!")
	                pwin += 1
	                profit = profit+ 2*bet
	        elif td >= tp:
	            print ("The Dealer wins!")
	            dwin += 1
	            profit = profit - bet
	        elif tp > td:
	            if pbust == False:
	                print ("You win!")
	                pwin += 1
	                profit = profit + 2*bet
	            elif dbust == False:
	                print ("The dealer wins!")
	                dwin += 1
	                profit = profit - bet
	            else:
	            	print ("Both players busted. Draw")
	        break
	    print
	    print ("Wins, player = %d  Dealer = %d" % (pwin, dwin))
	    print("Total profit = %d" % (profit))
	    exit = input("Press Enter to continue, or Quit to exit")
	    if exit == 'quit' or exit == 'Exit' or exit == "Quit" or exit == 'exit':
	        break
	    else:
	    	cls()
	print
	print ("Thanks for playing blackjack, please play another one of our games!")
	time.sleep(2)
	return(profit)
def Roulette():
	profit = 0
	ball = 0
	x = False
	ply = True
	while ply == True:
		try:
			bet = float(input("How much money would you like to bet on this game?"))
		except ValueError:
			print('That is not a valid number.')
			break
		Category = (input("Would you like to bet on odds, evens, or a certain number between 00 and 36.")) # make sure the player has choosen a correct choice
		try:
			x =  -1 < int(Category) < 36
		except ValueError:
			print('')
		if Category == 'odds' or Category == "Odds" or Category == "Odd" or Category == "odd":
			print("You have chosen Odds.")
			Category = "Odds"
		elif Category == 'evens' or Category == "Evens" or Category == "even" or Category == "Even":
			print("You have chosen Evens.")
			Category = "Evens"
		elif Category == '00':
			print("You have chosen 00")
			Category = -1
		elif x == True:
			print('you have chosen',Category)
		else:
			print("please select a valid Category. 00 Has been chosen for you.")
			Category = -1
			time.sleep(2)
		ball = randint(-1, 36)	# Check to see if the player has won
		if ball == -1 and Category == -1:
			print("The ball landed on 00, You win!")
			profit = profit + 4 * bet
		elif Category == ball:
			print("The ball landed on",ball,". You win!")
			profit = profit + 3 * bet
		elif ball // 2 == ball /2 and Category == 'Evens':
			print("The ball landed on",ball," That's an even! You win!")
			profit = profit + 1.5 * bet
		elif ball //2 != ball / 2 and Category == 'Odds':
			print("The ball landed on",ball," That's an odd! You win!")
			profit = profit + 1.5 * bet
		else:
			print("The ball landed on ",ball,". You lose.")
			profit = profit - bet
		print("You have currently made $",profit)
		time.sleep(1)
		exit = input("Press Enter to continue, or Quit to exit")
		if exit == 'quit' or exit == 'Exit' or exit == "Quit":
			ply = True
			break
		else:
			cls()
	print
	print ("Thanks for playing roulette, please play another one of our games!")
	return(profit)
'''def Slots():
	profit = 0
	options = [c,b,t,7]
	while True:
		machine = [] 
		machine.append(rc(options))
		machine.append(rc(options))
		machine.append(rc(options))


b in first slot, c in second, 7 in third
                .-------.\n
                |Jackpot|\n
    ____________|_______|____________\n
   |  __    __    ___  _______ __    |\n
   | / _\  / /   /___\/__  __// _\   |\n
   | \ \  / /   //  //  / /   \ \  25|\n
   | _\ \/ /___/ \_//  / /    _\ \ []|\n
   | \__/\____/\___/   \/     \__/ []|\n
   |===_______===_______===_______===|\n
   ||*|\_     |*| _____ |*|\_     |*||\n
   ||*|| \ _  |*||     ||*|| \ _  |*||\n
   ||*| \_(_) |*||*BAR*||*| \_(_) |*||\n
   ||*| (_)   |*||_____||*| (_)   |*|| __\n
   ||*|_______|*|_______|*|_______|*||(__)\n
   |===_______===_______===_______===| ||\n
   ||*| _____ |*|\_     |*|  ___  |*|| ||\n
   ||*||     ||*|| \ _  |*| |_  | |*|| ||\n
   ||*||*BAR*||*| \_(_) |*|  / /  |*|| ||\n
   ||*||_____||*| (_)   |*| /_/   |*|| ||\n
   ||*|_______|*|_______|*|_______|*||_//\n
   |===_______===_______===_______===|_/\n
   ||*|  ___  |*|   |   |*| _____ |*||\n
   ||*| |_  | |*|  / \  |*||     ||*||\n
   ||*|  / /  |*| /_ _\ |*||*BAR*||*||\n
   ||*| /_/   |*|   O   |*||_____||*||\n
   ||*|_______|*|_______|*|_______|*||\n
   |===___________________________===|\n
   |  /___________________________\  |\n
   |   |                         |   |\n
  _|    \_______________________/    |_\n
 (_____________________________________)\n

win with all bells
                .-------.\n
                |Jackpot|\n
    ____________|_______|____________\n
   |  __    __    ___  _______ __    |\n
   | / _\  / /   /___\/__  __// _\   |\n
   | \ \  / /   //  //  / /   \ \  25|\n
   | _\ \/ /___/ \_//  / /    _\ \ []|\n
   | \__/\____/\___/   \/     \__/ []|\n
   |===_______===_______===_______===|\n
   ||*|\_     |*| _____ |*|   |   |*||\n
   ||*|| \ _  |*||     ||*|  / \  |*||\n
   ||*| \_(_) |*||*BAR*||*| /_ _\ |*||\n
   ||*| (_)   |*||_____||*|   O   |*|| __\n
   ||*|_______|*|_______|*|_______|*||(__)\n
   |===_______===_______===_______===| ||\n
   ||*|   |   |*|   |   |*|  ___  |*|| ||\n
   ||*|  / \  |*|  / \  |*| |_  | |*|| ||\n
   ||*| /_ _\ |*| /_ _\ |*|  / /  |*|| ||\n
   ||*|   O   |*|   O   |*| /_/   |*|| ||\n
   ||*|_______|*|_______|*|_______|*||_//\n
   |===_______===_______===_______===|_/\n
   ||*| _____ |*|   |   |*|\_     |*||\n
   ||*||     ||*|  / \  |*|| \ _  |*||\n
   ||*||*BAR*||*| /_ _\ |*| \_(_) |*||\n
   ||*||_____||*|   O   |*| (_)   |*||\n
   ||*|_______|*|_______|*|_______|*||\n
   |===___________________________===|\n
   |  /___________________________\  |\n
   |   |                         |   |\n
  _|    \_______________________/    |_\n
 (_____________________________________)\n





have a list of three numbers between certain values representing different objects.
	print out random objects for one second
	print out a list of objects, 
	if two values are equal, give the player a reward equal to what they payed
	if three values are equal, dtripple the value that the player paid



	profit = 0
	time.sleep(2)
	return (profit)'''
#Intoduction
cls()
Money = 0
print('Welcome to Casino McGlinchey! As a gesture of providence, we will gift you $500 to spend on any of our games.')
time.sleep(3)
Money = Money + 500
print("If you can double the money, you will win $250 to take home!")
time.sleep(2)
input("Currently we have 2 games:")
while (0<=Money<=1000):
	time.sleep(1)
	cls()
	print("You currently have $",Money)
	g = input("Which game would you like to play next? \nBlackjack, or Roulette: ")

	if g == 'Blackjack' or g == 'blackjack' or g == '1':
		Money = Money+Blackjack()
	elif g == 'Roulette' or g == 'roulette' or g == '2':
		Money = Money+Roulette()
	elif g == 'Slots' or g == 'slots' or g == '3':
		Money = Money+Slots()
	else:
		input("We're sorry that there are no other games, please pick one of the above.")
if Money >= 1000:
	print('As you finish your game you are greeteed by Mr. McGlinchey himself.')
	time.sleep(2)
	print('\"Hello friend, you were really lucky today! Congratulations!\"')
	time.sleep(2)
	print('\"Here is your well earned $250\"')

if Money <= 0:
	print('You are thrown out to the Curb by the bouncer')
	print('\"Sorry Bub, we don\'t accept losers here.\"' )
	time.sleep(2)
	print('Bad ending.', end='')
	time.sleep(1)
	print('.', end='')
	time.sleep(1)
	print('.', end='')	
	time.sleep(1)
	print('.', end='')
	time.sleep(1)
	print('.', end='')
# Games
'''
Player's money value starts at 500?
for each game ask player how much money they want to bet
Blackjack
	- Program there to be only four of every card
	good example:
		https://www.daniweb.com/programming/software-development/code/216857/a-python-blackjack-game
roulette
	have the user bet on evens, odds, or a specific number
	denerate random int between -1, ??
	check to see if the number is divisible by two, if yes, its even, else its odd

	about roulette wheels
	https://en.wikipedia.org/wiki/Roulette#Roulette_table_layout
Slot machine
	have a list of three numbers between certain values representing different objects.
	print out random objects for one second
	print out a list of objects, 
	if two values are equal, give the player a reward equal to what they payed
	if three values are equal, tripple the value that the player paid
Profits
in order to 

'''