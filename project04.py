#TicTacTie

#1. input for loop
#2. board structure
#3. input for 9 values
#4. user move
#5. computer move
#6. is any free space
#7. winner
#8. post work after the winner


board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        move = input("Select a possition to enter the X between 1 to 9 : ")
        # Using try-except, when move not convert to the int then aoutomatically move to except tab
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Possition is already fill...")
            else:
                print("Invalied possition, please enter a correct possition number...")

        except:
            print("Please enter a number...")

def computerMove():
    possibleMove = [ x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMove:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornerOpen = []
    for i in possibleMove:
        if i in [1, 3, 7, 9]:
            cornerOpen.append(i)

    if len(cornerOpen) > 0:
        move = selectRandom(cornerOpen)
        return move

    if 5 in possibleMove:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMove:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
     import random
     ln = len(li)
     r = random.randrange(0, ln)
     return li[r]

def main():
    print("Welcome to the game!!!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print("Sorry you are lose!!!")
            break

        if not isWinner(board, 'X'):
            move = computerMove()
            if move == 0:
                print(" ")
            else:
                insertLetter('O', move)
                print("Computer place an O on possition ", move)
                printBoard(board)
        else:
            print("You win!!!")
            break


    if isBoardFull(board):
        print("Tie game!!!")


while True:
    x = input("Dou you want to play again? (y/n) : ")
    x = x.lower()
    if x == 'y':
        board = [' ' for x in range(10)]
        print('------------------')
        main()
    else:
        break

#printBoard(board)
