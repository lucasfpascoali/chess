from __future__ import annotations
from game.piece import Piece
from game.position import Position
from game.board import Board


class King(Piece):
    def __init__(self, color: str, position: Position, board: Board):
        super().__init__(color, position, board, "K")

    def possible_moves(self) -> list:
        possible_moves = []
        for row in range(0, self.board.rows):
            possible_moves.append([])
            for _ in range(0, self.board.cols):
                possible_moves[row].append(False)

        row = self.position.row
        col = self.position.col

        # Up
        new_pos = Position(row - 1, col)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.row][new_pos.col] = True

        # Up Right
        new_pos = Position(row - 1, col + 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.row][new_pos.col] = True

        # Right
        new_pos = Position(row, col + 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.row][new_pos.col] = True

        # Down Right
        new_pos = Position(row + 1, col + 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.row][new_pos.col] = True

        # Down
        new_pos = Position(row + 1, col)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.row][new_pos.col] = True

        # Down Left
        new_pos = Position(row + 1, col - 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.row][new_pos.col] = True

        # Left
        new_pos = Position(row, col - 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.row][new_pos.col] = True

        # Up Left
        new_pos = Position(row - 1, col - 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.row][new_pos.col] = True

        return possible_moves

    def houses_to_enemy_king(self) -> list[Position]:
        return []
