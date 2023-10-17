from __future__ import annotations
from game.piece import Piece
from game.position import Position
from game.board import Board


class Tower(Piece):
    def __init__(self, color: str, position: Position, board: Board):
        super().__init__(color, position, board, "R")

    def possible_moves(self) -> list:
        possibleMoves = []
        for row in range(0, self.board.rows):
            possibleMoves.append([])
            for _ in range(0, self.board.cols):
                possibleMoves[row].append(False)

        x = self.position.x
        y = self.position.y

        # Calculating possible moves to left
        for square in range(y - 1, -1, -1):
            pos = Position(x, square)
            if self.__board.valid_position(pos, self.color):
                possibleMoves[x][square] = True

            if self.__board.position_has_piece(pos):
                break

        # Calculating possible moves to right
        for square in range(y + 1, self.__board.cols):
            pos = Position(x, square)
            if self.__board.valid_position(pos, self.color):
                possibleMoves[x][square] = True

            if self.__board.position_has_piece(pos):
                break

        # Calculating possible moves to up
        for square in range(x - 1, -1, -1):
            pos = Position(square, y)
            if self.__board.valid_position(pos, self.color):
                possibleMoves[square][y] = True

            if self.__board.position_has_piece(pos):
                break

        # Calculating possible moves to down
        for square in range(x + 1, self.__board.rows):
            pos = Position(square, y)
            if self.__board.valid_position(pos, self.color):
                possibleMoves[square][y] = True

            if self.__board.position_has_piece(pos):
                break

        return possibleMoves
