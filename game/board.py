from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.piece import Piece
    from game.position import Position
    from chess.king import King


class Board:
    def __init__(self, rows=8, cols=8):
        self.__board = []
        self.__rows = rows
        self.__cols = cols
        for row in range(0, rows):
            self.__board.append([])
            for _ in range(0, cols):
                self.__board[row].append(None)

    @property
    def board(self) -> list:
        return self.__board

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def cols(self) -> int:
        return self.__cols

    def get_piece_by_position(self, position: Position) -> (None | Piece):
        return self.__board[position.x][position.y]

    def valid_position(self, position: Position, color: str) -> bool:
        if position.x < 0 or position.x >= self.__board.rows:
            return False

        if position.y < 0 or position.y >= self.__board.cols:
            return False

        piece_in_pos = self.get_piece_by_position(position)
        if piece_in_pos != None and piece_in_pos.color == color:
            return False

        return True

    def addPiece(self, piece: Piece, position: Position):
        self.__board[position.x][position.y] = piece
