from __future__ import annotations
from game.board import Board
from game.piece import Piece
from game.player import Player
from game.position import Position
from game.screen import Screen
from chess.bishop import Bishop
from chess.king import King
from chess.knight import Knight
from chess.queen import Queen
from chess.tower import Tower


class Match:
    def __init__(self):
        self.__turn = 1
        self.__white_plays = True
        self.__game_over = False
        player1 = Player("white")
        player2 = Player("black")
        self.__players = [player1, player2]
        self.board = Board()
        self.__screen = Screen(self.board)

    def start_match(self) -> None:
        self.board.add_piece(King("black", Position(7, 4),
                                  self.board), Position(7, 4))
        self.board.add_piece(King("white", Position(0, 4),
                                  self.board), Position(0, 4))
        self.board.add_piece(Tower("white", Position(7, 0),
                                   self.board), Position(7, 0))
        self.board.add_piece(Bishop("white", Position(3, 3),
                                    self.board), Position(3, 3))
        self.board.add_piece(Knight("black", Position(2, 2),
                                    self.board), Position(2, 2))
        self.board.add_piece(Queen("black", Position(3, 4),
                                   self.board), Position(3, 4))

        self.__screen.clear_console()

        while not self.__game_over:
            self.__play_turn(
                self.__players[0] if self.__white_plays else self.__players[1])

    def __play_turn(self, player: Player) -> None:
        self.__screen.clear_console()

        self.__screen.print_turn(self.__turn, player.color == "white")
        self.__screen.print_board()
        self.__screen.print_captured_pieces(self.board.get_captured_pieces_by_color(
            "white"), self.board.get_captured_pieces_by_color("black"))

        # REMOVE BEFORE DEPLOY
        self.__screen.print_in_game_pieces(self.board.get_pieces_in_game_by_color(
            "white"), self.board.get_pieces_in_game_by_color("black"))

        pieces_atacking_player_king = self.board.verify_check(player.color)

        if len(pieces_atacking_player_king) > 0:
            self.__check_turn(player, pieces_atacking_player_king)
            return

        self.__normal_turn(player)

        if player.color == "black":
            self.__turn += 1
            self.__white_plays = True
        else:
            self.__white_plays = False

    def __normal_turn(self, player: Player) -> None:
        selected_piece = self.__screen.get_piece_to_be_moved(player.color)

        self.__screen.clear_console()
        self.__screen.print_selected_piece_moves(selected_piece)

        next_position = self.__screen.get_piece_next_position(selected_piece)

        self.board.move_piece(selected_piece, next_position)

        self.__screen.clear_console()
        self.__screen.print_board()

    def __check_turn(self, player: Player, enemy_pieces: list[Piece]):
        pass
