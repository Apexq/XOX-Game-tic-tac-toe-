import random

class Game():
    def __init__(self):
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.statu = True
        self.moves = 0
        self.mode = None

    def resetGame(self):
        self.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
        self.statu = True
        self.moves = 0
        self.mode = None

    def selectMode(self):
        print("Select Game Mode:")
        print("1 - Two Players")
        print("2 - One Player (vs Computer)")
        mode = input("Enter 1 or 2: ").strip()
        while mode not in ["1", "2"]:
            print("Invalid choice. Please select 1 or 2.")
            mode = input("Enter 1 or 2: ").strip()
        self.mode = int(mode)

    def Play(self):
        if self.mode is None:
            self.selectMode()

        if self.mode == 1:  # Two-player mode
            if self.moves % 2 == 0:
                self.p1choose()
            else:
                self.p2choose()
        elif self.mode == 2:  # One-player mode
            if self.moves % 2 == 0:
                self.p1choose()
            else:
                self.computerMove()

        self.statu = self.GameCheck()

        if not self.statu:
            self.showBoard()
            if self.moves % 2 == 0:  
                winner = "Player 1 (X)"
            else:
                winner = "Player 2 (O)"
            print("Game Over! Winner is: {}".format(winner))
            self.askReplay()
        else:
            self.moves += 1  # Increment moves after checking game status
            if self.moves == 9:  # Tie condition
                self.showBoard()
                print("Game Over! No Winner")
                self.askReplay()

    def p1choose(self):
        self.showBoard()
        print("Player 1 (X) Choose Row and Column")
        row = int(input("Row: "))
        while row > 3 or row < 1:
            print("Invalid Row")
            row = int(input("Row: "))
        col = int(input("Column: "))
        while col > 3 or col < 1:
            print("Invalid Column")
            col = int(input("Column: "))

        if self.isAvailable(row, col):
            self.board[row - 1][col - 1] = "X"
        else:
            print("Invalid Move!, Try Again")
            self.p1choose()

    def p2choose(self):
        self.showBoard()
        print("Player 2 (O) Choose Row and Column")
        row = int(input("Row: "))
        while row > 3 or row < 1:
            print("Invalid Row")
            row = int(input("Row: "))
        col = int(input("Column: "))
        while col > 3 or col < 1:
            print("Invalid Column")
            col = int(input("Column: "))

        if self.isAvailable(row, col):
            self.board[row - 1][col - 1] = "O"
        else:
            print("Invalid Move!, Try Again")
            self.p2choose()

    def computerMove(self):
        available_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == "_"]
        if available_moves:
            row, col = random.choice(available_moves)
            self.board[row][col] = "O"
            print("Computer's Move: Row: {}, Column: {}".format(row + 1, col + 1))

    def isAvailable(self, row, col):
        if self.board[row - 1][col - 1] == "_":
            return True
        return False

    def showBoard(self):
        for i in self.board:
            print(i)

    def GameCheck(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != "_":
                return False
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != "_":
                return False
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != "_":
            return False
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != "_":
            return False
        return True

    def askReplay(self):
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay == "yes":
            self.resetGame()
        else:
            print("Thanks for playing!")
            self.statu = False


game = Game()
while game.statu:
    game.Play()