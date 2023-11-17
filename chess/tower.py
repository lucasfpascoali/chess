from __future__ import annotations
from game.piece import Piece
from game.position import Position
from game.board import Board


class Tower(Piece):
    def __init__(self, color: str, position: Position, board: Board):
        super().__init__(color, position, board, "R")

    def possible_moves(self) -> list[list[bool]]:
        possible_moves = []
        for row in range(0, self.board.rows):
            possible_moves.append([])
            for _ in range(0, self.board.cols):
                possible_moves[row].append(False)

        x = self.position.x
        y = self.position.y

        # Calculating possible moves to left
        for square in range(y - 1, -1, -1):
            pos = Position(x, square)
            if self.board.valid_position(pos, self.color):
                possible_moves[x][square] = True

            if self.board.position_has_piece(pos):
                break

        # Calculating possible moves to right
        for square in range(y + 1, self.board.cols):
            pos = Position(x, square)
            if self.board.valid_position(pos, self.color):
                possible_moves[x][square] = True

            if self.board.position_has_piece(pos):
                break

        # Calculating possible moves to up
        for square in range(x - 1, -1, -1):
            pos = Position(square, y)
            if self.board.valid_position(pos, self.color):
                possible_moves[square][y] = True

            if self.board.position_has_piece(pos):
                break

        # Calculating possible moves to down
        for square in range(x + 1, self.board.rows):
            pos = Position(square, y)
            if self.board.valid_position(pos, self.color):
                possible_moves[square][y] = True

            if self.board.position_has_piece(pos):
                break

        return possible_moves

    def houses_to_enemy_king(self) -> list[Position]:
        enemy_color = "white" if self.color == "black" else "black"
        enemy_king = self.board.get_king_by_color(enemy_color)

        houses_to_enemy_king = []
        # enemy king on same row
        if enemy_king.position.y == self.position.y:
            start = min(enemy_king.position.y, self.position.y) + 1
            end = max(enemy_king.position.y, self.position.y)
            for square in range(start, end):
                houses_to_enemy_king.append(Position(square, self.position.y))

        if enemy_king.position.x == self.position.x:
            start = min(enemy_king.position.x, self.position.x) + 1
            end = max(enemy_king.position.x, self.position.x)
            for square in range(start, end):
                houses_to_enemy_king.append(Position(self.position.x, square))

        return houses_to_enemy_king
