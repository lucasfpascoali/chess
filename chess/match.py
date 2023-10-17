from __future__ import annotations
from game.player import Player
from game.board import Board
from game.position import Position
from game.piece import Piece
from chess.king import King
from chess.tower import Tower


class Match:
    def __init__(self):
        player1 = Player("white")
        player2 = Player("black")
        self.__turn = 1
        self.__players = [player1, player2]
        self.board = Board()

    def start_match(self):
        self.board.addPiece(King("white", Position(7, 4),
                            self.board), Position(7, 4))
        self.board.addPiece(Tower("white", Position(7, 0),
                            self.board), Position(7, 0))

        self.print_board()

        white_input = self.__players[0].get_input()
        selectedPiece = self.board.get_piece_by_position(white_input)

        self.print_selected_piece_moves(selectedPiece)

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

    def print_selected_piece_moves(self, piece: Piece):
        possible_moves = piece.possible_moves()
        for row in range(0, self.board.rows):
            print(f"{8 - row} ", end='')
            for col in range(0, self.board.cols):
                piece_on_pos = self.board.get_piece_by_position(
                    Position(row, col))
                if possible_moves[row][col]:
                    print("X ", end='')
                elif piece_on_pos == None:
                    print("_ ", end='')
                else:
                    print(f"{piece_on_pos.sign} ", end='')

            print()

        print("  a b c d e f g h")
