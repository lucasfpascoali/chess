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
        increment = -1 if self.color == "white" else -1
        possible_moves[self.position.x][self.position.y + increment] = True

        # Pawn first move can be 2 houses
        if self.__is_first_move:
            possible_moves[self.position.x][self.position.y +
                                            (increment * 2)] = True
