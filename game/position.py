class Position:
    def __init__(self, row: int, col: int):
        self.__row = row
        self.__col = col

    @property
    def row(self) -> int:
        return self.__row

    @property
    def col(self) -> int:
        return self.__col
