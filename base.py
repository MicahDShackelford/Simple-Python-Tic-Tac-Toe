# This is a basic python tic tac toe game.
# The structure of the board is a 1d array ['_','_','_','_','_','_','_','_','_'] <- Base board
# A board will be populated by Xs and Os as the game progresses 

def playGame():
    '''
        Purpose: Initalized the game
        Input: None
        Output: None
    '''
    
    # Non local vars
    solved = False
    player = 'x'
    board = ['_','_','_','_','_','_','_','_','_']
    
    def togglePiece(position):
        '''
            Purpose: Toggles a board piece (Also runs a win check)
            Input: Takes in the position where the board piece is being added
            Output: None ( Modifies nonlocal variables )
        '''
        # Check score
        nonlocal player
        if board[position] == '_':
            board[position] = player
            if player == 'x':
                player = 'y'
            else:
                player = 'x'
        else:
            print(f'Sorry that position is already occupied by {board[position]}. \nTry another space!')
    # Introduction
    print('Welcome to my basic terminal Tic-Tac-Toe game!\nTo play you will be asked to enter a number that will represent the box you would like to fill')
    print('Example:\n 1 # 2 # 3 \n###########\n 4 # 5 # 6 \n###########\n 7 # 8 # 9 \nUser Enters: 3 \nNew Board: \n   #   # X \n###########\n   #   #   \n###########\n   #   #   \n-------------------------------')
    # Continues running the game till a win is achieved
    while not solved:
        print(f'Current Board: \n {board[0]} # {board[1]} # {board[2]} \n###########\n {board[3]} # {board[4]} # {board[5]} \n###########\n {board[6]} # {board[7]} # {board[8]} ')
        try:
            move = int(input(f'Enter your move ({player.upper()}): '))
        except:
            print('Invalid input, please enter a number')
            continue
        if move >= 1 and  move <= 9:
            togglePiece(move - 1)
        else:
            print('Invalid input, please enter a number between 1 and 9')
            continue

        
playGame()
