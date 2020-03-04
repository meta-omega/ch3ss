from move       import Move
from piece      import Piece
from board      import Board
from location   import Location

# C3 Chess Solver

'''

A   Alfil
T   Torre
C   Caballo
P   Peón
D   Dama
R   Rey

'''

b = Board()

l1 = Location(3, 5)
l2 = Location(4, 4)
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
p6 = Piece('C', l6)
p7 = Piece('T', l7)

b.pieces = [p1, p2, p3, p4, p5, p6, p7]

m1 = Move(p1, l2)
m2 = Move(p2, l3)
m3 = Move(p3, l4)
m4 = Move(p4, l5)
m5 = Move(p5, l6)
m6 = Move(p6, l7)
m7 = Move(p7, l1)

print('\n\n', b)
