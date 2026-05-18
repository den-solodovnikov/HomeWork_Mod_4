import pytest

from src.product import Product, Smartphone, LawnGrass


def test_product_init(product):
    assert product.name == 'Iphone 15'
    assert product.description == '512GB, Gray space'
    assert product.price == 210000.0
    assert product.quantity == 8


def test_product_init_value_error():
    with pytest.raises(ValueError):
        Product("Iphone 15", "512GB, Gray space", 10000.0, 0)


@pytest.fixture
def new_product_dict():
    return {"name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8
            }


def test_new_product(product, new_product_dict):
    product.new_product(new_product_dict)
    assert product.name == 'Iphone 15'
    assert product.description == '512GB, Gray space'
    assert product.price == 210000.0
    assert product.quantity == 8


def test_prise_setter():
    product = Product("Iphone 15", "512GB, Gray space", 10000.0, 2)
    product.price = 20000.0
    assert product.price == 20000.0


# def test_product_str(product, product_str):
#     assert str(product) == product_str


def test_product_add(product, product1, smartphone1, lawngrass1, lawngrass2):
    assert product + product1 == 2580000.0
    assert lawngrass1 + lawngrass2 == 16750.0
    with pytest.raises(TypeError):
        total_amount = lawngrass1 + smartphone1
        assert total_amount == 'Нельзя складывать товары разных категорий'
    with pytest.raises(TypeError):
        total_amount = product + smartphone1
        assert total_amount == 'Нельзя складывать товары разных категорий'


def test_smartphone_init(smartphone1):
    assert smartphone1.name == 'Iphone 15'
    assert smartphone1.description == '512GB, Gray space'
    assert smartphone1.price == 210000.0
    assert smartphone1.quantity == 8
    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == '15'
    assert smartphone1.memory == 512
    assert smartphone1.color == 'Gray space'


def test_prise_setter_smartphone():
    smartphone = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 18000.0,
        5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone.price = 20000.0
    assert smartphone.price == 20000.0


# def test_smartphone_str(smartphone1, product_str):
#     assert str(smartphone1) == product_str


@pytest.fixture
def new_smartphone_dict():
    return {"name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8,
            "efficiency": 98.2,
            "model": "15",
            "memory": 512,
            "color": "Gray space"
            }


def test_new_smartphone_dict(smartphone1, new_smartphone_dict):
    smartphone1.new_product(new_smartphone_dict)
    assert smartphone1.name == 'Iphone 15'
    assert smartphone1.description == '512GB, Gray space'
    assert smartphone1.price == 210000.0
    assert smartphone1.quantity == 8
    assert smartphone1.efficiency == 98.2
    assert smartphone1.model == '15'
    assert smartphone1.memory == 512
    assert smartphone1.color == 'Gray space'


def test_lawngrass_init(lawngrass1):
    assert lawngrass1.name == 'Газонная трава'
    assert lawngrass1.description == 'Элитная трава для газона'
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20
    assert lawngrass1.country == 'Россия'
    assert lawngrass1.germination_period == '7 дней'
    assert lawngrass1.color == 'Зеленый'


def test_prise_setter_lawngrass():
    lawngrass = LawnGrass(
        "Газонная трава", "Элитная трава для газона", 500.0, 20,
        "Россия", "7 дней", "Зеленый")
    lawngrass.price = 700.0
    assert lawngrass.price == 700.0


# def test_lawngrass_str(lawngrass1):
#     assert str(lawngrass1) == 'Газонная трава, 500.0 руб. Остаток: 20 шт.'
