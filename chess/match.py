from __future__ import annotations
from game.player import Player
from game.board import Board
from game.position import Position
from chess.king import King


class Match:
    def __init__(self):
        player1 = Player("white")
        player2 = Player("black")
        self.__turn = 1
        self.__players = [player1, player2]
        self.board = Board()

    def start_match(self):
        self.print_board()

    def print_board(self):
        for row in range(0, self.board.rows):
            print(f"{8 - row} ", end='')
            for col in range(0, self.board.cols):
                piece = self.board.get_piece_by_position(Position(row, col))
                if piece == None:
                    print("_ ", end='')
                else:
                    print(f"{piece.sign} ", end='')

            print()

        print("  a b c d e f g h")
