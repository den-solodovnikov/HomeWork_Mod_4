import pytest


def test_category_iterator(iter_category):
    assert iter_category.index == 0
    assert next(iter_category) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert next(iter_category) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    assert iter_category.index == 2
    assert next(iter_category) == ""
    assert iter_category.index == 3
    with pytest.raises(StopIteration):
        next(iter_category)
