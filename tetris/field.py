
class Field:

    wall_field: bool
    is_occupied: bool

    def __int__(self, wf, io):
        self.wall_field = wf
        self.is_occupied = io
