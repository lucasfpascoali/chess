from __future__ import annotations
from game.piece import Piece
from game.position import Position
from game.board import Board


class Rook(Piece):
    def __init__(self, color: str, position: Position, board: Board):
        super().__init__(color, position, board, "R")
        self.__move_counter = 0

    def move(self) -> None:
        self.__move_counter += 1

    def undo_move(self) -> None:
        self.__move_counter -= 1

    def possible_moves(self) -> list[list[bool]]:
        possible_moves = []
        for row in range(0, self.board.rows):
            possible_moves.append([])
            for _ in range(0, self.board.cols):
                possible_moves[row].append(False)

        row = self.position.row
        col = self.position.col

        # Calculating possible moves to left
        for square in range(col - 1, -1, -1):
            pos = Position(row, square)
            if self.board.valid_position(pos, self.color):
                possible_moves[row][square] = True

            if self.board.position_has_piece(pos):
                break

        # Calculating possible moves to right
        for square in range(col + 1, self.board.cols):
            pos = Position(row, square)
            if self.board.valid_position(pos, self.color):
                possible_moves[row][square] = True

            if self.board.position_has_piece(pos):
                break

        # Calculating possible moves to up
        for square in range(row - 1, -1, -1):
            pos = Position(square, col)
            if self.board.valid_position(pos, self.color):
                possible_moves[square][col] = True

            if self.board.position_has_piece(pos):
                break

        # Calculating possible moves to down
        for square in range(row + 1, self.board.rows):
            pos = Position(square, col)
            if self.board.valid_position(pos, self.color):
                possible_moves[square][col] = True

            if self.board.position_has_piece(pos):
                break

        return possible_moves

    def houses_to_enemy_king(self) -> list[Position]:
        enemy_color = "white" if self.color == "black" else "black"
        enemy_king = self.board.get_king_by_color(enemy_color)

        houses_to_enemy_king = []
        # enemy king on same row
        if enemy_king.position.col == self.position.col:
            start = min(enemy_king.position.col, self.position.col) + 1
            end = max(enemy_king.position.col, self.position.col)
            for square in range(start, end):
                houses_to_enemy_king.append(
                    Position(square, self.position.col))

        if enemy_king.position.row == self.position.row:
            start = min(enemy_king.position.row, self.position.row) + 1
            end = max(enemy_king.position.row, self.position.row)
            for square in range(start, end):
                houses_to_enemy_king.append(
                    Position(self.position.row, square))

        return houses_to_enemy_king
