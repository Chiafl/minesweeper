import random
import queue

class board:
    def __init__(self, rows:int, cols:int, numBombs:int):
        self.board = [[cell(i, j) for j in range(cols)] for i in range(rows)]
        while numBombs>0:
            r = random.randint(0, rows-1)
            c = random.randint(0, cols-1)
            if self.board[r][c].checkbomb():
                continue
            else:
                self.board[r][c].setbomb()
                numBombs-=1
        self.numClicks = 0
        self.rows = rows
        self.cols = cols

    def click(self, row:int, col:int):
        if self.board[row][col].checkclicked():
            return True
        elif self.board[row][col].click():
            self.search(row,col)
            return True
        else:
            return False

    def printboard(self):
        print()
        for i in range(len(self.board)):
            print("\t\t ", end='')
            for j in range(len(self.board[0])):
                print(self.board[i][j].getValue()+" ", end='')
            print("\n")

    def printtrueboard(self):
        print()
        for i in range(len(self.board)):
            print("\t\t ", end='')
            for j in range(len(self.board[0])):
                if self.board[i][j].checkbomb():
                    print("[*] ", end='')
                else:
                    print(self.board[i][j].getValue()+" ", end='')
            print("\n")

    def getBomb(self):
        return self.bombs

    def search(self, row, col):
        q = queue.Queue()
        S = set()
        q.put(self.board[row][col])
        while not q.empty():
            v = q.get()
            if v.checkbomb() or v in S or v.getNum()>0:
                continue
            v.click()
            self.numClicks += 1
            S.add(v)
            r = v.getRow()
            c = v.getCol()
            buff = []
            for i in range(-1,2):
                for j in range(-1,2):
                    if (r+i>=0 and c+j>=0 and r+i<self.rows and c+j<self.cols): 
                        cell = self.board[r+i][c+j]
                        if v.getNum()>0:
                            continue
                        elif cell.checkbomb():
                            v.incrementNum()
                        else:
                            buff.append(cell)
            if v.getNum()>0:
                v.showNum()
            else:
                for x in buff: q.put(x) 

class cell:
    def __init__(self, row:int, col:int):
        self.clicked = False
        self.isbomb = False
        self.value = '[?]'
        self.row = row
        self.col = col
        self.num = 0

    def click(self)->bool:
        self.clicked = True
        if self.checkbomb():
            self.value = '[X]'
            print("You blew up a bomb!")
            return False
        else:
            self.value = '[ ]'
            return True

    def checkclicked(self)->bool:
        if self.clicked:
            return True
        return False

    def checkbomb(self)->bool:
        if self.isbomb:
            return True
        return False

    def getValue(self):
        return self.value
    
    def setbomb(self):
        self.isbomb = True
        return

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getNum(self):
        return self.num

    def incrementNum(self):
        self.num+=1

    def showNum(self):
        self.value = "["+str(self.num)+"]"
