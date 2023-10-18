from __future__ import annotations
from game.player import Player
from game.board import Board
from game.position import Position
from game.piece import Piece
from chess.king import King
from chess.tower import Tower
from chess.bishop import Bishop
from colorama import init as colorama_init
from colorama import Fore, Back, Style


class Match:
    def __init__(self):
        colorama_init()
        player1 = Player("white")
        player2 = Player("black")
        self.__turn = 1
        self.__players = [player1, player2]
        self.board = Board()

    def start_match(self):
        self.board.addPiece(King("black", Position(7, 4),
                            self.board), Position(7, 4))
        self.board.addPiece(Tower("white", Position(7, 0),
                            self.board), Position(7, 0))
        self.board.addPiece(Bishop("white", Position(3, 3),
                            self.board), Position(3, 3))

        self.print_board()

        white_input = self.__players[0].get_input()
        selectedPiece = self.board.get_piece_by_position(white_input)

        self.print_selected_piece_moves(selectedPiece)

    def print_board(self):
        for row in range(0, self.board.rows):
            print(f"{8 - row} ", end='')
            for col in range(0, self.board.cols):
                piece = self.board.get_piece_by_position(Position(row, col))
                self.__print_piece(piece)

            print()

        print("  a b c d e f g h")

    def print_selected_piece_moves(self, piece: Piece):
        possible_moves = piece.possible_moves()
        for row in range(0, self.board.rows):
            print(f"{8 - row} ", end='')
            for col in range(0, self.board.cols):
                piece_on_pos = self.board.get_piece_by_position(
                    Position(row, col))
                if possible_moves[row][col] and piece_on_pos == None:
                    print(f"{Back.RED}x{Style.RESET_ALL} ", end='')
                elif possible_moves[row][col] and piece_on_pos.color != piece.color:
                    print(Back.RED, end='')
                    self.__print_piece(piece_on_pos)
                    print(Style.RESET_ALL, end='')
                else:
                    self.__print_piece(piece_on_pos)

            print()

        print("  a b c d e f g h")

    def __print_piece(self, piece: Piece | None):
        if piece == None:
            print("_ ", end='')
        elif piece.color == 'white':
            print(f"{piece.sign} ", end='')
        else:
            print(f"{Fore.YELLOW}{piece.sign}{Style.RESET_ALL} ", end='')
