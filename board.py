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
        loc = piece.loc
        type = piece.type

        # Peón
        if type == 'P':
            x_check = abs(loc.x - new_loc.x) == 1
            y_check = new_loc.y == loc.y + 1

            return x_check and y_check

        # Rey
        elif type == 'R':
            x_check = loc.dist_x(new_loc) == 1
            y_check = loc.dist_y(new_loc) == 1

            return x_check and y_check

        # Torre
        elif type == 'T':
            x_check = loc.x == new_loc.x
            y_check = loc.y == new_loc.y
            axis_check = x_check or y_check

            return axis_check and self.is_freeway(loc, new_loc)

        # Alfil
        elif type == 'A':
            diag_check = loc.dist_x(new_loc) == loc.dist_y(new_loc)

            return diag_check and self.is_freeway(loc, new_loc)

    def solve(self):
        return
