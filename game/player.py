from game.position import Position


class Player:
    def __init__(self, color: str):
        self.__color = color

    def get_input(self) -> Position:
        print(
            f"Agora a vez é das {'brancas' if self.__color == 'white' else 'pretas'}!")
        player_input = input(
            "Digite a posição da peça a ser movida (ex: E4): ")

        while not self.__verify_input(player_input):
            print("Posição Inválida! Tente Novamente!")
            player_input = input(
                "Digite a posição da peça a ser movida (ex: E4): ")

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
