from xml.etree.ElementTree import PI
from colorama import init as colorama_init
from colorama import Fore, Back, Style
from game.board import Board
from game.piece import Piece
from game.position import Position
import os


class Screen:
    def __init__(self, board: Board) -> None:
        colorama_init()
        self.board = board

    def print_board(self) -> None:
        for row in range(0, self.board.rows):
            print(f"{8 - row} ", end='')
            for col in range(0, self.board.cols):
                piece = self.board.get_piece_by_position(Position(row, col))
                self.__print_piece(piece)

            print()

        print("  a b c d e f g h")

    def print_selected_piece_moves(self, piece: Piece) -> None:
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

    def print_turn(self, turn: int, whites_play: bool) -> None:
        print(f"Turno {turn}")
        print(f"Agora é a vez das {'brancas' if whites_play else 'pretas'}!")

    def print_invalid_piece_to_move(self) -> None:
        print("A posição selecionada não contém uma peça da sua cor!")
        print("Digite outra posição!")

    def print_captured_pieces(self, white_pieces: list[Piece], black_pieces: list[Piece]) -> None:
        print("Peças brancas capturadas: ", end='')
        for white_piece in white_pieces:
            self.__print_piece(white_piece)
        print()
        print("Peças pretas capturadas: ", end='')
        for black_piece in black_pieces:
            self.__print_piece(black_piece)
        print()

    def print_in_game_pieces(self, white_pieces: list[Piece], black_pieces: list[Piece]) -> None:
        print("Peças brancas em jogo: ", end='')
        for white_piece in white_pieces:
            self.__print_piece(white_piece)
        print()
        print("Peças pretas em jogo: ", end='')
        for black_piece in black_pieces:
            self.__print_piece(black_piece)
        print()

    def clear_console(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_piece_to_be_moved(self, player_color: str) -> Piece:
        while True:
            try:
                player_input = self.__get_input(
                    "Digite a posição da peça a ser movida: ")
                if not self.board.valid_piece(player_input, player_color):
                    raise Exception(
                        "A posição digitada não contém uma peça da sua cor!")

                return self.board.get_piece_by_position(player_input)

            except Exception as e:
                print(str(e))

    def get_piece_next_position(self, piece: Piece) -> Position:
        while True:
            try:
                player_input = self.__get_input(
                    "Digite a posição que você quer que a peça vá:")

                if not piece.possible_moves()[player_input.x][player_input.y]:
                    raise Exception(
                        "A sua peça não pode se mover para essa direção")

                return player_input
            except Exception as e:
                print(str(e))

    def __print_piece(self, piece: Piece) -> None:
        if piece == None:
            print("_ ", end='')
        elif piece.color == 'white':
            print(f"{piece.sign} ", end='')
        else:
            print(f"{Fore.YELLOW}{piece.sign}{Style.RESET_ALL} ", end='')

    def __get_input(self, input_message: str) -> Position:
        player_input = input(input_message)

        if not self.__verify_input(player_input):
            raise Exception("Posição Inválida! Tente Novamente")

        return self.__convert_input_to_position(player_input)

    def __convert_input_to_position(self, player_input: str) -> Position:
        # in ASCII, 97 is 'a', col is a letter between a and h
        # and in array counting pattern, a is 0, b is 1 and so on
        col = (ord(player_input[0].lower()) - 97)
        row = 8 - int(player_input[1])
        return Position(row, col)

    def __verify_input(self, player_input: str) -> bool:
        if len(player_input) != 2:
            return False

        if player_input[0].lower() not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            return False

        if player_input[1] not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            return False

        return True
