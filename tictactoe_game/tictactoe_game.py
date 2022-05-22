'''
def decorator_for_launch(x):
    def wrapped_func(**kwargs):
        if mode == 'default':
            print("default game mode. commencing default intro function.")
            name1,name2,marker1,marker2,num_players = x()
            return name1,name2,marker1,marker2,num_players
            
        elif mode == 'diag':
            print("diagnostic mode. Game now single-player, generic player names config.") 
            name1 = 'player1'
            name2 = 'computer'
            marker1 = 'X'
            marker2 = 'O'
            num_players = 1
            return name1,name2,marker1,marker2,num_players
        else:
            print("else; passing...")
            pass
    return wrapped_func
'''
#(BRANCH wrapped game script ver1.4.1a)
#@decorator_for_launch
def launch_game(mode='default',**testconfig):
    from game_functions import clear_output_new,display_board,display_score,intro_players
    from game_functions import choose_first,player_input,space_check,player_choice,place_marker
    from game_functions import full_board_check,win_check,replay,determine_victor
    from game_functions import computer_choice,get_position_data,load_defaults
    from game_functions import decorator_for_intros,decorator_for_load,recheck_player

    print('Welcome to Tic Tac Toe!')

    ''' # No longer loading defaults here, we want this AFTER intro_players
    # ____ Load the defaults _____
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']    # Empty Board
    game_on = True
    match_on = True
    pos_occupancy = []
    pos_vacancy = [1,2,3,4,5,6,7,8,9]
    winstatus = False
    replayQ = None
    '''

    # _______ Player Setup  __________ 
    # ------ player introduction 
    name1,name2,marker1,marker2,num_players = intro_players(mode)
    ''' 
    # intro_players is a decorated function, only prompts if mode left to default, mode='default'
    # if game is launched with mode='diag', the decorator auto-responds and intro_players gives no prompt
    '''
    player1 = {'name':name1,'marker':marker1,'score':0}
    player2 = {'name':name2,'marker':marker2,'score':0}

    # ------ randomly pick first player  
    player = choose_first(player1,player2,num_players,mode)    # ---- "choose_first" /  designates player1 or player2 as "player"

    # NEW! load the defaults here, after intro_players and choose_first
    board,game_on,match_on,pos_occupancy,pos_vacancy,winstatus,replayQ = load_defaults(mode,**testconfig)
    ''' 
    # load_defaults is a decorated function, takes standard defaults at first... 
    # ...but overwrites board & pos_occupancy if they are provided in the testconfig
    '''
    # NEW! if test config starts this mid-game, we want to adjust the current turn correctly 
    player,winstatus,match_on = recheck_player(mode,player,player1,player2,board,pos_occupancy)

    # PYTHON DEBUGGER - TEMPORARY
    import pdb; pdb.set_trace()

    marker = player['marker']                 # ---- assign current player's marker (re-assigned each turn)

    clear_output_new()

    display_board(board)                            # Display Board
    display_score(player1,player2)


    # ------ Anounce first player ------
    print(f"\n\tThe player chosen to move first is {player['name']} (symbol '{marker}') \n")

    # __________ Game continuity __________ 
    while game_on == True:
       
        # __________ Match continuity  __________ 
        # NOTE: -- maybe below clause needs to be "while..." and the following 'elif' becomes 'if'
        if match_on == True and len(pos_vacancy) > 0:          # loop until a win, or until board full 


            # _______ Each Turn  _________________   
            
            #print(name2,player2,marker2,name1,player1,marker1,player,marker)
            position = player_choice(board,player,pos_vacancy,marker,marker1,marker2,num_players,winstatus)
            #position = player_choices(board,player,pos_vacancy,marker,marker1,marker2,num_players)
            
            if position == 'quit':                              
                match_on = False
                game_on = False
                break
            elif position == 'pre-win': # TESTING CLAUSE - TEMPORARY
                match_on = False # TESTING CLAUSE - TEMPORARY
                game_on = False # TESTING CLAUSE - TEMPORARY
                break # TESTING CLAUSE - TEMPORARY
            else:
                pass
            

            # ---------- position specified, proceed
            place_marker(board, marker, position)               # adds the marker to the board

            # ---- check if player has won 
            winstatus,wincount = win_check(board,marker)         # check if player won
            
            if winstatus == True:
                game_on = True
                match_on = False
            else:
                pass
                    
            # ---- update list of open / occupied positions
            pos_vacancy,pos_occupancy = get_position_data(board)
            #pos_vacancy.remove(position)
            #pos_occupancy.append(position)

            
            # --- end match if board is full   
            if len(pos_vacancy) == 0:
                game_on = True
                match_on = False
            else:
                pass
            
            clear_output_new()
            
            display_board(board)        # prints the board for next players turn
            display_score(player1,player2)
            
            
            # _______ Switch Turns _______    
         
            if match_on == True and marker == marker1: 
                print(f"\tend of turn for {name1} (marker {marker1})")
                marker = marker2
                player = player2
                print(f"\tnext turn is for {name2} (marker {marker2})\n")
                
            elif match_on == True and marker == marker2: 
                print(f"\tend of turn for {name2} (marker {marker2})")
                marker = marker1
                player = player1
                print(f"\tnext turn is for {name1} (marker {marker1})\n")
                
            else:
                # when match_on = False we come here
                pass
            
        
        # __________ End of Match   __________ 
        elif match_on == False and game_on == True:
            
            clear_output_new()
            
            # ---- Announce Winner ---- 
            if winstatus == True:
                player['score'] += wincount
                display_board(board)
                display_score(player1,player2)
                print(f"Player {player['name']} is the winner! \n\t Number of winning positions = {wincount}")
                pass
            else:
                display_board(board)
                display_score(player1,player2)
                print("no winner")
            
            # ---- Ask Player if Replay ---- IL2, IE00B, function 01
            
            replayQ = replay()
            
            # --- no replay ----
            
            if replayQ == False:        
                print("\nExiting Game...")
                game_on = False
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
                pass
            else:
                print("nothing")
        

    # __________ End Match & End Game   __________   
    if not game_on:
        print("\n\n\tThank you for playing Tic-Tac-Toe!")
        
        (victor,message) = determine_victor(player1,player2)
        print("\t",message)

        print(f"\n Goodbye.")
        
    elif winstatus == False and game_on == False:   # this won't occur because the previous condition matches first anyways
        # test
        print("no win, end of match, gameon false")

if __name__ == "__main__":
   #launch_game(mode='default')
   boardx = ['#', 'O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']    # Empty Board
   launch_game(mode='diag',board=boardx)

else:
   print("Failure to launch")