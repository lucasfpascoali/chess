from __future__ import annotations
from typing import TYPE_CHECKING
from game.position import Position

if TYPE_CHECKING:
    from game.piece import Piece


class Board:
    def __init__(self, rows=8, cols=8):
        self.__board = []
        self.__rows = rows
        self.__cols = cols
        self.__pieces_in_game = {"white": [], "black": []}
        self.__captured_pieces = {"white": [], "black": []}
        self.__pieces_with_move_counter = ['K', 'P', 'R']
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
        original_pos = piece.position

        captured_piece = self.__execute_move(piece, next_position)

        if piece.sign in self.__pieces_with_move_counter:
            piece.move()

        if self.verify_check(piece.color):
            if piece.sign in self.__pieces_with_move_counter:
                piece.undo_move()

            self.__undo_move(piece, captured_piece,
                             original_pos, next_position)
            raise Exception(
                "Você não pode realizar um movimento que deixe seu rei em cheque!")

    def castle_move(self, piece: Piece, next_position: Position) -> None:
        tower = None
        first_line = next_position.row
        if next_position.col == 6:
            tower = self.get_piece_by_position(Position(first_line, 7))
            self.__execute_move(tower, Position(first_line, 5))
        else:
            tower = self.get_piece_by_position(Position(first_line, 0))
            self.__execute_move(tower, Position(first_line, 3))

        self.__execute_move(piece, next_position)

    def add_captured_piece(self, piece: Piece) -> None:
        self.__captured_pieces[piece.color].append(piece)
        self.__pieces_in_game[piece.color].remove(piece)

    def undo_add_captured_piece(self, piece: Piece | None) -> None:
        if piece == None:
            return

        self.__captured_pieces[piece.color].remove(piece)
        self.__pieces_in_game[piece.color].append(piece)

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

    def verify_check(self, color: str) -> bool:
        player_king = self.get_king_by_color(color)
        enemy_color = "white" if color == "black" else "black"

        for piece in self.get_pieces_in_game_by_color(enemy_color):
            piece_moves = piece.possible_moves()
            if (piece_moves[player_king.position.row][player_king.position.col]):
                return True

        return False

    def verify_mate(self, color: str) -> bool:
        for piece in self.get_pieces_in_game_by_color(color):
            piece_moves = piece.possible_moves()
            for row in range(0, self.rows):
                for col in range(0, self.cols):
                    if piece_moves[row][col]:
                        origin_pos = piece.position
                        captured_piece = self.__execute_move(
                            piece, Position(row, col))
                        is_check = self.verify_check(color)
                        self.__undo_move(piece, captured_piece,
                                         origin_pos, Position(row, col))
                        if not is_check:
                            return False

        return True

    def add_piece(self, piece: Piece) -> None:
        self.__board[piece.position.row][piece.position.col] = piece
        self.__pieces_in_game[piece.color].append(piece)

    def __execute_move(self, piece: Piece, target_pos: Position) -> Piece | None:
        captured_piece = self.get_piece_by_position(target_pos)
        if captured_piece != None:
            self.add_captured_piece(captured_piece)

        self.board[piece.position.row][piece.position.col] = None
        piece.change_position(target_pos)
        self.board[target_pos.row][target_pos.col] = piece

        return captured_piece

    def __undo_move(self, piece: Piece, captured_piece: Piece | None, original_pos: Position, target_pos) -> None:
        piece.change_position(original_pos)
        self.board[original_pos.row][original_pos.col] = piece
        if captured_piece != None:
            self.undo_add_captured_piece(captured_piece)

        self.board[target_pos.row][target_pos.col] = captured_piece
