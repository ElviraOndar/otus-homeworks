import pytest
from lotto_bag import LottoBag
from lotto_card import LottoCard
from game import Game


@pytest.fixture
def new_lotto_bag():
    return LottoBag()


@pytest.fixture
def new_lotto_card():
    return LottoCard()


@pytest.fixture
def new_game():
    return Game()