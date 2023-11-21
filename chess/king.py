from __future__ import annotations
from chess.rook import Rook
from game.piece import Piece
from game.position import Position
from game.board import Board


class King(Piece):
    def __init__(self, color: str, position: Position, board: Board):
        super().__init__(color, position, board, "K")
        self.__move_counter = 0
        self.__first_line = 0 if color == "black" else 7

    @property
    def first_line(self):
        return self.__first_line

    def move(self) -> None:
        self.__move_counter += 1

    def undo_move(self) -> None:
        self.__move_counter -= 1

    def possible_moves(self) -> list:
        possible_moves = []
        for row in range(0, self.board.rows):
            possible_moves.append([])
            for _ in range(0, self.board.cols):
                possible_moves[row].append(False)

        row = self.position.row
        col = self.position.col

        # Listing all the 8 houses king can go
        all_king_moves = [
            Position(row - 1, col),
            Position(row - 1, col + 1),
            Position(row, col + 1),
            Position(row + 1, col + 1),
            Position(row + 1, col),
            Position(row + 1, col - 1),
            Position(row, col - 1),
            Position(row - 1, col - 1)
        ]

        for move in all_king_moves:
            if self.board.valid_position(move, self.color):
                possible_moves[move.row][move.col] = True

        # Verifying if castle is possible
        if self.__move_counter != 0:
            return possible_moves

        if self.__verify_left_castle():
            possible_moves[self.__first_line][2] = True

        if self.__verify_right_castle():
            possible_moves[self.__first_line][6] = True

        return possible_moves

    def houses_to_enemy_king(self) -> list[Position]:
        return []

    def __verify_left_castle(self) -> bool:
        row = self.__first_line

        left_tower = self.board.get_piece_by_position(Position(row, 0))

        # Can't castle if houses between king and tower aren't empty
        if self.board.get_piece_by_position(Position(self.__first_line, 1)) != None or self.board.get_piece_by_position(Position(self.__first_line, 2)) != None or self.board.get_piece_by_position(Position(self.__first_line, 3)) != None:
            return False

        # Can't castle if the rook already move
        if left_tower == None or left_tower.sign != 'R' or left_tower.color != self.color or left_tower.__move_counter != 0:
            return False

        enemy_pieces = self.board.get_pieces_in_game_by_color(
            "white" if self.color == "black" else "black")

        for enemy_piece in enemy_pieces:
            # Cant castle if king is in check or the houses between are under attack
            if enemy_piece.is_atacking_pos(self.position) or enemy_piece.is_atacking_pos(Position(row, 2)) or enemy_piece.is_atacking_pos(Position(row, 3)):
                return False

        return True

    def __verify_right_castle(self) -> bool:
        row = self.__first_line

        right_tower = self.board.get_piece_by_position(Position(row, 7))

        # Can't castle if houses between king and tower aren't empty
        if self.board.get_piece_by_position(Position(self.__first_line, 6)) != None or self.board.get_piece_by_position(Position(self.__first_line, 7)) != None:
            return False

        # Can't castle if the king or rook already move
        if right_tower == None or right_tower.sign != 'R' or right_tower.color != self.color or right_tower.__move_counter != 0:
            return False

        enemy_pieces = self.board.get_pieces_in_game_by_color(
            "white" if self.color == "black" else "black")

        for enemy_piece in enemy_pieces:
            # Cant castle if king is in check or the houses between are under attack
            if enemy_piece.is_atacking_pos(self.position) or enemy_piece.is_atacking_pos(Position(row, 5)) or enemy_piece.is_atacking_pos(Position(row, 6)):
                return False

        return True
