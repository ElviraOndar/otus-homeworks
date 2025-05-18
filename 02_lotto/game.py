from lotto_bag import LottoBag
from lotto_card import LottoCard


class Game:
    """Это функция 1) создает карточки игрока и компьютера,
    2) создает мешок с 90 бочонками,
    3) запускает игру,
    4) проверяет, правильно ли действует игрок,
    5) завершает игру в случае поражения или победы игрока
    """
    __player_card = None
    __computer_card = None
    __kegs = []

    def __init__(self):
        self.__player_card = LottoCard()
        self.__computer_card = LottoCard()
        self.__kegs = LottoBag().kegs

    def play_round(self) -> int:
        """0 - игра продолжается
        1 - игрок победил
        2 - компьютер победил"""

        keg = self.__kegs.pop()

        print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
        print(f'----- Ваша карточка ------\n{self.__player_card}')
        print(f'-- Карточка компьютера ---\n{self.__computer_card}')

        player_decision = input('Зачеркнуть цифру? Введите "да" или "нет": ').lower().strip()
        if player_decision == 'да' and not keg in self.__player_card.numbers or \
                player_decision != 'да' and keg in self.__player_card.numbers:
            return 2

        if keg in self.__player_card.numbers:
            self.__player_card.cross_a_number(keg)
            if self.__player_card.numbers_finished():
                return 1
        if keg in self.__computer_card.numbers:
            self.__computer_card.cross_a_number(keg)
            if self.__computer_card.numbers_finished():
                return 2

        return 0


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round()
        if score == 1:
            print('Вы победили')
            break
        elif score == 2:
            print('Вы проиграли')
            break



