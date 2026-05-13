import pytest

from src.category import Category
from src.category_iterator import CategoryIterator
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture
def product():
    return Product('Iphone 15', '512GB, Gray space', 210000.0, 8)


@pytest.fixture
def product1():
    return Product('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)


@pytest.fixture
def product_str():
    return "Iphone 15, 210000.0 руб. Остаток: 8 шт."


@pytest.fixture
def category_smartphone():
    return Category(
        'Смартфоны',
        'Смартфоны, как средство не только коммуникации, '
        'но и получение дополнительных функций для удобства жизни',
        [
            Product('Iphone 15', '512GB, Gray space', 210000.0, 8),
            Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
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


@pytest.fixture
def iter_category(category_smartphone):
    return CategoryIterator(category_smartphone)


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8,
        98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone2():
    return Smartphone(
        "Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14,
        90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def lawngrass1():
    return LawnGrass(
        "Газонная трава", "Элитная трава для газона", 500.0, 20,
        "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass2():
    return LawnGrass(
        "Газонная трава 2", "Выносливая трава", 450.0, 15,
        "США", "5 дней", "Темно-зеленый"
    )
