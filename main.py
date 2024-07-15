import random

print('Rock Paper Scissors 1')

while True:
    sideA = input("Choose between rock, paper, scissors (enter q to quit): ").lower()
    if sideA == 'q':
        break
    options = ['rock','paper','scissors']
    while sideA not in options:
        print ('Invalid answer. Try again.')
        sideA = input("Choose between rock, paper, scissors: ").lower()
    sideB = random.choice(options)
    print ('Your opponent chose: ' + sideB)

    if sideA == sideB:
        print('You both chose ' + sideA + ' its a tie!')

    elif (sideA == 'paper' and sideB == 'scissors' or
        sideA == 'scissors' and sideB == 'rock' or
        sideA == 'rock' and sideB == 'paper'):
        print ('You lost!')
    else:
        print ('You won!')

print('Thanks for playing!!')