import os   #for making folders and links
os.mkdir("Invalid_Move") #folder for invalid moves

for x in range(0,(19684)):   #should be 3^9 possibilities 3, possibilities for 9 squares
    os.mkdir(str(x))         #Make directories for gamestate so they can be moved into and linked to


for gamestate in range(19684): #create gamestate's
    board = []                #gamestate as a list
    os.chdir(str(gamestate))  #Get ready to make gamestate
    print(os.getcwd())        #tells debugger where they are
    for square in range(0,9):
        board.append((gamestate/(3**square))%3)  #gamestate is in ternary
    numo = 0 #num of O's
    numx = 0  #num of X's
    numun = 0  #num of un-used squares

    for x in board: #count to figure out who's turn it is
        if x == 2:
            numo += 1
        elif x == 1:
            numx += 1
        else:
            numun += 1
            #1 = player1
            #2 = player2
            #3 = Invalid State
            #4 = no moves left
	    #5 = winnerx
	    #6 = winnero
    print("numx: " + str(numx))   #debugger count
    print("numo: " + str(numo)) 
    print("numun: " + str(numun))
    print(board)

    if numx == numo:  
        PlayersTurn = 1
    elif (numun == 9):
        PlayersTurn = 4
    elif numx  == (numo + 1):  
        PlayersTurn = 2
	print("o's turn")
    else:
        PlayersTurn = 3
    
    #Screw it, I'll do 7 checks by hand
    if (board[0] == board[1] == board[2] != 0):
	if (numx == numo):
	    PlayersTurn=6
	else:
	    PlayersTurn=5
    elif (board[3] == board[4] == board[5] != 0):
	if (numx == numo):
	    PlayersTurn=6
	else:
	    PlayersTurn=5
    elif (board[6] == board[7] == board[8] != 0):
	if (numx == numo):
	    PlayersTurn=6
	else:
	    PlayersTurn=5
    elif (board[0] == board[3] == board[6] != 0):
	if (numx == numo):
	    PlayersTurn=6
	else:
	    PlayersTurn=5
    elif (board[1] == board[4] == board[7] != 0):
	if (numx == numo):
	    PlayersTurn=6
	else:
	    PlayersTurn=5
    elif (board[3] == board[5] == board[8] != 0):
	if (numx == numo):
	    PlayersTurn=6
	else:
	    PlayersTurn=5
    elif (board[0] == board[4] == board[8] != 0):
	if (numx == numo):
	    PlayersTurn=6
	else:
	    PlayersTurn=5
    elif (board[2] == board[4] == board[6] != 0):
	if (numx == numo):
	    PlayersTurn=6
	else:
	    PlayersTurn=5
    
    if PlayersTurn < 3:
	    for makelinks in range(0,9):  #make the board
		filename = ""
		if board[makelinks] == 0:
		    
		    filename = str(makelinks) + "--"
		    linknum = 0
		    
		    for x in range(0,9):
		        if x == makelinks:
		            linknum += PlayersTurn * 3**x
		        else:
		            linknum += board[x] * 3**x
		    os.symlink("../" + str(linknum), filename)
		    
		elif board[makelinks] == 1:
		    filename = str(makelinks) + "X"
		    os.symlink("../Invalid_Move", filename)
		else:
		    filename = str(makelinks) + "O"
		    os.symlink("../Invalid_Move", filename)
    else:
	if (PlayersTurn == 3):
	    open("cheater", 'w').close()
	    os.symlink("../0", "Play Again?")
	elif (PlayersTurn == 4):
	    open("cats game", 'w').close()
	    os.symlink("../0", "Play Again?")
	elif (PlayersTurn == 5):
	    open("X wins!!", 'w').close()
	    os.symlink("../0", "Play Again?")
	elif (PlayersTurn == 6):
	    open("O wins!!", 'w').close()
	    os.symlink("../0", "Play Again?")
        print("end of game")
    os.chdir("..")
            
        
    
                
        
