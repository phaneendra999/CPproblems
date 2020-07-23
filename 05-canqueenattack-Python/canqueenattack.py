# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.

def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	rows = 8
	columns = 8
	board = [[False for x in range(columns)] for y in range(rows)]
	for i in range(rows):
		for j in range(columns):
			if(i == oR):
				board[i][j] = True
			elif(j == oC):
				board[i][j] = True
			elif(abs(i-j) == abs(oR- oC) or abs(i+j) == abs(oR+oC)):
				board[i][j] = True
	if(board[qR][qC] == True):
		return True
	return False