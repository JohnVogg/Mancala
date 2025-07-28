# Oi lakoi twn paixtwn
player_X_pits = ('A','B','C','D','E','F')
player_Y_pits = ('6', '5', '4', '3', '2', '1') 


#ena lejiko tou opoiou ta kleidia(keys) einai oi lakoi kai times(values) tou oi apenanti lakoi:
mirror_pit = {'A' : '6', 'B' : '5', 'C' : '4', 'D' : '3', 'E' : '2', 'F' : '1',
            '1' : 'F', '2' : 'E', '3' : 'D', '4' : 'C', '5' : 'B', '6' : 'A'}


#ena lejiko tou opoiou ta kleidia(keys) einai oi lakoi kai oi times(values) einai oi epomenoi lakoi se seira:
path_pit = {'A' : 'B', 'B' : 'C', 'C' : 'D', 'D' : 'E', 'E' : 'F', 'F' : 'X', 'X' : '1',
            '1' : '2', '2' : '3', '3' : '4', '4' : '5', '5' : '6', '6' : 'Y', 'Y' : 'A'} # Opoy X h trapeza toy paixth x kai  gia to Y antistoixa

pit_names = "654321YABCDEFX"
starting_balls = 4                  
    

#To  Prwto tablo tou paixnidiou
def first_board():
    
    return {
    'A' : starting_balls, 'B' : starting_balls, 'C' : starting_balls, 'D' : starting_balls, 'E' : starting_balls, 'F' : starting_balls, 'X' : 0,
    '1' : starting_balls, '2': starting_balls, '3' : starting_balls, '4' : starting_balls, '5' : starting_balls, '6' : starting_balls, 'Y' : 0
    }   
    
    
def live_board(board):
    live_balls_count = [str(board[pit]).rjust(2) for pit in pit_names]

    print(f'''
        +--<<--+--<<--+--<<--+-Player Y-<<-+--<<--+--<<--+--<<--+
        |Y     |6     |5     |4     |3     |2     |1     |X     |
        Y      |  {live_balls_count[0]}  |  {live_balls_count[1]}  |  {live_balls_count[2]}  |  {live_balls_count[3]}  |  {live_balls_count[4]}  |  {live_balls_count[5]}  |      X
        B      |      |      |      |      |      |      |      B
        A  {live_balls_count[6]}  +------+------+------+------+------+------+  {live_balls_count[13]}  A
        N      |A     |B     |C     |D     |E     |F     |      N
        K      |  {live_balls_count[7]}  |  {live_balls_count[8]}  |  {live_balls_count[9]}  |  {live_balls_count[10]}  |  {live_balls_count[11]}  |  {live_balls_count[12]}  |      K
        |      |      |      |      |      |      |      |      |
        +-->>--+-->>--+-->>--+-Player X->>-+->>--+-->>--+-->>--+   
        ''')
        
    
def make_move(turn, board): 
    while True: #Gia synexh elegxo twn apanthsewn toy paixth 
        if turn == "x":
            print("Player X, choose move: A-F")
            player_input = input("> ").upper().strip() #Gia na dexete kai ta mikra kai ta kefalaia 
        else:
            print("Player Y, choose: 1-6")
            player_input = input("> ").strip()
            
        if (turn == "x" and player_input not in player_X_pits) or (turn == "y" and (not player_input.isdigit() or  player_input not in player_Y_pits)):
            print("Select a pit from your side of the board!!")
            continue #gia na zhthsei jana kinhsh apo to paixth
        
        if board.get(player_input) == 0:
            print("Please select a pit that it is not empty!!")  
            continue
        
        return player_input
        

def perform_move(board, turn, pit):
    #arxika ua enhmerwsw to pinaka me tis epiloges toy paixth   
    obvious_balls = board[pit] 
    board[pit] = 0

    while obvious_balls > 0: 
        pit = path_pit[pit] 
        
        if (turn == "x" and pit == "Y") or (turn == "y" and pit == "X"): #Gia na mhn topothetei mpales sth trapeza toy antipaloy
            continue
        
        board[pit] += 1
        obvious_balls -= 1
        
    #Aixmalothsh + O paixths janapaizei
    if turn == "x" and pit in player_X_pits and board[pit] == 1:
        mirror = mirror_pit[pit]
        board["X"] += (board[mirror] + board[pit])
        board[mirror] = 0
        board[pit] = 0
        print("Player X plays again!!")
        return turn #gia na janapaijei
    elif turn == "y" and pit in player_Y_pits and board[pit] == 1:
        mirror =  mirror_pit[pit]
        board["Y"] += (board[mirror] + board[pit])
        board[mirror] = 0
        board[pit] = 0
        print("Player Y plays again!!")
        return turn #gia na janapaijei        
    
    #Enallagh paixtwn
    if turn == "x":
        return "y"
    else:
        return "x"
    


def winner(board):
    
    sum_X = board["A"] + board["B"] + board["C"] + board["D"] + board["E"] + board["F"]
    sum_Y = board['1'] + board['2'] + board['3'] + board['4'] + board['5'] + board['6']
    

    if sum_X == 0: #painrei oles tis mpales pou emeinan apo th meria tou kai tis vazei sth trapeza toy
        board["Y"] += sum_Y
        for pit in player_Y_pits:
            board[pit] = 0 
    elif sum_Y == 0:
        board["X"] += sum_X
        for pit in player_X_pits:
            board[pit] = 0
    
    #Elegxos nikhth
    if sum_X == 0 or sum_Y == 0:
        if board["X"] > board["Y"]:
            return "X"
        elif board["Y"] > board["X"]:
            return "Y"
        else:
            return "tie"
    
    return None      
            
        

#To kyrios programma
board = first_board() #To board einai ena lejiko 
turn = "x" #O paixths X jekinaei 
    
while True: #Gia na trejei h seira toy paixth 
    live_board(board) 
        
    move = make_move(turn, board)
    turn = perform_move(board, turn, move)
        
    #Elegxos gia telos paixnidiou kai emfanish apotelesmatwn 
    winner_result = winner(board)
    if winner_result in ("X", "Y"):
        live_board(board) #deixnei to teliko tablo 
        print(f"Player {winner_result} won the game!!")
        break
    elif winner_result == "tie":
        live_board(board)
        print("There is a tie!")
        break 
