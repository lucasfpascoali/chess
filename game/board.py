from __future__ import annotations
from math import pi
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from game.piece import Piece
    from game.position import Position
    from chess.pawn import Pawn


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
        return self.__board[position.row][position.col]

    def position_has_piece(self, position: Position) -> bool:
        return self.get_piece_by_position(position) != None

    def valid_piece(self, position: Position, color: str) -> bool:
        if position.row < 0 or position.row >= self.__rows:
            return False

        if position.col < 0 or position.col >= self.__cols:
            return False

        piece_in_pos = self.get_piece_by_position(position)
        if piece_in_pos == None or piece_in_pos.color != color:
            return False

        return True

    def valid_position(self, position: Position, color: str) -> bool:
        if position.row < 0 or position.row >= self.__rows:
            return False

        if position.col < 0 or position.col >= self.__cols:
            return False

        piece_in_pos = self.get_piece_by_position(position)
        if piece_in_pos != None and piece_in_pos.color == color:
            return False

        return True

    def move_piece(self, piece: Piece, next_position: Position) -> None:
        if self.__board[next_position.row][next_position.col] != None:
            self.add_captured_piece(self.get_piece_by_position(
                next_position))

        if piece.sign == 'P':
            piece.move()

        self.__board[piece.position.row][piece.position.col] = None
        piece.change_position(next_position)
        self.__board[next_position.row][next_position.col] = piece

    def add_captured_piece(self, piece: Piece) -> None:
        self.__captured_pieces[piece.color].append(piece)
        self.__pieces_in_game[piece.color].remove(piece)

    def get_captured_pieces_by_color(self, color: str) -> list[Piece]:
        return self.__captured_pieces[color]

    def get_all_captured_pieces(self) -> list[Piece]:
        return [*self.__captured_pieces["white"], *self.__captured_pieces["black"]]

    def get_pieces_in_game_by_color(self, color: str) -> list[Piece]:
        return self.__pieces_in_game[color]

    def get_all_pieces_in_game(self) -> list[Piece]:
        return [*self.__pieces_in_game["white"], *self.__pieces_in_game["black"]]

    def get_king_by_color(self, color: str) -> Piece:
        for piece in self.__pieces_in_game[color]:
            if piece.sign == 'K':
                return piece

    def verify_check(self, color: str) -> list[Piece]:
        player_king = self.get_king_by_color(color)
        enemy_color = "white" if color == "black" else "black"
        enemy_pieces_atacking = []

        for piece in self.get_pieces_in_game_by_color(enemy_color):
            if piece.is_atacking_pos(player_king.position):
                enemy_pieces_atacking.append(piece)

        return enemy_pieces_atacking

    def verify_mate(self, color: str, enemy_pieces_atacking: list[Piece]) -> bool:
        player_king = self.get_king_by_color(color)
        for enemy_piece in enemy_pieces_atacking:
            if len(enemy_piece.houses_to_enemy_king()) > 0:
                return False

        if len(player_king.possible_moves()) > 0:
            return False

        return True

    def add_piece(self, piece: Piece) -> None:
        self.__board[piece.position.row][piece.position.col] = piece
        self.__pieces_in_game[piece.color].append(piece)
