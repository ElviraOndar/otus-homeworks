import pytest
from lotto_bag import LottoBag
from lotto_card import LottoCard


@pytest.fixture
def new_lotto_bag():
    return LottoBag()


@pytest.fixture
def new_lotto_card():
    return LottoCard()
