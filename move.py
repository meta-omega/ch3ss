# Move

class Move:
    def __init__(self, piece, loc):
        self.piece = piece
        self.loc = loc

    def __iter__(self):
        yield self.piece
        yield self.loc

    def __eq__(self, other):
        if isinstance(other, Move):
            return tuple(self) == tuple(other)

        return False

    def __repr__(self):
        return f'{{{self.piece}, {self.loc}}}'

    def is_valid(self, ctx = None):
        loc = self.piece.loc
        type = self.piece.type
        new_loc = self.loc

        no_obstacles = True if not ctx else ctx.is_freeway(loc, new_loc)

        # El movimiento require de un cambio de ubicación.
        if loc == new_loc:
            return False

        # Peón
        elif type == 'P':
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

            return axis_check and no_obstacles

        # Alfil
        elif type == 'A':
            diag_check = loc.dist_x(new_loc) == loc.dist_y(new_loc)

            return diag_check and no_obstacles

        # Dama
        elif type == 'D':
            x_check = loc.x == new_loc.x
            y_check = loc.y == new_loc.y
            diag_check = loc.dist_x(new_loc) == loc.dist_y(new_loc)
            locs_check = x_check or y_check or diag_check

            return locs_check and no_obstacles

        # Caballo
        elif type == 'C':
            x_check = 0 < loc.dist_x(new_loc) < 3
            y_check = 0 < loc.dist_y(new_loc) < 3
            sum_check = loc.dist(new_loc) == 3

            return x_check and y_check and sum_check

        return False
