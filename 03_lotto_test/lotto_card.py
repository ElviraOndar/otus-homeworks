from random import randint


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
        """Функция для зачеркивания цифры, выпавшей на бочонке"""
        if number in self.__numbers:
            index = self.__numbers.index(number)
            self.__numbers[index] = "-"

    def numbers_finished(self) -> bool:
        """Функция, проверяющая, что все цифры на карточке зачеркнуты"""
        return all(num == "-" for num in self.__numbers)


if __name__ == '__main__':
    # Тестирование класса LottoCard (не будет выполнено при импорте)
    card = LottoCard()
    print(card.numbers)