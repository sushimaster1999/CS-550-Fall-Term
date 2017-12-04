import time
import os
'''minesweeper game
take existing code, fill it with boxxes that remember the values.
take an input fron the user in an x / y coordinate
acces that number in the array, set it to its original value
reprint out the board with updated number
if it is zero, reveal every tile of around it, look for other 0's around it, and tell those zeros to look for more zeros.
add the tiles to a list of coordinates
reprint out the board with the zeros
if it is a mine, create a custom animation using time.sleep  
'''
def cls():
	os.system('cls' if os.name=='nt' else 'clear')
def explode():
	cls()
	print("       .")
	time.sleep(.1)
	cls()
	print("       o")
	time.sleep(.1)
	cls()
	print("       O")
	time.sleep(.1)
	cls()
	print("       ()")
	time.sleep(.1)
	cls()
	print("      ( )")
	time.sleep(.1)
	cls()
	print("      { }")
	time.sleep(.1)
	cls()
	print("     { . }")
	time.sleep(.1)
	cls()
	print("    {  o  }")
	time.sleep(.1)
	cls()
	print("   {   O   }")
	time.sleep(.1)
	cls()
	print("  {   ()   }")
	time.sleep(.1)
	cls()
	print(" {   (  )   }")
	time.sleep(.1)
	cls()
	print(" =   {  }   =")
	time.sleep(.1)
	cls()
	print("--=  {   }  =--")
	time.sleep(.1)
	cls()
	print("-    =    =    -")
	time.sleep(.1)
	cls()
	print("    --    --     ")
explode()