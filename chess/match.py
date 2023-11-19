from __future__ import annotations
from chess.pawn import Pawn
from game.board import Board
from game.piece import Piece
from game.player import Player
from game.position import Position
from game.screen import Screen
from chess.bishop import Bishop
from chess.king import King
from chess.knight import Knight
from chess.queen import Queen
from chess.rook import Rook


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
        self.__setup_board()

        self.__screen.clear_console()

        while not self.__game_over:
            self.__play_turn(
                self.__players[0] if self.__white_plays else self.__players[1])

        self.__screen.print_game_over_message(self.__white_plays)
        return

    def __setup_board(self) -> None:
        configs = [{"color": "white", "row": 7},
                   {"color": "black", "row": 0}]

        # Placing first line pieces
        for config in configs:
            self.board.add_piece(Rook(config["color"], Position(
                config["row"], 0), self.board))
            self.board.add_piece(Rook(config["color"], Position(
                config["row"], 7), self.board))
            self.board.add_piece(Knight(config["color"], Position(
                config["row"], 1), self.board))
            self.board.add_piece(Knight(config["color"], Position(
                config["row"], 6), self.board))
            self.board.add_piece(Bishop(config["color"], Position(
                config["row"], 2), self.board))
            self.board.add_piece(Bishop(config["color"], Position(
                config["row"], 5), self.board))
            self.board.add_piece(Queen(config["color"], Position(
                config["row"], 3), self.board))
            self.board.add_piece(King(config["color"], Position(
                config["row"], 4), self.board))

        # Placing Pawns
        for row in range(0, 8):
            self.board.add_piece(Pawn("white", Position(6, row), self.board))
            self.board.add_piece(Pawn("black", Position(1, row), self.board))

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
        else:
            self.__normal_turn(player)

        if player.color == "black" and not self.__game_over:
            self.__turn += 1
            self.__white_plays = True
        else:
            self.__white_plays = False

    def __normal_turn(self, player: Player) -> None:
        while True:
            try:
                selected_piece = self.__screen.get_piece_to_be_moved(
                    player.color)

                self.__screen.clear_console()
                self.__screen.print_selected_piece_moves(selected_piece)

                next_position = self.__screen.get_piece_next_position(
                    selected_piece)

                self.board.move_piece(selected_piece, next_position)

                self.__screen.clear_console()
                self.__screen.print_board()

                break
            except Exception as e:
                self.__screen.clear_console()
                self.__screen.print_turn(self.__turn, player.color == "white")
                self.__screen.print_board()
                print(str(e))

    def __check_turn(self, player: Player, enemy_pieces: list[Piece]):
        if self.board.verify_mate(player.color, enemy_pieces):
            self.__game_over == True
            return

        possible_moves_to_block = []

        # If two pieces are atacking the king
        # or the piece is a knight, you cant block the check
        if len(enemy_pieces) == 1 and enemy_pieces[0].sign != 'N':
            possible_moves_to_block = [
                enemy_pieces[0].position, *enemy_pieces[0].houses_to_enemy_king()]

        self.__screen.print_check_message()

        while True:
            try:
                selected_piece = self.__screen.get_piece_to_be_moved_on_check(
                    player.color, possible_moves_to_block)

                selected_piece_possible_moves = selected_piece.possible_moves()

                intersection_pos_to_block_and_piece_moves = []
                for pos in possible_moves_to_block:
                    if selected_piece_possible_moves[pos.row][pos.col]:
                        intersection_pos_to_block_and_piece_moves.append(
                            [pos.row, pos.col])

                self.__screen.clear_console()
                self.__screen.print_piece_moves_on_check(
                    selected_piece, intersection_pos_to_block_and_piece_moves)

                next_position = self.__screen.get_piece_next_position_on_check(
                    selected_piece, intersection_pos_to_block_and_piece_moves)

                self.board.move_piece(selected_piece, next_position)

                break

            except Exception as e:
                self.__screen.clear_console()
                self.__screen.print_turn(self.__turn, player.color == "white")
                self.__screen.print_board()
                print(str(e))

        self.__screen.clear_console()
        self.__screen.print_board()
