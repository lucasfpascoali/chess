from __future__ import annotations
from game.piece import Piece
from game.position import Position
from game.board import Board


class King(Piece):
    def __init__(self, color: str, position: Position, board: Board):
        super().__init__(color, position, board, "K")

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

        # Removing the houses that are under attack
        for piece in self.board.get_pieces_in_game_by_color("white" if self.color == "black" else "black"):
            for move in all_king_moves:
                if self.board.valid_position(move, self.color):
                    all_king_moves.remove(move)
                    continue

                if self.board.valid_position(move, self.color) and piece.is_atacking_pos(move):
                    all_king_moves.remove(move)

        for move in all_king_moves:
            if self.board.valid_position(move, self.color):
                possible_moves[move.row][move.col] = True

        return possible_moves

    def houses_to_enemy_king(self) -> list[Position]:
        return []
