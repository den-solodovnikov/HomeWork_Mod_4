import pytest

from src.category import Category
from src.product import Product


class FaikProduct:
    """ Фейковый класс продуктов. """
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


def test_category_init(category_smartphone, category_tv):
    assert category_smartphone.name == 'Смартфоны'
    assert category_smartphone.description == (
        'Смартфоны, как средство не только коммуникации, '
        'но и получение дополнительных функций для удобства жизни'
    )
    assert category_smartphone.category_count == 4
    assert category_tv.product_count == 4


def test_add_product():
    category = Category("Смартфоны", "Средство коммуникации", [])
    product = Product("Nokia", "Dark_Grey", 20000, 3)

    category.add_product(product)

    assert Category.category_count == 5
    assert Category.category_count == 5  # Проверяем, что продукт добавлен в категорию
    assert Category.product_count == 5

    faik_product = FaikProduct("Nokia", "Dark_Grey", 20000, 3)
    with pytest.raises(TypeError):
        result = category.add_product(faik_product)
        assert result == (f'Нельзя добавить {faik_product}, т.к. он не является объектом класса Product,\n'
                          f'а также его подклассов')


def test_get_products():
    product = Product("Nokia", "Dark_Grey", 20000, 3)
    category = Category("Смартфоны", "Cредство коммуникации", [product])
    result = category.products.rstrip()
    assert result == "Nokia, 20000 руб. Остаток: 3 шт."


def test_category_str(category_smartphone):
    assert str(category_smartphone) == "Смартфоны, количество продуктов: 22 шт."
