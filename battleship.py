#Import necessary libraries
import time
import unicornhathd
from sys import exit

#Starting cursor position
cursor = [7, 7]

rotation = 0

#Dictionary of ships with lengths
startingShips = {
	"carrier": 5,
	"horizontalBattleship": 4,
	"verticalBattleship": 4,
	"horizontalCruiser": 3,
	"verticalCruiser": 3,
	"horizontalSub": 3,
	"verticalSub": 3,
	"horizontalDestroyer": 2,
	"verticalDestroyer": 2
}

#Player's grids, both their setup and view of opponent's board
player1Layout = {
	"row1": ['.' for i in range(12)],
	"row2": ['.' for i in range(12)],
	"row3": ['.' for i in range(12)],
	"row4": ['.' for i in range(12)],
	"row5": ['.' for i in range(12)],
	"row6": ['.' for i in range(12)],
	"row7": ['.' for i in range(12)],
	"row8": ['.' for i in range(12)],
	"row9": ['.' for i in range(12)],
	"row10": ['.' for i in range(12)],
	"row11": ['.' for i in range(12)],
	"row12": ['.' for i in range(12)]
}
player1View = {
	"row1": ['?' for i in range(12)],
	"row2": ['?' for i in range(12)],
	"row3": ['?' for i in range(12)],
	"row4": ['?' for i in range(12)],
	"row5": ['?' for i in range(12)],
	"row6": ['?' for i in range(12)],
	"row7": ['?' for i in range(12)],
	"row8": ['?' for i in range(12)],
	"row9": ['?' for i in range(12)],
	"row10": ['?' for i in range(12)],
	"row11": ['?' for i in range(12)],
	"row12": ['?' for i in range(12)]
}
player2Layout = {
	"row1": ['.' for i in range(12)],
	"row2": ['.' for i in range(12)],
	"row3": ['.' for i in range(12)],
	"row4": ['.' for i in range(12)],
	"row5": ['.' for i in range(12)],
	"row6": ['.' for i in range(12)],
	"row7": ['.' for i in range(12)],
	"row8": ['.' for i in range(12)],
	"row9": ['.' for i in range(12)],
	"row10": ['.' for i in range(12)],
	"row11": ['.' for i in range(12)],
	"row12": ['.' for i in range(12)]
}
player2View = {
	"row1": ['?' for i in range(12)],
	"row2": ['?' for i in range(12)],
	"row3": ['?' for i in range(12)],
	"row4": ['?' for i in range(12)],
	"row5": ['?' for i in range(12)],
	"row6": ['?' for i in range(12)],
	"row7": ['?' for i in range(12)],
	"row8": ['?' for i in range(12)],
	"row9": ['?' for i in range(12)],
	"row10": ['?' for i in range(12)],
	"row11": ['?' for i in range(12)],
	"row12": ['?' for i in range(12)]
}

#Sets up the border of the gameboard
def gameSetup():
	unicornhathd.rotation(0) #Set starting rotation
	
	#For loops that place the border lights of the board
	for x in range(14): 
		unicornhathd.set_pixel(x + 1, 14, 255, 255, 255)
		unicornhathd.show()
		unicornhathd.set_pixel(x + 1, 1, 255, 255, 255)
		unicornhathd.show()
	for y in range(12):
		unicornhathd.set_pixel(1, y + 2, 255, 255, 255)
		unicornhathd.show()
		unicornhathd.set_pixel(14, y + 2, 255, 255, 255)
		unicornhathd.show()


#Setup for a player's ships
def playerSetup(ships, layout):
	for ship in ships:
		while True:
			x = cursor[0]
			y = cursor[1]
			cursor[0], cursor[1], place, rotate = cursorMovement(input(""), cursor)
			try:
				for i in range(ships[ship]):
					if cursor[1]+i > 13:
						pass
					unicornhathd.set_pixel(cursor[0], cursor[1]+i, 255, 0, 0)
					unicornhathd.show()
				if place:
					layout["row1"] = 0
			except IndexError:
				unicornhathd.clear()
				
#Checking for any input
def cursorMovement(input, cursor):
	#X and Y are position of cursor, Place and Rotate are the two other possible actions
	x = cursor[0]
	y = cursor[1]
	place = False
	rotate = False
	
	#Each movement of cursor checks to make sure cursor doessn't leave board area
	if input == "2" and y > 2:
		y -= 1
	elif input == "8" and y < 13:
		y += 1
	elif input == "4" and x > 2:
		x -= 1
	elif input == "6" and x < 13:
		x += 1
	elif input == "7":
		place = True
	elif input == "9":
		rotate = True
	unicornhathd.rotation(0)
	print(x)
	unicornhathd.set_pixel(x, y, 10, 32, 240)
	unicornhathd.show()
	return x, y, place, rotate



try:
	gameSetup()
	playerSetup(startingShips, player1Layout)
except EOFError:
	unicornhathd.clear()

