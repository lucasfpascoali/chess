from __future__ import annotations
from game.piece import Piece
from game.position import Position
from game.board import Board


class Pawn(Piece):
    def __init__(self, color: str, position: Position, board: Board):
        super().__init__(color, position, board, 'P')
        self.__is_first_move = True

    def move(self) -> None:
        if self.__is_first_move:
            self.__is_first_move = False

    def possible_moves(self) -> list[list[bool]]:
        possible_moves = []
        for row in range(0, self.board.rows):
            possible_moves.append([])
            for _ in range(0, self.board.cols):
                possible_moves[row].append(False)

        # Pawn can only go straight, so we need to know what direction its looking
        increment = -1 if self.color == "white" else 1
        if self.board.valid_position(Position(self.position.row + increment, self.position.col), self.color):
            possible_moves[self.position.row +
                           increment][self.position.col] = True

        # Pawn first move can be 2 houses
        if self.__is_first_move and self.board.valid_position(Position(self.position.row + (
                increment * 2), self.position.col), self.color):
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

        return possible_moves

    def houses_to_enemy_king(self) -> list[Position]:
        return []
