from unittest.mock import patch
import pytest


def test_game(new_game):
    """Функция тестирует, правильно ли создаются объекты после начала игры"""
    # Проверяем, что у игрока и компьютера есть карточки, а в них содержится 15 цифр
    assert len(new_game._Game__player_card.numbers) == 15
    assert len(new_game._Game__computer_card.numbers) == 15

    # Проверяем, что мешок содержит 90 бочонков
    assert len(new_game._Game__kegs) == 90














