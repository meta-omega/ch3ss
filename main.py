from piece      import Piece
from board      import Board
from location   import Location

# C3 Chess Solver

'''
        A       Alfil
        T       Torre       Done + Checked
        C       Caballo
        P       Peón        Done + Checked
        D       Dama
        R       Rey
'''

b = Board()

l1 = Location(3, 4)
l2 = Location(8, 1)
l3 = Location(5, 7)
l4 = Location(6, 8)
l5 = Location(4, 8)
l6 = Location(3, 6)
l7 = Location(6, 4)

p1 = Piece('A', l1)
p2 = Piece('D', l2)
p3 = Piece('P', l3)
p4 = Piece('R', l4)
p5 = Piece('T', l5)
p6 = Piece('T', l6)
p7 = Piece('T', l7)

b.pieces = [p1, p2, p3, p4, p5, p6, p7]

print('\n\n', b)
