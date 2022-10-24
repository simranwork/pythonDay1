
# Hangman : The game


import random
from words import words

def hangman():

    list_of_words = words
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ''
    valid_entry = set('abcdefghijklmnopqrstuvwxyz')
    while len(word) >0:
        main_word = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word +letter 
            else:
                main_word = main_word +'_ '

        if main_word == word:
            print(main_word)
            print('you won!')
            break        

        print('Guess the word', main_word)
        guess = input()

        if guess in valid_entry:
            guessmade = guessmade +guess
        else:
            print('enter valid character')
            guess = input()

        if guess not in word:
            turns = turns -1
            if turns == 9:
                print('9 turns left!')
                print('--------------------')
            if turns ==8:
                print('8 turns left!')
                print('--------------------')
                print('         O           ')
            if turns ==7:
                print('7 turns left!')
                print('--------------------')
                print('         O           ')
                print('         |           ')
            if turns ==6:
                print('6 turns left!')
                print('--------------------')
                print('         O           ')
                print('         |           ')
                print('        /            ')
            if turns ==5:
                print('5 turns left!')
                print('--------------------')
                print('         O           ')
                print('         |           ')
                print('        / \           ')
                
            if turns ==4:
                print('4 turns left!')
                print('--------------------')
                print('        \O           ')
                print('         |           ')
                print('        / \           ')
            if turns ==3:
                print('3 turns left!')
                print('--------------------')
                print('        \O/           ')
                print('         |           ')
                print('        / \           ')
            if turns ==2:
                print('2 turns left!')
                print('--------------------')
                print('        \O/ |          ')
                print('         |           ')
                print('        / \           ')
            if turns ==1:
                print('last breath left!!')
                print('--------------------')
                print('        \O/__|          ')
                print('         |           ')
                print('        / \           ')
            if turns ==0:
                print('You loose!!')
                print('--------------------')
                print('         O__|          ')
                print('        /|\           ')
                print('        / \           ')
                print('Hangman died!!')
                print(f'the correct word was {word}')


                
name = input('Enter your name:')
print(f'Welcome {name}!')
print('----------------------------')
print('Try to guess the word in less than 10 attempts.')               









hangman()
