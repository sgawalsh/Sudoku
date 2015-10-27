class square(object):

    def __init__(self, x, y):
        self.pot = [1,2,3,4,5,6,7,8,9]
        self.x = x
        self.y = y
        self.solved = False

    def assignVal(self, val):
        self.pot = [val]
        self.solved = True

    def remPot(self, rems):
        for el in rems:
            if el in self.pot:
                self.pot.remove(el)

        if self.checkSolved():
            return True
        else:
            return False

    def checkSolved(self):
        if len(self.pot) == 1:
            self.solved = True
            print"A %d has been found at %d, %d." %(self.pot[0], self.x, self.y)
            #raw_input("A %d has been found at %d, %d." %(self.pot[0], self.x, self.y))
            return True
        else:
            return False

class board(object):

    def __init__(self):
        print "Let's make a board"

        self.board = []
        self.name = raw_input("Select a name for this board.\n> ")

        for el in xrange(9):
            row = []
            for el2 in xrange(9):
                row.append(square(el2, el))
            self.board.append(row)

        self.assignVals()
        self.printBoard()

    def setPotentials(self, n, pots): #was used for testing, used to set potential values for squares
        count = 0
        while count < n:
            x = int(raw_input('x = ?'))
            y = int(raw_input('y = ?'))
            self.board[y][x].pot = pots
            count += 1

    def solveRow(self): # eliminates potential values in a row and checks if any are solved
        for y in xrange(9):
            nums = []
            for x1 in xrange(9):
                if self.board[y][x1].solved:
                    nums.append(self.board[y][x1].pot[0])
            while True:
                for x2 in xrange(9):
                    if not self.board[y][x2].solved:
                        if self.board[y][x2].remPot(nums):
                            print 'row find!'
                            nums.append(self.board[y][x2].pot[0])
                            self.printBoard()
                            self.oneCol(x2, y, self.board[y][x2].pot[0])
                            self.oneSquare(x2, y, self.board[y][x2].pot[0])
                            break
                else:
                    break

    def potRow(self): # checks to see if if any groups of values are limited to certain areas, then eliminates those potential values from other squares
        for y in xrange(9):
            for x1 in xrange(9):
                if not self.board[y][x1].solved:
                    matches = []
                    set = list(self.board[y][x1].pot)
                    for x2 in xrange(9):
                        inSet = True
                        if not all([v in set for v in self.board[y][x2].pot ]):
                            inSet = False
                        if inSet:
                            matches.append(x2)
                    if len(matches) is len(set):
                        toRemove = range(9)
                        for el in matches:
                            toRemove.remove(el)
                        for el in toRemove:
                            if not self.board[y][el].solved and self.board[y][el].remPot(set):
                                print 'potrow find'
                                self.printBoard()

    def solveCol(self): #solveRow for columns
        for x1 in xrange(9):
            nums = list()
            for y1 in xrange(9):
                if self.board[y1][x1].solved:
                    nums.append(self.board[y1][x1].pot[0])
            while True:
                for y2 in xrange(9):
                    if not self.board[y2][x1].solved:
                        if self.board[y2][x1].remPot(nums):
                            print 'col find!'
                            nums.append(self.board[y2][x1].pot[0])
                            self.printBoard()
                            self.oneRow(x1, y2, self.board[y2][x1].pot[0])
                            self.oneSquare(x1, y2, self.board[y2][x1].pot[0])
                            break
                else:
                    break

    def potCol(self): #potRow for columns
        for x in xrange(9):
            for y1 in xrange(9):
                if not self.board[y1][x].solved:
                    matches = []
                    set = list(self.board[y1][x].pot)
                    for y2 in xrange(9):
                        inSet = True
                        if not all([v in set for v in self.board[y2][x].pot ]):
                            inSet = False
                        if inSet:
                            matches.append(y2)
                    if len(matches) is len(set):
                        toRemove = range(9)
                        for el in matches:
                            toRemove.remove(el)
                        for el in toRemove:
                            if not self.board[el][x].solved and self.board[el][x].remPot(set):
                                print 'pot col find'
                                self.printBoard()

    def solveSquare(self, x1, y1): #solveRow for squares
        nums = []
        for x in xrange(x1, x1+3):
            for y in xrange(y1, y1+3):
                if self.board[y][x].solved:
                    nums.append(self.board[y][x].pot[0])
        while True:
            for x in xrange(x1, x1+3):
                for y in xrange(y1, y1+3):
                    if not self.board[y][x].solved:
                        if self.board[y][x].remPot(nums):
                            print 'square find!'
                            nums.append(self.board[y][x].pot[0])
                            self.printBoard()
                            self.oneRow(x, y, self.board[y][x].pot[0])
                            self.oneCol(x, y, self.board[y][x].pot[0])
                            break
            else:
                break

    def oneCol(self, x, y, val): #after a number is found, this is executed to see if the new find leads to new info
        y1 = range(9)
        y1.remove(y)
        for y2 in y1:
            if val in self.board[y2][x].pot:
                self.board[y2][x].pot.remove(val)

    def oneRow(self, x, y, val): #after a number is found, this is executed to see if the new find leads to new info
        x1 = range(9)
        x1.remove(x)
        for x2 in x1:
            if val in self.board[y][x2].pot:
                self.board[y][x2].pot.remove(val)

    def oneSquare(self, x, y, val):
        for y1 in xrange(3, 10, 3):
            if y < y1:
                for x1 in xrange(3, 10, 3):
                    if x < x1:
                        x1 -=3
                        y1 -=3
                        for x2 in xrange(3):
                            for y2 in xrange(3):
                                if x2 + x1 is not x and y2 + y1 is not y:
                                    if val in self.board[y1 + y2][x1 + x2].pot:
                                        self.board[y1 + y2][x1 + x2].pot.remove(val)
                        return

    def potSquare(self, xin, yin): #potRow for squares
        for x1 in xrange(xin, xin+3):
            for y1 in xrange(yin, yin+3):
                if not self.board[y1][x1].solved:
                    matches = []
                    set = list(self.board[y1][x1].pot)
                    for x2 in xrange(xin, xin+3):
                        for y2 in xrange(yin, yin+3):
                            inSet = True
                            if not all([v in set for v in self.board[y2][x2].pot ]):
                                inSet = False
                            if inSet:
                                matches.append((y2,x2))
                        if len(matches) is len(set):
                            toRemove = [(yin, xin), (yin, xin+1), (yin, xin+2), (yin+1, xin), (yin+1, xin+1), (yin+1, xin+2), (yin+2, xin), (yin+2, xin+1), (yin+2, xin+2)]
                            for el in matches:
                                toRemove.remove(el)
                            for el in toRemove:
                                if not self.board[el[0]][el[1]].solved and self.board[el[0]][el[1]].remPot(set):
                                    print 'pot square find'
                                    self.printBoard()

    def checkBoardSolved(self):
        for x in xrange(9):
            for y in xrange(9):
                if not self.board[y][x].solved:
                    print "Board is not solved"
                    return False
        else:
            return True

    def assignVals(self): #user inputs values
        print "Lets assign values"
        for y in xrange(9):
            for x in xrange(9):
                while(True):
                    inNum = raw_input("What is the value of square (%d, %d)? press 0 for unknown \n> " %(x,y))
                    if not inNum.isdigit():
                        print "People usually use numbers for this sort of thing.."
                    elif 0 < int(inNum) < 10:
                        self.board[y][x].assignVal(int(inNum))
                        break
                    elif inNum == '0':
                        break
                    else:
                        print "That's the wrong number."

    def assignVal(self):
        n = 0
        while n < 2:
            x = int(raw_input("x = ? \n >"))
            y = int(raw_input("y = ? \n >"))
            val = int(raw_input("value = ? \n >"))
            self.board[y][x].assignVal(val)
            n += 1

    def printBoard(self):
        for y1 in xrange(3):
            for y2 in xrange(3):
                for x1 in xrange(3):
                    for x2 in xrange(3):
                        if self.board[y1 * 3 + y2][x2 + x1 * 3].solved:
                            print self.board[y1 * 3 + y2][x2 + x1 * 3].pot[0],
                        else:
                            print 'x',
                        print " ",
                    if x1 < 2:
                        print '| ',
                print "\n"
            if y1 < 2:
                for count in xrange(20):
                    print '-',
                print '\n'

    def validateBoard(self): #checks if any rules have been broken during the solving process
        for y in xrange(9):
            countList = [0] * 9
            for x in xrange(9):
                countList[self.board[y][x].pot[0] - 1] += 1
            if not all([v == 1 for v in countList ]):
                print "Puzzle is not valid"
                return False

        for x in xrange(9):
            countList = [0] * 9
            for y in xrange(9):
                countList[self.board[y][x].pot[0] - 1] += 1
            if not all([v == 1 for v in countList ]):
                print "Puzzle is not valid"
                return False

        for y1 in xrange(0, 8, 3):
            for x1 in xrange(0, 8, 3):
               countList = [0] * 9
               for y2 in xrange(3):
                   for x2 in xrange(3):
                       countList[self.board[y1 + y2][x1 + x2].pot[0] - 1] += 1
               if not all([v == 1 for v in countList ]):
                   print "Puzzle is not valid"
                   return False
        print "Puzzle is valid"
        return True