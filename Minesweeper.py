import random
import sys


class GameEngine:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = None
        self._reveal = None
        self._mineLoc = None
        self.revealCount = self.rows * self.cols

    def getUserChoice(self):
        print('Enter your location: i,j')
        choice = sys.stdin.readline()
        return (int(choice[0]), int(choice[2]))

    def _create_board(self):
        self.board = []
        for i in range(self.rows):
            self.board.append([0]*self.cols)

        self._reveal = []
        for i in range(self.rows):
            self._reveal.append([False]*self.cols)

        self._mineLoc = self._get_random_mine_locations()
        self._compute_mine_scores(self._mineLoc)

    def _get_random_mine_locations(self):
        res = set()
        j = 0
        # Ignore duplicates and fill set with requires mine locations
        while j < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            if (r,c) not in res:
                res.add((r,c))
                j += 1

        return res

    def _compute_mine_scores(self, mineLoc):
        for loc in mineLoc:     # for each loc
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (loc[0] + i) in range(0, self.rows) and (loc[1] + j) in range(0, self.cols):
                        self.board[loc[0] + i][loc[1] + j] += 1
    

    def _reveal_board(self, userLoc):
        if (userLoc[0]) in range(0, self.rows) and (userLoc[1]) in range(0, self.cols) and not (self._reveal[userLoc[0]][userLoc[1]]):
                self._reveal[userLoc[0]][userLoc[1]] = True
                self.revealCount -= 1
                if self.board[userLoc[0]][userLoc[1]] == 0:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            self._reveal_board((userLoc[0] + i, userLoc[1] + j))


    def print_board(self):
        print('    ', end='')
        print(*list(range(self.cols)))
        print('---------------------')
        for i in range(0, self.rows):
            print(i, end=' | ')
            for j in range(0, self.cols):
                if self._reveal[i][j]:
                    print(self.board[i][j], end=' ')
                else:
                    print('X', end=' ')
            print()
        print('--------------')

    def start_game(self):
        self._create_board()
        self.print_board()

        while self.revealCount > self.mines: # TODO change to end game on success.
            uc = self.getUserChoice()
            if uc in self._mineLoc:
                print("Stepped on mine. Boom. End of game.")
                self.print_board()
                print('Mine locations: ', self._mineLoc)
                return
            self._reveal_board(uc)
            self.print_board()
        print("You Won!!")
        self.print_board()
        print('Mine locations: ', self._mineLoc)

if __name__ == "__main__":
    g = GameEngine(9, 9, 10)
    g.start_game()
            
            
