import numpy as np

from solver import Board
from solver import Piece
from solver import Location

b = Board()
l1 = Location(3, 4)
l2 = Location(8, 1)
l3 = Location(5, 7)
p1 = Piece('a', l1)
p2 = Piece('d', l2)
p3 = Piece('p', l3)
b.pieces = [p1, p2, p3]
print(b)

def can_move(self, piece, l_1, l_2):
    if piece == 'P':
        x_check = l_2.x == l_1.x + 1 or l_2.x == l_1.x - 1
        y_check = l_2.y == l_1.y + 1
        return x_check and y_check

    elif piece == 'T':
        def x_middle_check(p):
            if p.loc.x == l_1.x:
                return p.loc.dist(l_1) + p.loc.dist(l_2) == l_1.dist(l_2)

        def y_middle_check(p):
            if p.loc.y == l_1.y:
                return p.loc.dist(l_1) + p.loc.dist(l_2) == l_1.dist(l_2)

        x_middle = len(filter(x_middle_check, self.pieces)) == 2
        y_middle = len(filter(y_middle_check, self.pieces)) == 2

        x_check = l_1.x == l_2.x and x_middle_check
        y_check = l_2.y == l_2.y and y_middle_check

        return x_check or y_check

# Torre
elif piece.type == 'T':
    # Think better middle check

    def x_middle_check(p):
        if p.loc.x == piece.loc.x:
            distance = p.loc.dist(piece.loc) + p.loc.dist(new_loc)
            return distance == piece.loc.dist(new_loc)

    def y_middle_check(p):
        if p.loc.y == piece.loc.y:
            distance = p.loc.dist(piece.loc) + p.loc.dist(new_loc)
            return distance == piece.loc.dist(new_loc)

    x_middle = len(filter(x_middle_check, self.pieces)) == 2
    y_middle = len(filter(y_middle_check, self.pieces)) == 2

    x_check = piece.loc.x == new_loc.x and x_middle_check
    y_check = piece.loc.y == new_loc.y and y_middle_check

    return x_check or y_check
