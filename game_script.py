#from IPython.display import clear_output
#from random import randint
from game_functions import clear_output_new,display_board,display_score,intro_players,choose_first,player_input,space_check,player_choice,place_marker,full_board_check,win_check,replay

print('Welcome to Tic Tac Toe!')

# ____ Load the defaults _____
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']    # Empty Board
game_on = True
match_on = True
pos_occupancy = []
pos_vacancy = [1,2,3,4,5,6,7,8,9]
winstatus = False
replayQ = None

# _______ Player Setup  __________ 

# ------ player introduction 
name1,name2,marker1,marker2 = intro_players()

player1 = {'name':name1,'marker':marker1,'score':0}

player2 = {'name':name2,'marker':marker2,'score':0}

#           finally, at the end of game, check player1['score'] vs. player2['score'] for overall winner (cumulative score). 


# ------ randomly pick first player  
player = choose_first(player1,player2)    # ---- "choose_first" /  designates player1 or player2 as "player"
marker = player['marker']                 # ---- assign current player's marker (re-assigned each turn)

clear_output_new()  
display_board(board)                            # Display Board
display_score(player1,player2)


# ------ Anounce first player ------
print(f"\n\tThe player chosen to move first is {player['name']} (symbol '{marker}') \n")


# __________ Game continuity __________ indent Level 0 (IL0)
while game_on == True:   
   
    print("diagnostic message IL1-checkpoint 0") # ************* DIAGNOSTIC *************
    # __________ Match continuity  __________   indent Level 1 (IL1)
    
    
    if match_on == True and len(pos_vacancy) > 0:          # loop until a win, or until board full 
        
        print("diagnostic message IL2-IE00A-start") # ************* DIAGNOSTIC *************
        
        # _______ Each Turn  _________________   indent level 2 (IL2)
        
        print("diagnostic message IL2-IE00A-F01") # ************* DIAGNOSTIC *************
        
        #print(f"the positions currently available are: {pos_vacancy}")
        
        position = player_choice(board,player,pos_vacancy)               # given board, takes choice for input position
        
        
        # ---------- option to quit early ---  IL2, If-Else check 01  (IL2-IE01)
        if position == 'quit':                              
            match_on = False
            game_on = False
            print("diagnostic message IL2-IE00A-IE01-A") # ************* DIAGNOSTIC *************
            break
        else:
            print("diagnostic message IL2-IE00A-IE01-B") # ************* DIAGNOSTIC *************
            pass
        
        
        # ---------- position specified, proceed
        #clear_output()
        #clear_output_new()
        
        print("diagnostic message IL2-IE00A-F02a") # ************* DIAGNOSTIC *************
        place_marker(board, marker, position)               # adds the marker to the board
        
        print("diagnostic message IL2-IE00A-F02b") # ************* DIAGNOSTIC *************
        #display_board(board)
        
        # ---- check if player has won 
        #print("diagnostic message IL2-IE00A-F03") # ************* DIAGNOSTIC *************
        winstatus,wincount = win_check(board,marker)         # check if player won
        
        # ---- end match if player won    ---- IL2, if-else check 02  (IL2-IE02)
        if winstatus == True:
            
            game_on = True
            match_on = False
            print("diagnostic message IL2-IE00A-IE02-A") # ************* DIAGNOSTIC *************
        else:
            #print("diagnostic message IL2-IE00A-IE02-B") # ************* DIAGNOSTIC *************
            pass
                
        # ---- update list of open / occupied positions
        #print("diagnostic message IL2-IE00A-F04a") # ************* DIAGNOSTIC *************
        pos_vacancy.remove(position)
        
        #print("diagnostic message IL2-IE00A-F04b") # ************* DIAGNOSTIC *************
        pos_occupancy.append(position)               
        
        # --- end match if board is full   --- IL2, if-else check 03 (IL2-IE03)
        if len(pos_vacancy) == 0:
            game_on = True
            match_on = False
            print("diagnostic message IL2-IE00A-IE03-A") # ************* DIAGNOSTIC *************
            #break
        else:
            #print("diagnostic message IL2-IE00A-IE03-B") # ************* DIAGNOSTIC *************
            pass
        
        print("diagnostic message IL2-F05a") # ************* DIAGNOSTIC *************
        clear_output_new()
        
        print("diagnostic message IL2-IE00A-F05b") # ************* DIAGNOSTIC *************
        display_board(board)                          # prints the board for next players turn
        display_score(player1,player2)
        
        
        # _______ Switch Turns _______    --- IL2, if-else check 04 (IL2-IE04)
     
        if match_on == True and marker == marker1: 
            print(f"\tend of turn for {name1} (marker {marker1})")
            marker = marker2
            player = player2
            print(f"\tnext turn is for {name2} (marker {marker2})\n")
            print("diagnostic message IL2-IE00A-IE04-A") # ************* DIAGNOSTIC *************
            
        elif match_on == True and marker == marker2: 
            print(f"\tend of turn for {name2} (marker {marker2})")
            marker = marker1
            player = player1
            print(f"\tnext turn is for {name1} (marker {marker1})\n")
            print("diagnostic message IL2-IE00A-IE04-B") # ************* DIAGNOSTIC *************
            
        else:
            # when match_on = False we come here
            print("diagnostic message IL2-IE00A-IE04-C") # ************* DIAGNOSTIC *************
            pass
        
        print("diagnostic message IL2-IE00A-end") # ************* DIAGNOSTIC *************
    
    # __________ End of Match   __________     inside:    IL2-IE00B code block  
    elif match_on == False and game_on == True:
        
        print("diagnostic message IL2-IE00B-start") # ************* DIAGNOSTIC *************
        
        clear_output_new()
        
        # ---- Announce Winner ----  IL2-IE00B, if-else check 01
        if winstatus == True:
            player['score'] += wincount
            display_board(board)
            display_score(player1,player2)
            print(f"Player {player['name']} is the winner! \n\t Number of winning positions = {wincount}")
            
            print("diagnostic message IL2-IE00B-IE01A") # ************* DIAGNOSTIC *************
            pass
        else:
            display_board(board)
            display_score(player1,player2)
            print("no winner")
            print("diagnostic message IL2-IE00B-IE01B") # ************* DIAGNOSTIC *************
        
        # ---- Ask Player if Replay ---- IL2, IE00B, function 01
        
        print("diagnostic message IL2-IE00B-F01") # ************* DIAGNOSTIC *************
        replayQ = replay()
        
        # --- no replay ----
        
        if replayQ == False:        
            print("\nExiting Game...")
            game_on = False
            print("diagnostic message IL2-IE00B-IE02A") # ************* DIAGNOSTIC *************
            break
        
        # ---- yes replay ----
        elif replayQ == True:         
            # ---- reset all defaults ----
            game_on = True
            match_on = True
            board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']    # Empty Board
            pos_occupancy = []
            pos_vacancy = [1,2,3,4,5,6,7,8,9]
            winstatus = False
            replayQ = None
            clear_output_new()
            print("New Game Initiated")
            display_board(board)
            display_score(player1,player2)
            print("diagnostic message IL2-IE00B-IE02B") # ************* DIAGNOSTIC *************
            pass
        else:
            print("nothing")
        
        print("diagnostic message IL2-IE00B-end") # ************* DIAGNOSTIC *************
    
    # Unnecessary code - below
    elif game_on == False:    
        print('This code is not expected to appear. Please refer to the below diagnostic message.')
        print("diagnostic message IL2-IE00C") # ************* DIAGNOSTIC *************
        break
        
    print("diagnostic message IL1-checkpoint 2x") # ************* DIAGNOSTIC *************
    # returns to checkpoint 0 after checkpoint 2

# __________ End Match & End Game   __________   IL0-IE00
if game_on == False:
    print("\n\n\tThank you for playing Tic-Tac-Toe!")
    
    if player1['score'] == player2['score']:
        print("The game has ended in a tie!")
    elif player1['score'] > player2['score']:
        print(f"Victory goes to {player1['name']} (symbol '{player1['marker']}')! \t Final score {player1['score']} vs. {player2['score']}.")
    elif player1['score'] < player2['score']:
        print(f"Victory goes to {player2['name']} (symbol '{player2['marker']}')! \t Final score {player2['score']} vs. {player1['score']}.")
    else:
        pass
    
    print(f"\n Goodbye.")
    #print("quit, gameon false")
    
elif winstatus == False and game_on == False:   # this won't occur because the previous condition matches first anyways
    # test
    print("no win, end of match, gameon false")