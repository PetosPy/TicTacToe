# Create a 3x3 board
row_1 = ["⬜","⬜","⬜"]
row_2 = ["⬜","⬜","⬜"]
row_3 = ["⬜","⬜","⬜"]

def board():
	board = f"{row_1},\n{row_2},\n{row_3}"
	print(board)



def playgame(user):
	if user == 1:
		row_3[0] = "x"
	elif user == 2:
		row_3[1] = "x"
	elif user == 3:
		row_3[2] = "x"
	if user == 4:
		row_2[0] = "x"
	elif user == 5:
		row_2[1] = "x"
	elif user == 6:
		row_2[2] = "x"
	if user == 7:
		row_1[0] = "x"
	elif user == 8:
		row_1[1] = "x"
	elif user == 9:
		row_1[2] = "x"

	else:
		print("wrong play")
		
	board()

playgame(0)

# Way to print that board
# Create 2 players
# Select random player to go first (coin toss)
#

