def test_lotto_card(new_lotto_card):
    """Функция тестирует, что
        1) объект класса LottoCard создает 15 чисел,
        2) что эти 15 чисел уникальны,
        3) что эти числа находятся в диапазоне от 1 до 90 (если не зачеркнуты)"""

    assert len(new_lotto_card.numbers) == 15  # создается 15 чисел
    assert len(set(new_lotto_card.numbers)) == 15  # числа уникальны
    assert all(1 <= num <= 90 for num in new_lotto_card.numbers if num != "-")  # числа в диапазоне
    # от 1 до 90


def test_cross_a_number(new_lotto_card):
    """"Эта функция тестирует, что метод cross_a_number заменяет цифру на знак прочерка"""
    number_to_cross = new_lotto_card.numbers[0]
    new_lotto_card.cross_a_number(number_to_cross)
    assert new_lotto_card.numbers[0] == "-"
    assert number_to_cross not in new_lotto_card.numbers


def test_numbers_finished_returns_true(new_lotto_card):
    """Эта функция тестирует, что метод numbers_finished возвращает True,
    когда все цифры зачеркнуты"""
    for number in new_lotto_card.numbers:
        new_lotto_card.cross_a_number(number)
    assert new_lotto_card.numbers_finished() is True


def test_numbers_finished_returns_false(new_lotto_card):
    """Эта функция тестирует, что метод numbers_finished возвращает False,
    когда не все цифры зачеркнуты"""
    number = new_lotto_card.numbers[0]
    new_lotto_card.cross_a_number(number)
    assert new_lotto_card.numbers_finished() is False


def test_str_lotto_card(new_lotto_card):
    """Тестирует метод __str__ для корректного вывода карточки"""
    str_lotto_card = str(new_lotto_card)
    assert len(str_lotto_card.split()) == 15  # проверяем, что в строковом представлении осталось 15 элементов







