def test_lotto_bag(new_lotto_bag):
    """Функция тестирует, что 1) объект класса LottoCard создается корректно,
    2) генерируется ровно 90 бочонков,
    3) все бочонки уникальны,
    4) все бочонки находятся в диапазоне от 1 до 90"""
    assert len(new_lotto_bag.kegs) == 90  #создается 90 бочонков
    assert len(set(new_lotto_bag.kegs)) == 90  #все бочонки должны быть уникальными
    assert all(1 <= keg <= 90 for keg in new_lotto_bag.kegs)  #Бочонки должны быть в диапазоне
    # от 1 до 90



