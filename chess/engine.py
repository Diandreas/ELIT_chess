


class GameSate():
    def _init_(self):
        self.board = [
            ['/white/rook', '/white/knight', '/white/bishop', '/white/queen', '/white/king', '/white/bishop', '/white/knight', '/white/rook'],
            ['/white/pawn', '/white/pawn', '/white/pawn', '/white/pawn', '/white/pawn', '/white/pawn', '/white/pawn', '/white/pawn'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['/black/pawn', '/black/pawn', '/black/pawn', '/black/pawn', '/black/pawn', '/black/pawn', '/black/pawn', '/black/pawn'],
            ['/black/rook', '/black/knight', '/black/bishop', '/black/king', '/black/queen', '/black/bishop', '/black/knight', '/black/rook'],

        ]
        self.whiteToMove = True
        self.moveLog= []


