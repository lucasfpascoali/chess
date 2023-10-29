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
        self.__pieces_in_game = {"white": [], "black": []}
        self.__captured_pieces = {"white": [], "black": []}
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

    def position_has_piece(self, position: Position) -> bool:
        return self.get_piece_by_position(position) != None

    def valid_piece(self, position: Position, color: str) -> bool:
        if position.x < 0 or position.x >= self.__rows:
            return False

        if position.y < 0 or position.y >= self.__cols:
            return False

        piece_in_pos = self.get_piece_by_position(position)
        if piece_in_pos == None or piece_in_pos.color != color:
            return False

        return True

    def valid_position(self, position: Position, color: str) -> bool:
        if position.x < 0 or position.x >= self.__rows:
            return False

        if position.y < 0 or position.y >= self.__cols:
            return False

        piece_in_pos = self.get_piece_by_position(position)
        if piece_in_pos != None and piece_in_pos.color == color:
            return False

        return True

    def move_piece(self, piece: Piece, next_position: Position) -> None:
        if self.__board[next_position.x][next_position.y] != None:
            self.add_captured_piece(self.get_piece_by_position(next_position))

        self.__board[piece.position.x][piece.position.y] = None
        piece.change_position(next_position)
        self.__board[next_position.x][next_position.y] = piece

    def add_piece(self, piece: Piece, position: Position):
        self.__board[position.x][position.y] = piece
        self.__pieces_in_game[piece.color].append(piece)

    def add_captured_piece(self, piece: Piece):
        self.__captured_pieces[piece.color].append(piece)

    def get_captured_pieces_by_color(self, color: str) -> list:
        return self.__captured_pieces[color]

    def get_all_captured_pieces(self) -> list:
        return [*self.__captured_pieces["white"], *self.__captured_pieces["black"]]

    def get_pieces_in_game_by_color(self, color: str) -> list:
        return self.__pieces_in_game[color]

    def get_all_pieces_in_game(self) -> list:
        return [*self.__pieces_in_game["white"], *self.__pieces_in_game["black"]]
