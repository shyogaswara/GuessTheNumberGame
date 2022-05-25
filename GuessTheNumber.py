'''
GUESS THE NUMBER MULTIPLAYER
Created on Mei 25, 2022

@author: sh.yogaswara@gmail.com
'''


'''
Criteria :
1. First player give range to game for Second player to guess
2. Game give a clue if guess is higher or lower
3. Win Messages with how many time the player take guess
4. Ask player to continue or stop playing
'''

from random import randint


def give_range():
    _start = int(input('starting number : '))
    _end = int(input('last number : '))
    _value = randint(_start,_end)

    return _start, _end, _value

def getting_guess():
    _guess = int(input('guess the number : '))
    return _guess

def getting_clues(guess,value):
    if guess > value:
        print('the number is lower!')
    elif guess < value:
        print('the number is higher!')

def play_game():
    start, end, value = give_range()
    guess = None
    _count = 0

    while guess != value:
        guess = getting_guess()
        getting_clues(guess,value)
        _count += 1

    print(f'''Congrats, The number you're guessing is correct after {_count} times guess''')

def main():
    run = True

    while run:
        play_game()
        _run = input('Again? (y/n)     ')
        if _run != 'y':
            run = False



if __name__ == '__main__':
    main()
