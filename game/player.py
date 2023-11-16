from game.position import Position


class Player:
    def __init__(self, color: str):
        self.__color = color

    @property
    def color(self) -> str:
        return self.__color

    def get_enemy(self) -> str:
        return "white" if self.color == "black" else "black"
