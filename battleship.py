#Import necessary libraries
import time
import unicornhathd
from sys import exit

cursor = [2, 2]

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
	unicornhathd.rotation(0)
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
			cursor[0], cursor[1], place = cursorMovement(input(""), cursor)
			for i in range(ships[ship]):
				unicornhathd.set_pixel(x, y+i, 255, 0, 0)
				unicornhathd.show()
			if place:
				layout["row1"] = 0
				
#Checking for any input
def cursorMovement(input, cursor):
	x = cursor[0]
	y = cursor[1]
	action = False
	if input == "2" and y > 2:
		y -= 1
	elif input == "8" and y < 13:
		y += 1
	elif input == "4" and x > 2:
		x -= 1
	elif input == "6" and x < 13:
		x += 1
	elif input == "7":
		action = True
	unicornhathd.rotation(0)
	print(x)
	unicornhathd.set_pixel(x, y, 10, 32, 240)
	unicornhathd.show()
	return x, y, action




for row in player1Layout:
		for i in player1Layout[row]:
			print(i, end="")
try:
	gameSetup()
	player1Setup(startingShips)
except EOFError:
	pass

