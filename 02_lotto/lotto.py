from random import randint

class LottoBag:
    """Класс для создания мешка с бочонками"""
    def __init__(self):
        self.__kegs = []
        while len(self.__kegs) < 90:
            new_keg = randint(1, 90)
            if new_keg not in self.__kegs:
                self.__kegs.append(new_keg)

    @property
    def kegs(self):
        """Свойство, чтобы посмотреть все оставшиеся в мешке бочонки в виде списка"""
        return self.__kegs

class LottoCard:
    """Класс для создания карточек с числами для игрока и компьютера"""
    def __init__(self):
        self.__numbers = []
        while len(self.__numbers) < 15:
            new_number = randint(1, 90)
            if new_number not in self.__numbers:
                self.__numbers.append(new_number)

    @property
    def numbers(self):
        """Свойство, чтобы выводить числа на карточке в виде списка"""
        return self.__numbers

    def __str__(self):
        """Метод для красивого вывода карточки"""
        return ' '.join([str(x) if x != '-' else ' - ' for x in self.__numbers])

    def cross_a_number(self, number):
        if number in self.__numbers:
            index = self.__numbers.index(number)
            self.__numbers[index] = "-"

    def numbers_finished(self) -> bool:
        return all(num == "-" for num in self.__numbers)

class Game:
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