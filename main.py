# Create a 3x3 board
row_1 = ["⬜","⬜","⬜"]
row_2 = ["⬜","⬜","⬜"]
row_3 = ["⬜","⬜","⬜"]


def check_score():
	return row_1[0] == "x" and row_1[1] == "x" and row_1[2] == "x"
		

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


count = 0 
game_on = True
while game_on:
	count += 1
	user = int(input("Enter your position:"))
	playgame(user)
	if check_score():
		game_on = False
		print("You won")
	elif count == 9:
		print("you ran out of options")
		game_on = False






