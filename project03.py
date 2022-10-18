# Hangman Game
#1. Develop the Interface
#2. Predefined list
#3. Instruction
#4. Check the word
# --> If rigth then enter in empty list
# --> Then draw a figure
#5. Reduce the turns
#6. Generate the figure

import random
#function
def hangman():
    word = random.choice(['catwoman', 'batman', 'superman', 'iornman', 'hulk', 'avengers', 'spiderman', 'flash', 'thor', 'venom'])
    valiedLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word):
        main = ''
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + '_' + ' '

        if main == word:
            print(word)
            print('You win!!!')
            break
        print('Guess the word : ', main)
        guess = input()

        if guess in valiedLetters:
            guessmade = guessmade + guess
        else:
            print('Enter a valid charactor : ')
            guess = input()
        if guess not in word:
            turns = turns - 1
            #figure
            if turns == 9:
                print("9 turns left")
                print(" ---------- ")
            if turns == 8:
                print("8 turns left")
                print(" ---------- ")
                print("      O     ")
            if turns == 7:
                print("7 turns left")
                print(" ---------- ")
                print("      O     ")
                print("      |     ")
            if turns == 6:
                print("6 turns left")
                print(" ---------- ")
                print("      O     ")
                print("      |     ")
                print("     /      ")
            if turns == 5:
                print("5 turns left")
                print(" ---------- ")
                print("      O     ")
                print("      |     ")
                print("     / \    ")
            if turns == 4:
                print("4 turns left")
                print(" ---------- ")
                print("    \ O     ")
                print("      |     ")
                print("     / \    ")
            if turns == 3:
                print("3 turns left")
                print(" ---------- ")
                print("    \ O /   ")
                print("      |     ")
                print("     / \    ")
            if turns == 2:
                print("2 turns left")
                print(" ---------- ")
                print("    \ O /|  ")
                print("      |     ")
                print("     / \    ")
            if turns == 1:
                print("1 turns left")
                print(" ---------- ")
                print("    \ O_|/  ")
                print("      |     ")
                print("     / \    ")
            if turns == 0:
                print("You lose")
                print("You let a kind an die")
                print(" ---------- ")
                print("      O_|   ")
                print("     /|\    ")
                print("     / \    ")
                break


name = input('Enter your name : ')
print('Welcome ', name)
print('-----------------------')
print('Try to guess he word in less than 10 attempts')

hangman()
