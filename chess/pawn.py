from __future__ import annotations
from game.piece import Piece
from game.position import Position
from game.board import Board


class Pawn(Piece):
    def __init__(self, color: str, position: Position, board: Board):
        super().__init__(color, position, board, 'P')
        self.__move_counter = 0
        self.__made_double_move = True

    @property
    def move_counter(self) -> int:
        return self.__move_counter

    @property
    def made_double_move(self) -> bool:
        return self.__made_double_move

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

        # Pawn can only go straight, so we need to know what direction its looking
        increment = -1 if self.color == "white" else 1
        if not self.board.position_has_piece(Position(self.position.row + increment, self.position.col)) and self.board.valid_position(Position(self.position.row + increment, self.position.col), self.color):
            possible_moves[self.position.row +
                           increment][self.position.col] = True

        # Pawn first move can be 2 houses
        if self.__move_counter == 0 and self.board.valid_position(Position(self.position.row + (
                increment * 2), self.position.col), self.color) and not self.board.position_has_piece(Position(self.position.row + (increment * 2), self.position.col)):
            possible_moves[self.position.row + (
                increment * 2)][self.position.col] = True

        # Atacking pieces diagonally
        up_right_pos = Position(
            self.position.row + increment, self.position.col + 1)

        up_left_pos = Position(self.position.row +
                               increment, self.position.col - 1)

        if self.board.valid_position(up_right_pos, self.color) and self.board.position_has_piece(up_right_pos):
            possible_moves[up_right_pos.row][up_right_pos.col] = True

        if self.board.valid_position(up_left_pos, self.color) and self.board.position_has_piece(up_left_pos):
            possible_moves[up_left_pos.row][up_left_pos.col] = True

        left_side_pos = Position(self.position.row, self.position.col - 1)
        right_side_pos = Position(self.position.row, self.position.col + 1)

        line_increment = 1 if self.color == "black" else -1

        # Verifying en passant
        if self.board.valid_position(left_side_pos, self.color) and self.__verify_enpassant(left_side_pos):
            possible_moves[left_side_pos.row +
                           increment][left_side_pos.col] = True

        if self.board.valid_position(right_side_pos, self.color) and self.__verify_enpassant(right_side_pos):
            possible_moves[right_side_pos.row +
                           increment][right_side_pos.col] = True

        return possible_moves

    def houses_to_enemy_king(self) -> list[Position]:
        return []

    def __verify_enpassant(self, piece_pos) -> bool:
        piece = self.board.get_piece_by_position(piece_pos)
        if piece == None or piece.sign != 'P' or piece.move_counter != 1 or not piece.made_double_move:
            return False

        return True
