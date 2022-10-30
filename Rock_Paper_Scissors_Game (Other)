### This is Rock, Scissors, Paper game you play with your system (computer). 

import random, sys 

print('ROCK, PAPER, SCISSORS')

# These variables will keep track of the number of the wins, losses, and ties. 
wins = 0
losses = 0
ties = 0

while True: # This section is the main game loop. 
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The Player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors orr (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input look. 
        print('Type one of r, p, s, or q.')
        
    # This section displays what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('SCISSORS versus...')
        
    # This section will display what the computer chose: 
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SISCORS')
        
    # This section will display and record the wins/losss/ties:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
        
   # Enjoy the game!!!!
    
