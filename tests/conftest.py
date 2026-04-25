import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product('Iphone 15', '512GB, Gray space', 8, 210000.0)


@pytest.fixture
def category_smartphone():
    return Category(
        'Смартфоны',
        'Смартфоны, как средство не только коммуникации, '
        'но и получение дополнительных функций для удобства жизни',
        [
            Product('Iphone 15', '512GB, Gray space', 8, 210000.0),
            Product('Xiaomi Redmi Note 11', '1024GB, Синий', 14, 31000.0)
        ]
    )


@pytest.fixture
def category_tv():
    return Category(
        'Телевизоры',
        'Современный телевизор, который позволяет наслаждаться просмотром, '
        'станет вашим другом и помощником',
        [
            Product('55" QLED 4K', 'Фоновая подсветка', 123000.0, 7)
        ]
    )
