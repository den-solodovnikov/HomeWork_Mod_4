from src.category import Category
from src.product import Product


def test_category_init(category_smartphone, category_tv):
    assert category_smartphone.name == 'Смартфоны'
    assert category_smartphone.description == (
        'Смартфоны, как средство не только коммуникации, '
        'но и получение дополнительных функций для удобства жизни'
    )
    assert len(category_smartphone.get_products) == 2
    assert category_smartphone.category_count == 4
    assert category_tv.product_count == 4


def test_add_product():
    category = Category("Смартфоны", "Cредство коммуникации", [])
    product = Product("Nokia", "Dark_Grey", 20000, 3)
    initial_product_count = Category.product_count

    category.add_product(product)

    assert Category.category_count == 5
    assert Category.category_count == 5  # Проверяем, что продукт добавлен в категорию
    assert Category.product_count == initial_product_count


def test_get_products():
    product = Product("Nokia", "Dark_Grey", 3, 20000)
    category = Category("Смартфоны", "Cредство коммуникации", [product])
    result = category.get_products
    assert result == ["Nokia, 20000 руб. Остаток: 3 шт."]
