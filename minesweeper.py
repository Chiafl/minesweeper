import board as newboard

start = True
while start:
    while True:
        rows = int(input("Input number of rows: "))
        if rows>0:
            break
    while True:
        columns = int(input("Input number of columns: "))
        if columns>0:
            break
    while True:
        numBombs = int(input("Input number of bombs: "))
        if numBombs<rows*columns:
            break
        else:
            print("Bombs cannot occupy every cell")
    board = newboard.board(rows, columns, numBombs)
    board.printboard()
    b = True
    while b:
        while True:
            row = int(input("Choose a row index: "))-1
            col  = int(input("Choose a column index: "))-1
            if row>=rows or row<0:
                print("Row index is out of bounds!")
            elif col>=columns or col<0:
                print("Column index is out of bounds!")
            else:
                break
        b = board.click(row,col)
        if rows*columns - board.numClicks <= numBombs:
            b = False
            board.printtrueboard()
            print("Congratulations! You win!")
        else:
            board.printboard()
    start = input("Would you like to start a new game? (y/n) ")=="y"
