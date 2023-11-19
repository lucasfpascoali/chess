from __future__ import annotations
from game.piece import Piece
from game.position import Position
from game.board import Board


class Knight(Piece):
    def __init__(self, color: str, position: Position, board: Board):
        super().__init__(color, position, board, 'N')

    def possible_moves(self) -> list:
        possible_moves = []
        for row in range(0, self.board.rows):
            possible_moves.append([])
            for _ in range(0, self.board.cols):
                possible_moves[row].append(False)

        row = self.position.row
        col = self.position.col

        if self.board.valid_position(Position(row - 2, col + 1), self.color):
            possible_moves[row - 2][col + 1] = True

        if self.board.valid_position(Position(row - 2, col - 1), self.color):
            possible_moves[row - 2][col - 1] = True

        if self.board.valid_position(Position(row - 1, col + 2), self.color):
            possible_moves[row - 1][col + 2] = True

        if self.board.valid_position(Position(row - 1, col - 2), self.color):
            possible_moves[row - 1][col - 2] = True

        if self.board.valid_position(Position(row + 2, col + 1), self.color):
            possible_moves[row + 2][col + 1] = True

        if self.board.valid_position(Position(row + 2, col - 1), self.color):
            possible_moves[row + 2][col - 1] = True

        if self.board.valid_position(Position(row + 1, col + 2), self.color):
            possible_moves[row + 1][col + 2] = True

        if self.board.valid_position(Position(row + 1, col - 2), self.color):
            possible_moves[row + 1][col - 2] = True

        return possible_moves

    def houses_to_enemy_king(self) -> list:
        return []
