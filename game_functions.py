from IPython.display import clear_output
import random


# clear output w/ cross-IDLE compatibility
def clear_output_new():
    '''     
    # here, we "try" clear_output, but clear_output is specific to Jupyter IDLE.
    # avoids error in other environment by applying print-line method to clear board. 
    '''
    try:
        clear_output()
    except NameError or ModuleNotFoundError:
        print('\n'*25)


# PRINT GAME BOARD
def display_board(board):
    #row1 = board[1:4]
    #row2 = board[4:7]
    #row3 = board[7:10]
    print(f"\n\t|| {board[1]} | {board[2]} | {board[3]} ||")
    print("\t||-----------||")
    print(f"\t|| {board[4]} | {board[5]} | {board[6]} ||")
    print("\t||-----------||")
    print(f"\t|| {board[7]} | {board[8]} | {board[9]} ||\n")
    

def display_score(player1,player2):
    print(f"\t SCORE: \n\t - {player1['name']}: {player1['score']}\n\t - {player2['name']}: {player2['score']}\n")


# PLAYER SETUP 
def intro_players():
    '''
    I chose to allow any marker symbol; Official solution restricted to X or O.
    This could be made as such using default state and while loop,
    e.g., 
    > marker1 = '?' 
    > while not (marker1 == 'X' or marker1 == 'O')
    >     marker1 = input(...)   etc.
    '''
    name1 = input("To Player A: please enter your name")
    name2 = input("To Player B: please enter your name")
    
    marker1 = input(f"To {name1}: What is your marker symbol?")
    marker2 = input(f"To {name2}: What is your marker symbol?")
    # _______________
    return name1,name2,marker1,marker2

# CHOOSE WHICH PLAYER GOES FIRST
def choose_first(player1,player2):
    
    return random.choice([player1,player2])


# PLAYER CHOOSES THEIR MOVE
def player_input(player,pos_vacancy):
    # ----- defaults ------
    choice = 'wrong'       # loop criteria 1
    confirmation = False   # loop criteria 2
    
    while choice.isdigit() == False or confirmation == False:      
        # user input 
        choice = input(f"\n\t{player['name']}, please enter a number (1-9). \n\t The positions currently available are: {pos_vacancy}.  \n\t Alternatively, enter 'q' to quit the game.")
        
        # if not integer, retry 
        if choice == 'q':
            return 'quit'
        
        elif choice.isdigit() == False:
            print(f"Requires integer, {choice} is not an integer.")
            
        # if integer, give chance to change answer.
        
        elif choice.isdigit() == True:
            #confirm = input(f"You've selected {choice}.\n\t Confirm? (y or n)")
            confirm = 'y'  #temporary, to avoid confirmation screen
            if confirm == 'n':
                print("Enter another number (1-9)")      
            else:
                print(f"\n\tYou have selected: {choice}.")
                confirmation = True    # CRITERIA #2 TO ESCAPE LOOP  
    # _______________
    return int(choice)


# CHECK IF A POSITION IS OPEN FOR USE 
def space_check(board, position):
    # alternative to below, could check if 'position' in list pos_vacancy.. e.g., "return position in pos_vacancy"
    # i.e., we can check if its' value is currently "_"... OR, we could check the list 'pos_vacancy' for that index position #
    
    #if board[position] == '__':
    if board[position] == ' ':
        return True
    else:
        return False
    

# VERIFY PLAYER MOVE CAN BE CURRENTLY PLAYED 
def player_choice(board,player,pos_vacancy):
    '''
    ----explanation----
    this function calls the player_input function, which takes/verifies the input as integer 1-9. 
    once a valid integer is returned, this function verifies that the position is currently available for use. 
    
    '''
    position = 'wrong'    # Criteria #1 to maintain While-Loop: 
    
    while position == 'wrong' or vacancy == False:    
        position = player_input(player,pos_vacancy)
        
        if position != 'wrong':    # Crtieria #1 to escape loop:
            
            # if they chose to quit...  
            if position == 'quit':
                return 'quit'
            
            # if they picked a move...
            else:
                vacancy = space_check(board,position)   # ---> boolean output  
                if vacancy == False:
                    print("\tPosition occupied. Choose again.")
 
                else:   
                    print("\tPosition accepted. Placing marker.")
                    vacancy = True
    # _______________  
    return position


# PERFORM PLAYER MOVE ONTO THE GAME BOARD
def place_marker(board, marker, position):     
    board[position] = marker
    # _______________
    return board


# CHECK IS GAME BOARD IS FULL
def full_board_check(board):
    # _______________
    return len(pos_occupancy) == 9


# CHECK IF A PLAYER HAS WON THE GAME
def win_check(board, mark):
    '''
    # -----explanation----
    # note: the player is specified by their marker, not their name
    # (1) we index all board positions occupied by the given marker                             = 'playerpositions'
    # (2) we provide a list of all 3-position combos which would be considered a win            = 'winningcombos'
    # (3) then, we iterate 'winningcombos', checking each whether their 3 positions are in 'playerpositions' 
    # ---- ----------------
    '''
    playerpositions = [j for j, x in enumerate(board) if x == mark]
    
    winningcombos = [[1,2,3],[1,4,7],[1,5,9],[4,5,6],[2,5,8],[3,5,7],[7,8,9],[3,6,9]]
    
    i=0    # index iterator 
    winstatus = False
    wincount = 0   # this will be useful if we want extra points for multiple winning combinations
    
    for i in range(0,len(winningcombos)):
        j = winningcombos[i]
        
        k = all(x in playerpositions for x in j)   
        #'k'=True if a winning combo comprises 3 player positions 
        # 'k' is analogous to:  >>> "[True for x in combos if x in winningcombos][0]"
        # ...except that method requires generating every distinct combination of 3 player positions 
        
        if k == True:  
            #print(f"\t\t Tic-Tac-Toe, Three-in-a-row! \t --- positions {j}")
            wincount += 1
        else:
            pass
        i+=1
        
    if wincount >= 1:
        #print(f"Player {mark} wins! # of winning positions = {wincount}")
        winstatus = True
    else:
        winstatus = False
    # _______________
    return winstatus,wincount


def replay():
    replay = 'unknown' #new
    while replay == 'unknown':
        
        replay = input("\n\tWould you like to play the game again? (y or n)")
        if replay=='y':
            x_temp = True
        else:
            x_temp = False
    return x_temp