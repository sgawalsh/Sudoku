import pickle
import Sudoklasses

def startMenu():
    print "Welcome to Stephen's Sudoku App"
    while True:
        choice = raw_input("""What would you like to do?

C > Create new puzzle
L > Load puzzle
D > Delete puzzle

> """)
        if choice == 'c' or choice == 'C':
            while True:
                board1 = Sudoklasses.board()
                print "The board looks like this:"
                board1.printBoard()
                choice1 = raw_input("Is this the board you wish to create? y/n \n> ")
                if choice1 == 'y' or choice1 == 'Y':
                    while True:
                        choice2 = raw_input("Would you like to save this puzzle? y/n\n> ")
                        if choice2 == 'y' or choice2 == 'Y':
                            boardList = pickle.load(open("puzzle.p", "rb"))
                            boardList.append(board1)
                            pickle.dump(boardList, open("puzzle.p", "wb"))
                            break
                        elif choice2 == 'n' or choice2 == 'N':
                            break
                        else:
                            print "hmm.. let's try that again"
                    break
                elif choice1 == 'n' or choice1 == 'N':
                    continue
                else:
                    'que?'
        elif choice == 'l' or choice == 'L':
            boardList = pickle.load(open("puzzle.p", "rb"))
            if len(boardList) is 0:
                print "No saves found."
                continue
            print "Which puzzle do you want to load?"
            for el in xrange(len(boardList)):
                print el + 1, '. ', boardList[el].name
            while True:
                choice = raw_input('> ')
                if choice.isdigit():
                    choice = int(choice)
                    break
                else:
                    print 'choose a number pls.'
            board1 = boardList[choice - 1]
            print "Here is the board"
            board1.printBoard()
            choice = raw_input("Is this the board you want to load? y/n \n> ")
            if choice == 'y' or choice == 'Y':
                break
            elif choice == 'n' or choice == 'N':
                continue
            else:
                print 'wat'
        elif choice == 'd' or choice == 'D':
            boardList = pickle.load(open("puzzle.p", "rb"))
            if len(boardList) is 0:
                print "No saves found."
                continue
            print "Which puzzle do you want to delete?"
            for el in xrange(len(boardList)):
                print el + 1, '. ', boardList[el].name
            while True:
                choice = raw_input('> ')
                if choice.isdigit():
                    choice = int(choice)
                    del boardList[choice - 1]
                    pickle.dump(boardList, open("puzzle.p", "wb"))
                    break
                else:
                    print 'choose a number pls.'
        else:
            'no comprendo senor.'
    return board1

board1 = startMenu()

while not board1.checkBoardSolved():
    board1.printBoard()
    board1.solveRow()
    board1.solveCol()
    for y in xrange(0, 8, 3):
        for x in xrange(0, 8, 3):
            board1.solveSquare(x, y)
    board1.potRow()
    board1.potCol()
    for y in xrange(0, 8, 3):
        for x in xrange(0, 8, 3):
            board1.potSquare(x, y)

print 'wow you solved the board'
if board1.validateBoard():
    raw_input('you win')
else:
    raw_input('you lose')