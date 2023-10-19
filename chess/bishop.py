from __future__ import annotations
from game.piece import Piece
from game.position import Position
from game.board import Board


class Bishop(Piece):
    def __init__(self, color: str, position: Position, board: Board):
        super().__init__(color, position, board, 'B')

    def possible_moves(self) -> list:
        possible_moves = []
        for row in range(0, self.board.rows):
            possible_moves.append([])
            for _ in range(0, self.board.cols):
                possible_moves[row].append(False)

        x = self.position.x
        y = self.position.y

        downRightBreak = False
        downLeftBreak = False
        upRightBreak = False
        upLeftBreak = False
        # Calculating all diagonals in just one loop :)
        for square in range(1, 8):
            pos = Position(x + square, y + square)
            if self.board.valid_position(pos, self.color) and not downRightBreak:
                possible_moves[x + square][y + square] = True
                if self.board.position_has_piece(pos):
                    downRightBreak = True

            pos = Position(x + square, y - square)
            if self.board.valid_position(pos, self.color) and not downLeftBreak:
                possible_moves[x + square][y - square] = True
                if self.board.position_has_piece(pos):
                    downLeftBreak = True

            pos = Position(x - square, y + square)
            if self.board.valid_position(pos, self.color) and not upRightBreak:
                possible_moves[x - square][y + square] = True
                if self.board.position_has_piece(pos):
                    upRightBreak = True

            pos = Position(x - square, y - square)
            if self.board.valid_position(pos, self.color) and not upLeftBreak:
                possible_moves[x - square][y - square] = True
                if self.board.position_has_piece(pos):
                    upLeftBreak = True

            if downLeftBreak and downRightBreak and upLeftBreak and upRightBreak:
                break

        return possible_moves
