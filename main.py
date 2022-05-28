import sys

# read from cmd, we can play from white or blacks perspective
# works when completing perfect solution without mistakes, revise threat computation

files_white = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
files_black = {"a": 7, "b": 6, "c": 5, "d": 4, "e": 3, "f": 2, "g": 1, "h": 0}


def threatened(pos: tuple) -> list:
    threatened = []
    for i in range(8):
        for j in range(8):
            if i == pos[0] or j == pos[1] or (abs(i - pos[0]) == abs(j - pos[1])):
                threatened.append((i,j))
    return threatened


class Game:
    @staticmethod
    def threatened(pos: tuple) -> list:
        threatened = []
        for i in range(8):
            for j in range(8):
                if i == pos[0] or j == pos[1] or (abs(i - pos[0]) == abs(j - pos[1])):
                    threatened.append((i, j))
        return threatened



    def __init__(self, nqueens, perspective = "white"):
        self.board  = [["_" for i in range(8)] for j in range(8)]
        self.nqueens = nqueens
        self.placed_queens = []
        self.introduced = []
        self.perspective = perspective



    def check_threatened(self) -> set:
        # for each placed queen we get their attacked squares
        threat = set()
        for queen in self.placed_queens:
            for item in self.threatened(queen): threat.add(item)
        return threat


    def game_over(self) -> bool:
        if len(self.placed_queens) == self.nqueens:
            print(f"You won")
            solution_found = [self.to_chess_notation(queen) for queen in self.placed_queens]
            print(f"Positions of the queens were: {self.introduced}")
            return True

        if len(self.check_threatened()) == 64:
            print(f"There are no available positions and still {self.nqueens - len(self.placed_queens)}"
                  f" left to place.\nYou lost")
            return True


    def chess_translate(self, chess_pos: tuple) -> tuple:
        # chess position stores first the file and then the rank, for example "a6" is stored as ("a", 6)
        # translates from chess notation into python notation
        if self.perspective == "white":
            return (8 - (chess_pos[1]), files_white[chess_pos[0]])
        else:
            return (chess_pos[1] - 1, files_black[chess_pos[0]])


    def to_chess_notation(self, pos: tuple) -> str:
        rank_file = ""
        if self.perspective == "white":
            # we search for the file in the file dict corresponding to the perspective
            for key,value in files_white.items():
                if value == pos[1]:
                    rank_file += str(key)
                    rank_file += str(8 - pos[0])
                    return rank_file
        else:
            # we search for the file in the file dict corresponding to the perspective
            for key,value in files_white.items():
                if value == pos[1]:
                    rank_file += str(key)
                    rank_file += str(8 - pos[0])
                    return rank_file


    def show_board(self) -> str:
        aux_str = ""
        for row in self.board:
            for item in row:
                aux_str += " " + item
            aux_str += "\n"
        return aux_str

    def chess_notation_threatened(self) -> list:
        return [self.to_chess_notation(pos) for pos in self.check_threatened()]

    def play(self):
        while not self.game_over():
            print(self.show_board())
            file = input("Introduce a file for the queen: ")
            rank = int(input("Introduce a rank for the queen: "))
            pos = self.chess_translate((file, rank))
            # we can use either black's or white's dictionary since their keys are the same
            while (file not in files_black.keys()):
                # if the position is invalid we continue asking the user for valid positions
                print(f"invalid file\n")
                file = input("Introduce a valid file for the queen: ")
                rank = int(input("Introduce a rank for the queen: "))

            # checking whether rank is within the permitted values
            while (rank not in range(1,9)):
                print(f"invalid rank\n")
                file = input("Introduce a file for the queen")
                rank = input("Introduce a valid rank for the queen")
            # now we must check whether the position entered is threatened or not
            while pos in self.check_threatened():
                print(f"Unavailable position, try again\n")
                file = input("Introduce a file for the queen: ")
                rank = int(input("Introduce a valid rank for the queen: "))
                pos = self.chess_translate((file, rank))
            # once the position is valid we place the queen and add it to placed queens
            self.introduced.append("".join([file, str(rank)]))
            self.board[pos[0]][pos[1]] = "Q"
            self.placed_queens.append(pos)




g = Game(8, sys.argv[1])
g.play()




