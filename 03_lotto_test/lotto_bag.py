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


if __name__ == '__main__':
    # Тестирование класса LottoBag (не будет выполнено при импорте)
    bag = LottoBag()
    print(bag.kegs)


