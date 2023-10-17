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

        x = self.position.x
        y = self.position.y

        # Up
        new_pos = Position(x - 1, y)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.x][new_pos.y] = True

        # Up Right
        new_pos = Position(x - 1, y + 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.x][new_pos.y] = True

        # Right
        new_pos = Position(x, y + 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.x][new_pos.y] = True

        # Down Right
        new_pos = Position(x + 1, y + 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.x][new_pos.y] = True

        # Down
        new_pos = Position(x + 1, y)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.x][new_pos.y] = True

        # Down Left
        new_pos = Position(x + 1, y - 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.x][new_pos.y] = True

        # Left
        new_pos = Position(x, y - 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.x][new_pos.y] = True

        # Up Left
        new_pos = Position(x - 1, y - 1)
        if self.board.valid_position(new_pos, self.color):
            possible_moves[new_pos.x][new_pos.y] = True

        return possible_moves
