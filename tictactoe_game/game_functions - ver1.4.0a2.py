#(BRANCH wrapped game script ver1.4.2a)
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
    # This function prints the current state of the game board.
    print(f"\n\t|| {board[1]} | {board[2]} | {board[3]} ||")
    print("\t||-----------||")
    print(f"\t|| {board[4]} | {board[5]} | {board[6]} ||")
    print("\t||-----------||")
    print(f"\t|| {board[7]} | {board[8]} | {board[9]} ||\n")
    
def display_score(player1,player2):
    # print the current score of each player.
    print(f"\t SCORE: \n\t - {player1['name']}: {player1['score']}\n\t - {player2['name']}: {player2['score']}\n")

def get_position_data(board):
    pos_vacancy = [j for j, x in enumerate(board) if x == ' ']
    pos_occupancy = [j for j, x in enumerate(board) if x in {'X','O'}]
    return pos_vacancy,pos_occupancy

# PLAYER SETUP 
def intro_players():
    '''
    This function asks the player(s) to specify single/two-player game, their names, and desired marker symbol.
    '''
    num_players = 'unknown'
    num_confirm = False

    while num_players.isdigit() == False or num_confirm == False:
        
        num_players = input("Will this be game have 1 player or 2? (Please enter 1 or 2)\t")
        
        if num_players.isdigit() == False:
            print(f"Requires integer, {num_players} is not an integer.")
            continue
            
        # if integer, give chance to change answer.
        elif num_players.isdigit() == True:
            confirm = input(f"You've chosen a {num_players} player game. \n\t Please confirm? (y or n)")
            if confirm == 'n':
                print("Enter another number (1 or 2)")
                continue
            else:
                print(f"\n\tYou have selected: {num_players}.")
                num_confirm = True    # CRITERIA #2 TO ESCAPE LOOP
                break
    
    name1 = input("To Player A: please enter your name")
    markerchoices = ['X','O']
    marker1 = '?'
    while marker1 not in markerchoices:
        marker1 = input(f"To {name1}: What is your marker symbol? (Choose X or O)")
        if marker1 in markerchoices:
            markerchoices.remove(marker1)
            break
        else:
            continue
    if num_players == 2:
        name2 = input("To Player B: please enter your name")
    else:
        name2 = 'computer'
    marker2 = markerchoices[0]
    return name1,name2,marker1,marker2,num_players

# CHOOSE WHICH PLAYER GOES FIRST
def choose_first(player1,player2,num_players):
    '''
    This function uses the random library to select which player takes the first turn.
    In a two-player game, the players have 1:1 odds of taking the first turn.
    In a single-player game, to reduce difficulty, the human player has 2:1 odds in favor of taking first turn.
    '''
    if num_players == 1:
        return random.choice([player1,player1,player2]) 
    else:
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
    

def player_choice(board,player,pos_vacancy,marker,marker1,marker2,num_players):
    '''
    ----explanation----
    in a 1 player game, on the computer's turn, this will call 'computer_choice' function ...
    otherwise, this function calls the player_input function, which takes/verifies the input as integer 1-9. 
    once a valid integer is returned, this function verifies that the position is currently available for use. 
    
    '''
    if player['name'] == 'computer':
        position = computer_choice(board,marker1,marker2)
        vacancy = True
        return position
    else:
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

def computer_choice(board,marker1,marker2):
    '''
    This function is the decision algorithm for the computer player to derive their best move.
    1. Every winning combination is examined for opportunities and threats.
    2. Then a list of defensive and offensive opportunities is created.
    3. Next, offensive and defensive opportunities are cross-examined for mutual overlap.
    4. Last, a scoring system is applied to deduce the most preferable move by the above factors.
    '''
    # STATICS
    winningcombos = [[1,2,3],[1,4,7],[1,5,9],[4,5,6],[2,5,8],[3,5,7],[7,8,9],[3,6,9]]
    player1positions = [j for j, x in enumerate(board) if x == marker1]
    player2positions = [j for j, x in enumerate(board) if x == marker2]
    vacantpositions = [j for j, x in enumerate(board) if x == ' ']

    # LOGIC

    comboindex = []
    for combo in winningcombos:
        sum_p1,sum_p2,sum_open = 0,0,0
        vacancies = []
        for p in player1positions:
            sum_p1 += sum(i==p for i in combo)
        for p in player2positions:
            sum_p2 += sum(i==p for i in combo)
        for p in vacantpositions:
            sum_open += sum(i==p for i in combo)
            if p in combo:
                vacancies.append(p)

        comboindex.append((combo,sum_p1,sum_p2,sum_open,vacancies))
        #print("combo:",combo,"\tsum_p1:",sum_p1,"\tsum_p2:",sum_p2,"\tsum_open:",sum_open,"\tvacancies:",vacancies)

    defense = []
    offense = []
    for (a,b,c,d,e) in comboindex:
        if b == 0 and c == 0:
            for p in e:
                offense.append(p)
        elif b >= 1 and c == 0:
            for p in e:
                defense.append(p)
        elif b == 0 and c >= 1:
            for p in e:
                offense.append(p)   
        else:
            pass
    #print("defense:\t",defense)
    #print("offense:\t",offense)

    options = []
    for p in vacantpositions:
        count_offense = sum(p==i for i in offense)
        count_defense = sum(p==i for i in defense)
        scoring = count_offense + count_defense

        options.append([p,count_offense,count_defense,scoring])

    rankings = []
    for [i,j,k,rank] in options:
        x = 0
        if j >= 1 and k >= 1:
            x += 1
        else:
            pass
        for (a,b,c,d,e) in comboindex:
            if i in e:
                if b==2 and c==0:
                    x += 2
                elif b==0 and c==2:
                    x += 3
                else:
                    pass
            else:
                pass
        newrank = rank + x
        rankings.append((i,newrank))

    rankings.sort(key=lambda x:x[1])
    #print("Rankings list:\t",rankings)
    
    if len(rankings) > 1:
        # choice1 is the computer's best move. choice2 is the second-best.
        # to reduce difficulty, there is only a 2:1 probability that the computer selects the best move.
        choice1 = rankings[-1][0]
        choice2 = rankings[-2][0]
        choice = random.choice([choice1,choice1,choice2])
    else:
        choice1 = rankings[-1][0]
        choice = choice1
    #print("Computer chooses:\t",choice)
    return choice

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

def determine_victor(player1,player2):
    if player1['score'] == player2['score']:
        return ("Draw","The game has ended in a tie!")
    elif player1['score'] > player2['score']:
        return (player1,f"Victory goes to {player1['name']} (symbol '{player1['marker']}')! \t Final score {player1['score']} vs. {player2['score']}.")
    elif player1['score'] < player2['score']:
        return (player2,f"Victory goes to {player2['name']} (symbol '{player2['marker']}')! \t Final score {player2['score']} vs. {player1['score']}.")
    else:
        pass