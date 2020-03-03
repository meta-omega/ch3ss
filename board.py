from copy   import copy
from utils  import sign

# Board

class Board:
    def __init__(self):
        self.pieces = []
        self.children = []

    def __repr__(self):
        s = ''

        x = max(self.pieces, key = lambda p: p.loc.x).loc.x
        y = max(self.pieces, key = lambda p: p.loc.y).loc.y

        board = [['-' for j in range(x)] for i in range(y)]

        for p in self.pieces:
            board[p.loc.y - 1][p.loc.x - 1] = p.type

        for i in range(y):
            for j in range(x):
                s += f'{board[i][j]}\t'

            s += f'\n\n\n'

        return s

    def is_freeway(self, start, end): # Creo que mejorable usando rectas.
        locations = []
        loc = copy(start)

        def advance():
            loc.x += sign(end.x - loc.x)
            loc.y += sign(end.y - loc.y)

        advance()

        while loc.x != end.x or loc.y != end.y:
            locations.append(copy(loc))
            advance()

        pieces = set([tuple(p.loc) for p in self.pieces])
        locations = set([tuple(l) for l in locations])

        return pieces.isdisjoint(locations)

    def can_move(self, piece, new_loc):
        # Peón
        if piece.type == 'P':
            x_check = abs(piece.loc.x - new_loc.x) == 1
            y_check = new_loc.y == piece.loc.y + 1

            return x_check and y_check

        # Torre
        elif piece.type == 'T':
            x_check = piece.loc.x == new_loc.x
            y_check = piece.loc.y == new_loc.y
            axis_check = x_check or y_check

            return axis_check and self.is_freeway(piece.loc, new_loc)

    def solve(self):
        return
