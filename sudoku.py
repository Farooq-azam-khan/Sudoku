class Sudoku:
    def __init__(self, rows=9, cols=9):
        self.rows = rows
        self.cols = cols

        self.game_board = []
        for row in range(self.rows):
            self.game_board.append([])
            for col in range(self.cols):
                self.game_board[row].append(0)

    def checkGame(self):
        if self.checkRows() and self.checkCols() and self.checkSumSquares():
            print("winner")
            return True
        return False

    def checkRows(self):
        for row in range(self.rows):
            if not self.checkOneRow(row):
                return False
        return True

    def checkOneRow(self, row):
        isFound = [ False for i in range(self.rows)]
        for val in range(self.rows):
            cell = self.game_board[row][val]
            if isFound[cell]:
                print("row: ", row, "is invalid")
                return False
            else:
                isFound[cell] = True

        trueCount = 0
        for c in isFound:
            if c:
                trueCount+=1
        return trueCount == self.rows

    def checkCols(self):
        for col in range(self.cols):
            if not self.checkOneCol(col):
                return False
        return True

    def checkOneCol(self, col):
        isFound = [False for i in range(self.cols)]
        for val in range(self.cols):
            cell = self.game_board[val][col]
            if isFound[cell]:
                print("col: ", col, "is invalid")
                return False
            else:
                isFound[cell] = True

        trueCount = 0
        for c in isFound:
            if c:
                trueCount+=1
        return trueCount == self.cols

    def checkSumSquares(self):
        pass

    def setValue(self, val, row, col):
        if row < 0 and row > self.rows:

            return False
        if col < 0 and col > self.cols:
            print("invalid move")
            return False
        if val < 0 and val > self.cols:
            print("invalid move")
            return False
        if val > self.rows:
            print("invalid move")
            return False
        self.game_board[row][col] = val
        print("valid move")
        return True

    def __repr__(self):
        ret = "\n"

        # dashes
        dashes = ""
        for i in range(self.cols):
            dashes += "--"

        ret += dashes + "\n"
        for row in range(self.rows):
            if row >0 and row%3==0:
                ret += dashes + "\n"
            ret += "|"

            for col in range(self.cols):
                cell = self.game_board[row][col]
                if col>0 and col%3==0:
                    ret+="|"
                if col == self.cols-1:
                    ret += str(cell)
                else:
                    ret += str(cell) + " "

            ret += "|\n"

        ret+=dashes
        return ret+"\n"

def main():
    game = Sudoku()

    for i in range(game.cols):
        game.setValue(i+1, i,0)

    print(game)
    game.checkGame()

if __name__ == "__main__":
    main()
