from __future__ import annotations
from abc import ABC, abstractmethod
from game.position import Position
from game.board import Board


class Piece(ABC):
    def __init__(self, color: str, position: Position, board: Board, sign: str):
        self.__color = color
        self.__position = position
        self.__board = board
        self.__sign = sign

    @property
    def color(self) -> str:
        return self.__color

    @property
    def position(self) -> Position:
        return self.__position

    @property
    def board(self) -> Board:
        return self.__board

    @property
    def sign(self) -> str:
        return self.__sign

    @abstractmethod
    def possible_moves(self) -> list:
        pass
